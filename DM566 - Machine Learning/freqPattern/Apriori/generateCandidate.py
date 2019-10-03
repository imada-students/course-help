
# Takes a solution of size n, and returns the candidates of size N + 1.
def join(solutionN):
    k = len(solutionN[0]) - 1
    candidatesN = set()
    currentItem = []
    currentItemCount = 0
    nextItem = 1

    for i in range(len(solutionN)):
        for j in range(nextItem, len(solutionN) ):

            # Checking if the first k -2 are identical. If they are, make the new larger
            # item, and add it to the list of solutions
            if(solutionN[currentItemCount][:k] == solutionN[j][:k]):
                string = "".join(solutionN[j][:k])

                newitem = string + solutionN[currentItemCount][-1] + solutionN[j][-1]
                candidatesN.add(newitem)
        
        nextItem = nextItem + 1
        currentItemCount = currentItemCount + 1
    print ("Result of join for", solutionN ,"= \n", candidatesN, "")
    return candidatesN


# Remove all k-itemsets from solution solution off size N, that are not a member of
# the Candidate of size N - 1 that they were derevied from.
def prunning(solutionN, candidatesN):
    solutionN = tuple(solutionN)
    prunningSolution = []

    for i in range(len(solutionN)):
        kItemSet = removeItemset(solutionN[i])
        # If all k-itemSets are a part of the orignal solution, add that solutin to the
        # lists off solutions. Else go check the next solution. 
        if (all(elem in candidatesN for elem in kItemSet )):
            

            prunningSolution.append(solutionN[i])
    print ("\nOprindelig data = ", candidatesN,"\nResult for prunning", solutionN , "= ", prunningSolution, "\n")
    return prunningSolution  

# Helper method for prunning. It creates Strings we need for comparisons. 
def removeItemset(solutionN):
    solution = []

    # In all cases, we have a candidate, that is the solutionN minus the first letter.
    ignoreFirstItem = solutionN[1:]
    ignoreFirstItem = tuple(ignoreFirstItem)
    solution.append(ignoreFirstItem)
    
    ignoreItem = ""
    k = (len(solutionN)) - 2 # er ikke sikker på at dette er rigtigt.
    #If we have more then cases then the ignoreFirstItem
    if(len(solutionN) > 3):
    # Divide each itemset into two parts, and set them together. 
        indent = 1
        for j in range(k-1):
            ignoreItem = solutionN[:indent] + solutionN[1+indent:]
            indent = indent + 1
            ignoreItem = tuple(ignoreItem)
            solution.append(ignoreItem)

    return solution


#Put it all together and genereates a set of candidates, from a soultion size n - 1.
# HUSK AT LIGE NU, SÅ TÆLLER DEN IKKE, OM VORES KANDIDATER OVERHOLDER THRESHOLD!
# DET ER ALTSÅ KUN JOIN OG PRUNNING DEN BRUGER HER
def generateItemsetK(solutionN):
    temp = join(solutionN)

    candidate = prunning(temp,solutionN)

    return candidate
    