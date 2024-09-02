#!/usr/bin/env python3

import os
from PIL import Image

# Define file paths to grab and save images
path_to_files = '/home/student/supplier-data/images/'
path_to_save = '/home/student/supplier-data/images/'

# Iterate over files on given folders
for filename in os.listdir(path_to_files):
    # Filter only files with .tiff extension
    if filename.endswith('.tiff'):
        # Open and use convert("RGB") method for converting RGBA to RGB image
        im = Image.open(path_to_files + filename).convert('RGB')
        # Resize and save result in .jpeg format
        im.resize((600,400)).save(path_to_save + os.path.splitext(filename)[0] + '.jpeg', 'jpeg')
        # Create variable to list all saved images
        saved_images = [f for f in os.listdir(path_to_save) if f.endswith('.jpeg')]
# Print saved images to user
print(saved_images)
