from PIL import Image
import os


dir = 'assets'
for folder in os.listdir(dir):
    path = dir+'/'+folder
    for file in os.listdir(path):
        image = Image.open(path+'/'+file)
        new = image.resize((100, 100))
        new.save(path+'/'+file)
    print(folder)
