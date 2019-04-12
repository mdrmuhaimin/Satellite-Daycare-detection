import pandas as pd
import ast
import os
import cv2
from os import getcwd

# File with object annotations
da = pd.read_csv('DaycaresAnnotations_original.csv')

# Filepaths to folders
filepath_to_daycares = 'Daycares/'
filepath_to_nondaycares = 'NonDaycares/'
filepath_to_labels = 'labels/'

# Name of file that will have annotations
save_to_file = 'annotate.txt'
image_path_file = 'all.txt'


# Annotated output
output_annot = []
image_paths = []
cwd = os.getcwd()

###########################################################################
# DAYCARES
for r in range(len(da)):
    # Check if it has an object
    if da.loc[r, 'region_shape_attributes'] != "{}":
        filepath = filepath_to_daycares + da.loc[r, 'filename']
        imagepath = cwd +'/'+ filepath
        filepath_label = filepath_to_daycares + da.loc[r, 'filename'] # both jpg and text need to be in same dir
        filepath_label = filepath_label.replace('.jpg', '.txt')
        img = cv2.imread(filepath)
        if not (img is None):
            # Get rect attributes
            rect = ast.literal_eval(da.loc[r, 'region_shape_attributes'])

            height, width, channels = img.shape
            rel_x = (rect['x'] + (width / 2))/ width
            rel_y = (rect['y'] + (height / 2))/ height
            rel_width = rect['width'] / width
            rel_height = rect['height'] / height

            # class_name ("0" = Daycare) as we have only 1 class

            current_annot = '{} {} {} {} {}'.format(0, rel_x, rel_y, rel_width, rel_height)
            image_paths.append(imagepath)
            output_annot.append(current_annot)
            # print(filepath_label)
            with open(filepath_label, 'w') as f:
                f.write("%s\n" % current_annot)
    
        else:
            print(filepath, ' not found')


# Save image paths to FILE
with open(image_path_file, 'w') as f:
    for item in image_paths:
        f.write("%s\n" % item)