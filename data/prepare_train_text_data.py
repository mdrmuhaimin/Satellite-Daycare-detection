import pandas as pd
import numpy as np
import ast
import os
import cv2
from os import getcwd

cwd = os.getcwd()
filepath_to_daycares = 'Daycares/'

def add_full_path(filename):
    image_path = cwd +'/'+ filepath_to_daycares + filename
    exists = (os.path.isfile(image_path)) and (os.path.isfile(image_path.replace('.jpg', '.txt')))
    if exists:
        return image_path
    return None

train = pd.read_csv('train.csv', header=None)[0].values
test = pd.read_csv('test.csv', header=None)[0].values

train = [add_full_path(x) for x in train if add_full_path(x) is not None]
test = [add_full_path(x) for x in test if add_full_path(x) is not None]

# Save image paths to FILE
with open('train.txt', 'w') as f:
    for item in train:
        f.write("%s\n" % item)

with open('test.txt', 'w') as f:
    for item in test:
        f.write("%s\n" % item)

