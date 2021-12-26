# -*- coding: utf-8 -*-
"""
Created on 06/10/2019

@author: Dr Michael GUEDJ

Program: thumbnailsMaker.py
Description:
	- Find the thumbnails previously created
	- Delete the thumbnails previously created
	- Create thumbnails from the .jpg and .jpeg file in the current folder
"""
import os
import re
from PIL import Image

def filename(file):
    filename, file_extension = os.path.splitext(file)
    return filename

def extension(file):
    filename, file_extension = os.path.splitext(file)
    return file_extension

reduced_size = (500, 500)

# Find the thumbnails previously created
to_delete = []
for file in os.listdir("."):
    if file.endswith("_thumbnail.jpg") \
       or file.endswith("_thumbnail.jpeg") \
       or file.endswith("_thumbnail.JPG") \
       or file.endswith("_thumbnail.JPEG"):
        to_delete.append(file)
# Delete the thumbnails previously created
for thumbnail_file in to_delete:
    print(thumbnail_file, "deleted\t", end="")
    os.remove(thumbnail_file)
    print("[OK]")

# Create thumbnails from the .jpg and .jpeg file in the current folder 
for file in os.listdir("."):
    if extension(file).lower() in [".jpg", ".jpeg"]:
    	img = Image.open(file)
    	img.thumbnail(reduced_size)
    	output = filename(file) + "_thumbnail" + extension(file)
    	print(output, "\t", end="")
    	img.save(output, "JPEG", optimize=True)
    	print("[OK]")

input("\n--> End with success.")
