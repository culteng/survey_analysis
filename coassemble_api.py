import requests 
url = 'https://centerforunity.coassemble.com/api/v1/members?sort=namelastfirst&page=0&limit=5'
headers = {'Authorization': 'COASSEMBLE-V1-SHA256', 'UserId':'188473', 'UserToken':'79b30edc2d921f02d40f3e14de95f09a411bb6c478e10eeddc91161ff7a39e1a', 'accept': 'application/json'}
headers = {'accept': 'application/json', 'Authorization':'COASSEMBLE-V1-SHA256 UserId=188473, UserToken=79b30edc2d921f02d40f3e14de95f09a411bb6c478e10eeddc91161ff7a39e1a'}
r = requests.get(url, headers=headers)
r.text

Authorization: COASSEMBLE-V1-SHA256 UserId=188473, UserToken=79b30edc2d921f02d40f3e14de95f09a411bb6c478e10eeddc91161ff7a39e1a