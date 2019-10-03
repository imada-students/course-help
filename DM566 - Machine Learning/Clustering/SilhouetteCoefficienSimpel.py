import math 
import numpy as np
#Denne implementation kan kun udregne simple Silhouette Coefficien for vectoer i 2d, 
# og for 2 clusters


circle = [ [7,7],
           [7,8],
           [6,8],
           [7,9],
]


triangle = [
     [3,4],[2,3],[1,5],[10,1]]


def centerOfCluster(cluster):
    cluster = np.asarray(cluster)
    center =np.array([0,0])

    result = np.array([0,0])
    for i in range(len(cluster)):
        result = np.sum([cluster[i], result], axis = 0)

    numberOfPoints = len(cluster)
    result = result * (1 / numberOfPoints)

    return result



def distVector(vectorA, vectorB):
    vectorA = np.asarray(vectorA)
    vectorB = np.asarray(vectorB)

    tem1 = np.subtract(vectorA[0], vectorB[0])
    tem2 = np.subtract(vectorA[1], vectorB[1])
    tem1 = np.power(tem1,2)
    tem2 = np.power(tem2,2)
    
    result = np.add(tem1,tem2)
    result = math.sqrt(result)
   
    return result


 # let a(o) be the distance between o and its “own” cluster representative
 # let b(o) be the distance between o and the closest “foreign” cluster representative
def aobo(cluster, center):
    center = np.asarray(center)
    cluster = np.asarray(cluster)
    aboList = []
    #Udregn afstand fra centrum af et cluster, til alle andre punkter til et cluster
    #Det er forskelligt fra ao til bo se slide 184.
    for i in range (len(cluster)):
        aboList.append(distVector(cluster[i], center))

    return aboList  

#Se slide 182.
def silhouetteList(ao, bo):
    silhouetteList = []
    for i in range(len(ao)):
        sub = np.subtract(bo[i],ao[i])
        if(ao[i] < bo[i]):
            max = bo[i]
            res = sub / max
            silhouetteList.append(res)
        else:
            max = ao[i]
            res = sub / max
            silhouetteList.append(res)

    silhouetteList = np.array(silhouetteList)
    return silhouetteList


 
def SimSilCoe(cluster1, cluster2):
    center1 = centerOfCluster(cluster1)
    center2 = centerOfCluster(cluster2)

    totalNumPoints = len(cluster1) + len(cluster2)

    center1 = center1.tolist()
    center2 = center2.tolist()
    # Se def på ao og bo på slide 184
    ao1 = aobo(cluster1,center1)
    bo1 = aobo(cluster1,center2)
    ao2 = aobo(cluster2,center2)
    bo2 = aobo(cluster2,center1)

    so1 = silhouetteList(ao1,bo1)
    so2 = silhouetteList(ao2,bo2)

    temp1 = np.sum(so1) / totalNumPoints
    temp2 = np.sum(so2) / totalNumPoints
    result = temp1 + temp2

    return result  



print (SimSilCoe(circle,triangle))
