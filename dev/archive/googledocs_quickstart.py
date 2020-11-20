from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# The ID of a sample document.
DOCUMENT_ID = '1KFczcmwTUqdSXzIF5e9E9ZPnBpPuVXztIfVEwa9RIdI'

def main():
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('./dev/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('./dev/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()

    print('The title of the document is: {}'.format(document.get('title')))


def replace_named_range(service, document_id, range_name, new_text):
    """Replaces the text in existing named ranges."""
    
    # Determine the length of the replacement text, as UTF-16 code units.
    # https://developers.google.com/docs/api/concepts/structure#start_and_end_index
    new_text_len = len(new_text.encode('utf-16-le')) / 2
    
    # Fetch the document to determine the current indexes of the named ranges.
    document = service.documents().get(documentId=document_id).execute()
    
    # Find the matching named ranges.
    named_range_list = document.get('namedRanges', {}).get(range_name)
    if not named_range_list:
        raise Exception('The named range is no longer present in the document.')
    
    # Determine all the ranges of text to be removed, and at which indices the
    # replacement text should be inserted.
    all_ranges = []
    insert_at = {}
    for named_range in named_range_list.get('namedRanges'):
        ranges = named_range.get('ranges')
        all_ranges.extend(ranges)
        # Most named ranges only contain one range of text, but it's possible
        # for it to be split into multiple ranges by user edits in the document.
        # The replacement text should only be inserted at the start of the first
        # range.
        insert_at[ranges[0].get('startIndex')] = True
    
    # Sort the list of ranges by startIndex, in descending order.
    all_ranges.sort(key=lambda r: r.get('startIndex'), reverse=True)
    
    # Create a sequence of requests for each range.
    requests = []
    for r in all_ranges:
        # Delete all the content in the existing range.
        requests.append({
            'deleteContentRange': {
                'range': r
            }
        })
    
        segment_id = r.get('segmentId')
        start = r.get('startIndex')
        if insert_at[start]:
            # Insert the replacement text.
            requests.append({
                'insertText': {
                    'location': {
                        'segmentId': segment_id,
                        'index': start
                    },
                    'text': new_text
                }
            })
            # Re-create the named range on the new text.
            requests.append({
                'createNamedRange': {
                    'name': range_name,
                    'range': {
                        'segmentId': segment_id,
                        'startIndex': start,
                        'endIndex': start + new_text_len
                    }
                }
            })
    
    # Make a batchUpdate request to apply the changes, ensuring the document
    # hasn't changed since we fetched it.
    body = {
        'requests': requests,
        'writeControl': {
            'requiredRevisionId': document.get('revisionId')
        }
    }
    service.documents().batchUpdate(documentId=document_id, body=body).execute()



if __name__ == '__main__':
    main()