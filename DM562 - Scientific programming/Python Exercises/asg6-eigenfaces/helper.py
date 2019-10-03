# Import necessary packages
from __future__ import print_function
import os
import sys
import cv2
import random
import time
import math
import numpy as np
from asg6 import *

# Create data matrix from a list of images. Please note, we keep 3
# channels (i.e., 3 values per pixel) to be able to handle color
# pictures, too. Note, that the dataset you will be working with
# consists of greyscale-pictures only, where the three values
# are all identical.
# 
def createDataMatrix(images):
        print("Creating data matrix",end=" ... ")
        ''' 
        Allocate space for all images in one data matrix.
        The size of the data matrix is
        
        ( w  * h  * 3, numImages )
        
        where,
        
        w = width of an image in the dataset.
        h = height of an image in the dataset.
        3 is for the 3 color channels.
        '''
  
        numImages = len(images)
        sz = images[0].shape
        data = np.zeros((numImages, sz[0] * sz[1] * sz[2]), dtype=np.float32)
        for i in range(0, numImages):
                image = images[i].flatten()
                data[i,:] = image
        
        print("DONE")
        return data

# Read images from the directory
def readImages(path):
        print("Reading images from " + path, end="...")
        # Create array of array of images.
        images = []
        # List all files in the directory and read points from text files one by one
        imlist = []
        imlist = sorted(os.listdir(path))
        for filePath in imlist:
                fileExt = os.path.splitext(filePath)[1]
                if fileExt in [".jpg", ".jpeg"]:
                        
                        # Add to array of images
                        imagePath = os.path.join(path, filePath)
                        im = cv2.imread(imagePath)
                        
                        if im is None :
                                print("image:{} not read properly".format(imagePath))
                        else :
                                # Convert image to floating point
                                im = np.float32(im)/255.0
                                # Add image to list
                                images.append(im)
                                # Flip image 
                                #imFlip = cv2.flip(im, 1);
                                # Append flipped image
                                #images.append(imFlip)
                                
        numImages = len(images) 
        # Exit if no image found
        if numImages == 0 :
                print("No images found")
                sys.exit(0)
                
        print(str(numImages) + " files read.")
        return images

