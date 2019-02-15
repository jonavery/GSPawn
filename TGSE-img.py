import requests
import pandas as pd
import os
import math
import PIL
from PIL import Image

#set wd to current dir
os.chdir(os.path.dirname(__file__))

#make vector of letters for image names
letters = []
for letter in range(97,123):
    letters.append(chr(letter))

#open the csv file
df = pd.read_csv('TGSE-021218.csv')

#grab id's and url's from file
ids = df['Id']
urls = [df['Obverse Image'], df['Reverse Image'], df['Additional Image #1'], df['Additional Image #2']]

#create a dir if doesn't exist
folder = 'photos-021218'
if not os.path.exists(folder):
    os.makedirs(folder)

for i, id in enumerate(ids):
    #check if id blank
    if math.isnan(id):
        break
    for j, urlnum in enumerate(urls):
        url = str(urlnum[i])
        #check if url blank
        if url == "nan":
            break
        
        #get img from url
        filename = str(int(id)) + letters[j]
        img = Image.open(requests.get(url, stream=True).raw)

        #resize img to have height of 1000 pixels
        baseheight = 1000
        hpercent = (baseheight / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)

        #save img as id(A,B,...Z).jpg
        img.save(folder+'/'+filename+'.jpg')
