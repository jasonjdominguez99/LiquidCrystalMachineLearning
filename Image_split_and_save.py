# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:29:02 2020

@author: Jason
"""

import numpy as np
import os
from PIL import Image
from pathlib import Path

def image_split_and_save(image_directory, target_image_directory, target_size=(200,200)):
    """
    Given a directory of images, this function takes each image and splits it into
    as many non-overlapping images of target_size shape as will fit. It then 
    saves each new, split image into the target_image_directory.
    New saved image has a name of the format "name-00001" for the first
    image split from image called name

    Parameters
    ----------
    image_directory : string
        Directory destination containing all the images that are required to be
        split.
    target_image_directory : string
        Directory destination where the split images will be saved.
    target_size : tuple, optional
        The dimensions that you require the original image to be split into.
        The default is (200,200).

    Returns
    -------
    None.

    """
    directory = Path(image_directory)
    target_height, target_width = target_size
    
    n_image = 1
    for file in directory.iterdir():
        image = Image.open(file)
        image_array = np.asarray(image)
        fname, ext = os.path.splitext(file)
        fname = fname.replace(image_directory, "")
        
        height = image_array.shape[0]
        width = image_array.shape[1]
        n_h = height // target_height
        n_w = width // target_width
        
        split_image_number = 1
        for h in range(n_h):
            start_height = target_height * h
            for w in range(n_w):
                start_width = target_width * w
                split_image_array = image_array[start_height:start_height + target_height, start_width:start_width + target_width, :]
                split_image = Image.fromarray(split_image_array)
                save_path = target_image_directory + fname + "-%05d"%(split_image_number) + ext
                split_image.save(save_path)
                split_image_number += 1       
        print("Image %d has been split.\n" %(n_image))
        n_image += 1
    
    return None

"""
image_directory = "C:\\Users\\Jason\\Documents\\University\\Year_4\\MPhys_Project(s)\\Liquid_crystals-machine_learning\\Unsplit_image_dir\\"
target_image_directory = "C:\\Users\\Jason\\Documents\\University\\Year_4\\MPhys_Project(s)\\Liquid_crystals-machine_learning\\Split_image_dir\\"
image_split_and_save(image_directory, target_image_directory)
"""