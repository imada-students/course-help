import math 
import numpy as np
import random
import sys

#Helper Methods ------------------------------------------------------------------------
# Finds the mean/centroid of a cluster.
def centerOfCluster(cluster):
    cluster = np.asarray(cluster)
    center =np.array([0,0])

    result = np.array([0,0])
    for i in range(len(cluster)):
        result = np.sum([cluster[i], result], axis = 0)

    numberOfPoints = len(cluster)
    if numberOfPoints > 0:
        result = result * (1 / numberOfPoints)
        return result
    else: 
        print ("A cluster is empty")
        sys.exit()


# Calculates the distance between 2 2d vectors. 
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


# Calculates the sum of distance for all points in a clusters to its center.
def distClustSum(cluster):
    cluster = np.asarray(cluster)
    center = centerOfCluster(cluster)

    dist = 0
    for i in range(len(cluster)):
        temp = pow(distVector(center,cluster[i]),2)
        dist = temp + dist
    return dist

#End helper methods
#---------------------------------------------------------------------------------------

#Calculates the TD2 measure for
def TD2(data):
    result = 0
    data = np.asarray(data)


    for i in range(len(data)):
        result = distClustSum(data[i]) + result
    return result

# Is this forgy / Lloyd or not?
def kMeans(data):
    points = [item for sublist in data for item in sublist]
    k = len(data)
    clusters=[[]for i in range(k)]
    
    centroids = []
    for i in range(len(data)):
        centroids.append(centerOfCluster(data[i]))

    for x in points:
        lengths = []

        for i in centroids:
            lengths.append(distVector(x,i))
        # Find the centroid that are clossest to the point
        minimum = min(lengths)

        # Assign that point to the cluster, that centroid belongs too. 
        cluster =lengths.index(minimum)
   
        for j in range(k):
             if cluster==j:
                clusters[j].append(x)
    
    return clusters

#kMeansAlgo tager imod data og et k
#data: En liste af lister af 2d punkter.
#k: En liste af antal cluster vi gerne vil prøve at finde. 
def kMeansAlgo(data,k):
    # points takes the list from data, anc uses list comprehension on it. 
    points = [item for sublist in data for item in sublist]
  
    TD=[] # TD2squared soloutions for clusters
    for i in k:
        # lav k antal tomme clusters
        clusters=[[]for j in range(i)]
        for x in points:
            # tildel alle punkterne i vores data, tilfædigt i de k antal lister. 
            random.choice(clusters).append(x)
        # As long as there are changes for kMeans update, otherwise calcule TD2 and end.
        while kMeans(clusters)!=clusters:
            clusters= kMeans(clusters)
        
        temptTD = TD2(clusters)
        #TD.append(TD2(clusters))
        print("Clusters with k =", i,"is:", clusters, "and TD2 =", temptTD)
        TD.append(temptTD)
    #return TD # Har jeg udkommenteret fordi jeg ikke bruger den. Det er bare en liste af TD2 for 
    # de forskellige clusters. 


squares = [[1],[2]]
triangle = [[4],[6]]
circle = [[8],[9],[10]]

data = [squares,triangle,circle] 

#Her kører vi med værdierne som de er i grafen
print ("k-means with initialie values set = ",kMeans(data), "TD2 = ", TD2(kMeans(data)))

kMeansAlgo(data, [1,2,3])