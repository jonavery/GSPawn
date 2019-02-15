import requests
import pandas as pd
import os
import math

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
        print(url)
        print(type(url))
        
        #save img as id(A,B,...Z).jpg
        filename = str(int(id)) + letters[j] + ".jpg"
        print (filename)
        r = requests.get(url, allow_redirects=True)
        open(folder+'/'+filename, 'wb').write(r.content)
