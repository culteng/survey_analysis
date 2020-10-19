# use to generate idml report
# from simple_idml import idml
import win32com.client
from PIL import Image


def scale(image, max_size, method=Image.ANTIALIAS):
    # add whitespace to images to avoid cropping for fit in placeholders
    image.thumbnail(max_size, method)
    offset = (int((max_size[0] - image.size[0]) / 2), int((max_size[1] - image.size[1]) / 2))
    back = Image.new("RGB", max_size, "white")
    back.paste(image, offset)
    return back                
    

def img2idml(img, p, y1, x1, y2, x2):
    # place img on page [p] at location y1, x1, y2, x2
    myPage = myDocument.Pages.Item(p)
    myRectangle = myPage.Rectangles.Add()
    myRectangle.GeometricBounds = [y1, x1, y2, x2]
    myRectangle.StrokeWeight = 0
    myRectangle.Place(img)


def main(args):
    print("report.py main")
    docdir = "C:/gits/diversity_survey/template/faithandculture.idml"
    # my_idml_package = idml.IDMLPackage(docdir)
    testimg = 'C:/gits/diversity_survey/imgs/foo.png'

    app = win32com.client.Dispatch('InDesign.Application.2020')
    myDocument = app.Open(docdir)
    # deal with "this document contains 6 links to sources that are missing...."
    
    # resize then insert image
    will this work?:
        idContentToFrame = 1668575078   # from enum idFitOptions
        myRectangle.Fit(idContentToFrame)

    testimg = scale(testimg, [22,31]) # need to send testimg as image; not string of dir?
    img2idml(testimg, 2, "20p", "14p", "42p", "45p")
    
    myDocument.save() # opens popout window. need to execute in bckgrnd
    myDocument.Close()
    print('report.py main done')



if __name__ == '__main__':
    main(sys.argv[1:])

