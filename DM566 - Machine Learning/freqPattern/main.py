import numpy as np
import math as math
import euclideanDist as euc
import histogram as hist

colorsQ = ["yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","red","blue", "blue","blue", "blue","blue", "blue","blue"]
colorsA = ["red", "blue", "blue","blue", "blue","yellow","yellow","yellow","yellow"]
colorsB = ["red","red","red","red","red","red","red","red","yellow","blue", "blue","blue", "blue","blue", "blue","blue"]
colorsC = ["blue", "blue","blue", "blue","blue", "blue","blue", "blue","blue", "blue","yellow","yellow","yellow","yellow","red","red"]
colorsD = ["yellow","yellow","red","blue","blue", "blue", "blue","blue", "blue", "blue","blue","blue","blue","blue","blue","blue"]


"""The first number is for red color, the second is yellow and last is blue in these vectors.
   If yor want to make your own, make the numbers in the correct order. 
"""
qVector = euc.countColors(colorsQ)
aVector = euc.countColors(colorsA)
bVector = euc.countColors(colorsB)
cVector = euc.countColors(colorsC)
dVector = euc.countColors(colorsD)

#Make a list of vectors, that you would like to measure the distance, to a certian vector. 
listVectors = [aVector,bVector,cVector,dVector]


#Generate solutions for 4-2 b Result is a list, from a's distance to q, to d distance to q.
print(euc.distAllVec(qVector,listVectors))


# Generate solutions for 4-2 a
hist.makeHist(colorsC)
