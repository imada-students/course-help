"""asg2-graphs

The goal of this lab is to let you implement some of the ideas which
are necessary for using graphs in algorithmics and modelling. Such
implementations essentially lie at the very core of the endless
application scenarios. We intentionally will give most of the points for
the easier functions to be implemented. For those who like the
challenge are however also some more complicated tasks. 

If not mentioned otherwise, all adjacency matrices in this assignment
are for unweighted graphs i.e., all elements in the adjacency matrices
integers are 0 or 1. Furthermore, the graphs are undirected, i.e.,
A[i,j] == A[j,i], and furthermore the graphs do not have loops
i.e., A[i,i] == 0.

The functions /docstring/s again contain some examples and usage of the
functions. You can run these examples by executing the script from
command line:

python3 asg2.py

Note that the unit tests for the final grading may contain different tests,
and that certain requirements given below are not tested in the testing
period before the final testing. Also the pointing scheme might change. 
Furthermore, the tests might be changed or additional test might be 
introduced during the testing period before the final deadline, to give 
you additional/different feedback.

"""

import numpy as np
from math import inf

def isPermutationMatrix(matrix):
    """
    Returns true if matrix is a square permutation matrix.
    matrix is expected to be an instance of np.ndarray 

    Parameters
    ----------
    matrix
        (n,n) np.ndarray : A permutation matrix of integers. Note that numpy uses np.array,
                           which formally is a function that creates an ndarray.
                           Still, the convention is to use np.array when creating
                           arrays (see example below).
    
    Returns
    -------
    bool
        Returns True if A is a permutation matrix.
        Returns False if A is a matrix, but A is not a permutation matrix.

    Raises
    ------
    TypeError
        if A is not a two-dimensional squared np.ndarray 
    ValueError
        if at least one of the entries in A is not integer 0 or 1

    Examples
    --------
    
    >>> A = np.array([[0,1,0],[1,0,0],[0,0,1]])
    >>> isPermutationMatrix(A)
    True
    """
    if type(matrix) != np.ndarray or matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise TypeError("Matrix is not two-dimensional sqare numpy.ndarray") 
    inColumn = [False] * matrix.shape[1]        #Create list to remember if a one is found in a column
    for r in range(0, matrix.shape[0]):
        foundr = False                              #Variable to remember if a one was already found in this row
        for c in range(0, matrix.shape[1]):
            if matrix[r,c] == 0:
                continue
            elif matrix[r,c] == 1:
                if foundr or inColumn[c]:
                    return False                    #Not a permutation matrix because two ones was in same row or column
                foundr = True
                inColumn[c] = True
            else:
                raise ValueError("An entry was not a 0 or a 1. Input is not valid permutation matrix")
        if not foundr:
            return False                            #Not a permutation matrix because a row had no ones.
    if not all(inColumn):
        return False                                #Not a permutation matrix becase at least one row had no ones
    return True                                     #Input is permutation matrix
        
def allPermutationMatrices(n):
    """
    Returns a list of all permutation matrices of size n x n. 

    Parameters
    ----------
    n : The size of the resulting permutation matrices should be n x n

    Returns
    -------
    list: A list of all possible permutation matrices of size n x n. 
          Each entry should be an 2-dimesnional np.ndarray of ints

    Raises
    -------
    ValueError: if n<=0 

    Examples
    --------
    >>> allPermutationMatrices(2)
    [array([[1, 0],
           [0, 1]]), array([[0, 1],
           [1, 0]])]
    """
    if n <= 0:
        raise ValueError("Cannot generate permutation matrix of dimensions < 1")
    
    #Nested list comprehension that for each instance 0<=i<n^n generates a new matrix of 0 with one 1 on each row.
    #The instance/index number is a "seed" that calculates the position of the one in each row, such that only one 1
    #changes position pr instance, and in a way that creates a new combination of rows with a single 1.
    #Afterwards, all matrices with more than one 1 in each column is filtered out.
    #It seems like list comprehension only really works on simple things, which is why the filtering is done last. 
    
    return [matrix for matrix in                                        #Return each matrix that is a valid permutation matrix
        [np.array(
            [[1 if c==((n-1)-i%(r*n)//r) else 0 for c in range(0,n)]    #For each position in a row, calculate index of the row 1 from row and "seed" (i). (n-1)- because the matrices are otherwise generated in reverse order of the test
            for r in range(1,n+1)])                                     #For each row
        for i in range(0,n**n)]                                         #Generates an "seed" that is used to calculate possible indexes of ones
    if isPermutationMatrix(matrix)]

def isIsomorphicUsingP(A, B, P):
    """
    Returns True if the adjacency matrix B can be changed into the adjaceny matrix A
    by the formula presented in the lecture ( A = P*((P*B)^T ) in mathematical terms,
    where "*" is the matrix-matrix multiplication operator, and "^T" refers to the
    transpose.

    Parameters:
    -----------
    A, B : np.ndarray , two adjacency matrices
    P    : np.ndarray , a permutation matrix

    Returns:
    --------
    bool : see above

    Raises
    -------
    ValueError: if the dimensions of A, B, and P are not identical
    TypeError: if P is not a permutation matrix 


    Examples:
    ---------
    >>> A = np.array([[0, 1, 1], [1, 0, 0], [1, 0, 0]])
    >>> B = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    >>> P = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    >>> isIsomorphicUsingP(A, B, P)
    True
    
    """
    if not isPermutationMatrix(P):
        raise TypeError("P is not a permutation matrix")
    if A.shape != B.shape or A.shape != P.shape:
        raise ValueError("Matrices A, B, and P are of different dimensions")
    return np.all(A == P @ ((P @ B).T))        #When comparing numby arrays, it returns a boolean aray of which values are identical

def numIsomorphisms(A, B):
    """
    Returns the number of permutation matrices P, for which A = P*((P*B)^T holds,
    i.e., mathematically speaking, the number of different isomorphisms between
    A and B.

    Parameters:
    -----------
    A, B : np.ndarray , two adjacency matrices

    Returns:
    --------
    int : see above
    
    Examples:
    ---------
    >>> A = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    >>> B = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    >>> numIsomorphisms(A, B)
    6
    >>> A = np.array([[0, 1, 1], [1, 0, 0], [1, 1, 0]])
    >>> B = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    >>> numIsomorphisms(A, B)
    0
    """
    counter = 0
    for permutation in allPermutationMatrices(A.shape[0]):  #Iterate through valud permutation matrices
        if isIsomorphicUsingP(A,B,permutation):             #Check if permutation makes the matrices identical.
            counter = counter + 1
    return counter

def moreThanOneSubgraph(A, B):
    """
    NOTE: This methods requires more implementation work and probably a
    careful reading of literature - specifically if you aim to make an
    implementation for graphs A and B having, lets say, more than 20
    vertices. We will only give very few out of the possible 100 points for
    this task, so please think twice before you start. If you like the challenge: go!
    If time allows we will do a comparision and give bonus points to the best solution(s).
    Of course, this assumes that the "best" solution(s) will not "cheat" by using
    existing methods from imported modules. The best solution(s) will be the one(s)
    that can solve the largest of the test instances within 10 seconds and without
    using any imported modules other than numpy. For the testing, the host graph (B) 
    will have approx. twice as many nodes as the subgraph (A).

    What you probably learn by trying is: usually it _is_ indeed a very
    good idea to use an existing implementation if it is efficient and correct.

    Time Limit:
    -----------
    10 seconds 
    
    Returns:
    --------
    True: if A can be found at least twice as a subgraph of B. (Note, A does
    not necessarily need to be an induced subgraph of B. See the lecture
    slides if you are unsure what that means.) See slide 16 on the slideset
    "ullmann.pdf": if you find 2 or more different leaf nodes in the depicted
    search tree for which the property on slide 6 holds, then this method
    return "True".

    Parameters:
    -----------
    A, B : np.ndarray , two adjacency matrices, where the adjacency matrix of
           A represents a graph which has the same number or fewer vertices
           as the graph represented by B. 

    Returns:
    --------
    True or False : see description above
    
    Examples:
    ---------
    >>> A = np.array([[0, 1, 1], [1, 0, 0], [1, 0, 0]])
    >>> B = np.array([[0, 1], [1, 0]])
    >>> moreThanOneSubgraph(A, B)
    True
    """

    pass



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    

