from PIL import Image
import sys
import os

#set wd to current dir
os.chdir(os.path.dirname(__file__))
import image_manipulation as img_man

def resize(filename, size=1000):
    #get img from url
    img = Image.open(filename)

    #square img with blank space
    layer = img_man.square(img)
    #resize img to have height of size pixels
    img = layer.resize((size, size), Image.ANTIALIAS)

    #save img as id(A,B,...Z).jpg
    img.save(filename)

if (len(sys.argv) == 2):
    sys.argv.append(1000)

resize(sys.argv[1], sys.argv[2])
