import os
import numpy as np
import pandas as pd
import skimage
import cv2
import tensorflow as tf
import PIL
import xml.etree.ElementTree as ET

# Parsing and extracting from Kaggle dataset
root_directory = '/Users/micahkepe/Downloads/archive'
data = {}

for folder_name in os.listdir(root_directory):
    folder_path = os.path.join(root_directory, folder_name)
    if os.path.isdir(folder_path):
        folder_data = []
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if file_name.endswith('.inkml'):
                tree = ET.parse(file_path)
                root = tree.getroot()
                traces = []
                
