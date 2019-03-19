import os
import csv

#specify folder
folder = 'fine-art-images'

#create empty dict
skus = {"sku":"ext"}

#fill dict with sku:ext key:value pairs
for filename in os.listdir(folder):
    skus[str(filename.partition("-")[0])] = str(filename.partition(".")[2])

#write dict to a csv file
with open('fine-art-skus.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in skus.items():
        writer.writerow([key, value])
        
