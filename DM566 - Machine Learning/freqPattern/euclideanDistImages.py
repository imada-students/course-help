import numpy as np
import math as math


# Eucludian distance for images P and Q:
# dist(P,Q) = sqrt(hp-hq) * (hp -hq)**t 
# hp og hq er vectorer, over vores farver. 


# Counts the number of deffirent colors, yellow, blue and red and returns a list.
# The first number is for red color, the second is yellow and last is blue.
def countColors(data):
    redCount = 0
    yellowCount = 0
    blueCount = 0
    for i in range(len(data)):
        if (data[i] == 'yellow'):
            yellowCount = yellowCount + 1        
        if (data[i] == 'red'):
            redCount = redCount + 1
        if (data[i] == 'blue'):
            blueCount = blueCount + 1
        

    
    vector = [redCount,yellowCount,blueCount]
    return vector


"""Gets the distance between two color vectors in euclidean distance, from the formula from 
   slide 129. P og Q er normalt selve billedet. Her laver jeg det bare til at være vekotorer.

"""
def distHist(hp,hq):
    
    # Change the list to np arrays, so i can make vector calculations on them.
    hp = np.array(hp)
    hq = np.array(hq)

    #Calculate each temp vector before i use multiplication.
    tempVec1 = (hp - hq)
    tempVec2 = tempVec1
    tempVec2 = tempVec2.reshape(-1,1)
    
    #Use multiplication on the temp vectors, and take the squareroot of that.
    result = tempVec1.dot(tempVec2)
    result = float(result[0])
    result = math.sqrt(result)
    
    return result 



"""Calculates all the distances from one color vector, to all other colorvectors in a list.""" 
def distAllVec(qvec,listVectors):
    resultList = []
    for i in range (len(listVectors)):
        result = distHist(qvec, listVectors[i])
        resultList.append(result)

    return resultList

