import math 
import numpy as np
#SQQ er det samme som TD2
def TD2(data):
    result = 0
    data = np.asarray(data)
    #print(data )

    for i in range(len(data)):
        #print (data)
        result = distClustSum(data[i]) + result
    return result

def centerOfCluster(cluster):
    cluster = np.asarray(cluster)
    center =np.array([0,0])

    result = np.array([0,0])
    for i in range(len(cluster)):
        result = np.sum([cluster[i], result], axis = 0)

    numberOfPoints = len(cluster)
    result = result * (1 / numberOfPoints)

    return result


# Er dette den rigtige def? 
def distVector(vectorA, vectorB):
    vectorA = np.asarray(vectorA)
    vectorB = np.asarray(vectorB)

    tem1 = np.subtract(vectorA[0], vectorB[0])
    tem2 = np.subtract(vectorA[1], vectorB[1])
    tem1 = np.power(tem1,2)
    tem2 = np.power(tem2,2)
    
    result = np.add(tem1,tem2)
    #result = math.sqrt(result)

    #result = np.power(result,2)
   
    return result



def distClustSum(cluster):
    cluster = np.asarray(cluster)
    center = centerOfCluster(cluster)

    dist = 0
    for i in range(len(cluster)):
        temp = distVector(center,cluster[i])
        dist = temp + dist
    #print (dist)
    return dist

triangle = [[1,5],[2,3],[3,4],[10,1]]
circle = [[6,8],[7,7],[7,8],[7,9]]

data = [triangle,circle] 

print(TD2(data))