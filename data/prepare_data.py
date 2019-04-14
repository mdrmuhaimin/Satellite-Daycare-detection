import pandas as pd
import ast
import os
import cv2
from os import getcwd
import numpy as np

# File with object annotations
da = pd.read_csv('DaycaresAnnotations_original.csv')[['filename', 'region_shape_attributes']].drop_duplicates().reset_index()

# Filepaths to folders
filepath_to_daycares = 'Daycares/'
filepath_to_zca_daycares = 'zca/'
filepath_to_nondaycares = 'NonDaycares/'
filepath_to_labels = 'labels/'

# Name of file that will have annotations
save_to_file = 'annotate.txt'
image_path_file = 'all.txt'
cwd = getcwd()

# Name of file that will have annotations
save_to_file = 'annotate.txt'
image_path_file = 'all.txt'


# Annotated output
output_annot = []
image_paths = []

zca_files = [x for x in filter(lambda x: x.endswith('jpg'), os.listdir(filepath_to_zca_daycares))]
print('Total of ZCA files - ', len(zca_files))
zca_to_org_map = [(file, file.replace('_ZCA', '')) for file in zca_files]
zca_org_df = pd.DataFrame(np.array(zca_to_org_map), columns=['zca', 'filename'])
zca_annot_map = pd.merge(zca_org_df, da, on='filename', how='inner').drop_duplicates()
# zca_annot_map[zca_annot_map.filename.isin(zca_annot_map[zca_annot_map.duplicated(['filename'])]['filename'].values)]
assert len(zca_annot_map) == len(zca_files)
# zca_annot_map.head(5)

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
            rel_x = (rect['x'] + (rect['width'] / 2) )/ width
            rel_y = (rect['y'] + (rect['width'] / 2) )/ height
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

# Annotated output
output_annot = []
image_paths = []
###########################################################################
# ZCA _ DAYCARES
for r in range(len(zca_annot_map)):
    # Check if it has an object
    if zca_annot_map.loc[r, 'region_shape_attributes'] != "{}":
        # filename
        filepath = filepath_to_zca_daycares + zca_annot_map.loc[r, 'zca']
        imagepath = cwd +'/'+ filepath
        filepath_label = filepath_to_zca_daycares + zca_annot_map.loc[r, 'zca'] # both jpg and text need to be in same dir
#         filepath_label = filepath_to_labels + da.loc[r, 'filename']
        filepath_label = filepath_label.replace('.jpg', '.txt')
        img = cv2.imread(filepath)
        if not (img is None):
            # Get rect attributes
            rect = ast.literal_eval(zca_annot_map.loc[r, 'region_shape_attributes'])

            height, width, channels = img.shape
            rel_x = (rect['x'] + (rect['width'] / 2) )/ width
            rel_y = (rect['y'] + (rect['width'] / 2) )/ height
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