import generateCandidate as gc

data = [("B", "E", "G", "H"),
 ("A","B", "C", "E", "G", "H"),
 ("A", "B", "C", "E", "F", "H"),
 ("B", "C", "D", "E", "F", "G", "H", "L"),
 ("A", "B", "E", "K", "H"),
 ("B", "E", "F" ,"G" ,"H" ,"I" ,"K"),
 ("A", "B", "D", "G", "H"),
 ("A", "B", "D", "G"),
 ("B", "D", "F", "G"),
 ("C", "E", "F"),
 ("A", "C", "E", "F", "H"),
 ("A", "B", "E", "G")]


def generateC1(data):
    s1 = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            s1.add(data[i][j])
    s1 = list(s1)
    return s1




def Apriori(I,D,sigma):
    sK = generateC1(D)
    k = 2
    #Generate the data as Strings, so i can compare them with candidates later.
    dataAsStrings = []
    for i in range (len(D)):
        dataAsStrings.append("".join(D[i]))
        #Genere alle mulige sammensætninger af din transaktion som string, af størrelse n

    
    while(sk != []):
        cK = gc.generateItemsetK(sK)



        





test = (("A","B","E"),("A","B","G"),("A","B","H"),("A","E","H"),("B","D","G"),("B","E","G"),("B","E","H"),("B","G","H"),("C","E","F"),("C","E","H"),("E","F","H"),("E","G","H"))
test2 = (("A","B"),( "C","E"), ("A","E"), ("C","F"),("A","G"), ("C","H"),("A","H"), ("D","G"),("B","D"), ("E","F"),("B","E"), ("E","G"),("B","F"), ("E","H"), ("B","G"), ("F","H"), ("B","H"), ("G","H"))

print ("S",len(test[0]) + 1, "inden vi tæller, om den overholder threshold =",gc.generateItemsetK(test))
print ("Nu mangler du at tælle, om de overholder threshold")
