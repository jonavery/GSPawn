import requests
import pandas as pd
import os
import math
from PIL import Image

#set wd to current dir
#os.chdir(os.path.dirname(__file__))

#open the csv file
df = pd.read_csv('products-2019-03-15.csv')

#grab id's and url's from file
ids = df['Product SKU']
urls = [ df['Product Image File - 1'], df['Product Image File - 2'], df['Product Image File - 3'], df['Product Image File - 4'], df['Product Image File - 5'], df['Product Image File - 6'], df['Product Image File - 7'], df['Product Image File - 8'] ]

#create a dir if doesn't exist
folder = 'fine-art-images'
if not os.path.exists(folder):
    os.makedirs(folder)

for i, id in enumerate(ids):
    #check if id blank
    if id == "":
        break
    for j, urlnum in enumerate(urls):
        urltail = str(urlnum[i])
        url = "https://gspawn.com/product_images/" + urltail
        print(url)
        #check if url blank
        if urltail == "nan":
            break
        
        #get img from url
        try:
            img = Image.open(requests.get(url, stream=True).raw)
        except:
            break

        #save img as id(A,B,...Z).jpg
        filename = str(id) + "-" + str(j+1) + '.' + urltail.rpartition('.')[2]
        print(filename)
        img.save(folder+'/'+filename)
        
