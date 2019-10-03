import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Makes a histogram for a colorvector
def makeHist(colorVector):
    a = plt.hist(colorVector, bins = 3,rwidth = 0.7, histtype = 'bar', facecolor = 'blue')
    #print ("a = ",colorsQ)
    plt.ylabel("Number of cubes in that color")
    plt.xlabel("Colors")
    #plt.title("Colors of d")
    plt.axis([0,2,0,14])
    plt.show()