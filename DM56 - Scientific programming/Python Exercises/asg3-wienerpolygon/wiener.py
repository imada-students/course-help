"""wiener.py

Lab 3: Wiener Index / Polygons
------------------------------

This lab has two independent parts, you need to provide you solutions
via implementations in wiener.py (this file) and polygon.py.

Hint: Start with the implementations for polygon.py, to ensure you get
most of the points with a small amount of work.

Number of point to be achieved in polygon.py : 92 
Number of point to be achieved in wiener.py  :  8

wienerIndex(W):         2
distanceMatrix(W):      2
lengthThreePaths(W):    2
boilingPoint(W):        2 

In this part of the lab you need to implement the methods in order to
predict boiling points of chemical compounds, where the chemical
compounds are, for simplicity, encoded as adjacency matrices of
graphs. See the lecture slides for all the details.

The functions /docstring/s again contain some real examples and usage
of the functions. You can run these examples by executing the script
from command line:

python3 wiener.py

Note that the unit tests for the final grading may contain different
tests, and that certain requirements given below are not tested in the
tesing before the final testing.

"""

import numpy as np
from math import inf


def wienerIndex(W):
    """
    Returns the Wiener Index (i.e, the sum of all pairwise shortest paths in a
    graph represented by an edge weight matrix W). Note, that we assume all
    weights to be floats.

    Parameters:
    -----------
    W : np.ndarray , the edge weight matrix representation of a graph (floats)

    Returns:
    --------
    float : the Wiener Index as presented on the lecture slides

    Examples:
    ---------
    >>> A = np.array([[0.0, inf, 1.0, inf, inf, inf], \
                      [inf, 0.0, 1.0, inf, inf, inf], \
                      [1.0, 1.0, 0.0, 1.0, 1.0, inf], \
                      [inf, inf, 1.0, 0.0, inf, 1.0], \
                      [inf, inf, 1.0, inf, 0.0, inf], \
                      [inf, inf, inf, 1.0, inf, 0.0]])
    >>> wienerIndex(A)
    28.0
    
    """
    
    pass

def distanceMatrix(W):
    """
    Given an edge weight matrix W, this returns the distance matrix D (as presented
    on the lecture slides)

    Parameters:
    -----------
    W : np.ndarray , the edge weight matrix representation of a graph (floats)

    Returns:
    --------
    D : np.ndarray , the distance matrix of a chemical graph

    Examples:
    ---------
    >>> W = np.array([[0.0, inf, 1.0, inf, inf, inf], \
                      [inf, 0.0, 1.0, inf, inf, inf], \
                      [1.0, 1.0, 0.0, 1.0, 1.0, inf], \
                      [inf, inf, 1.0, 0.0, inf, 1.0], \
                      [inf, inf, 1.0, inf, 0.0, inf], \
                      [inf, inf, inf, 1.0, inf, 0.0]])
    >>> distanceMatrix(W)
    array([[ 0.,  2.,  1.,  2.,  2.,  3.],
           [ 2.,  0.,  1.,  2.,  2.,  3.],
           [ 1.,  1.,  0.,  1.,  1.,  2.],
           [ 2.,  2.,  1.,  0.,  2.,  1.],
           [ 2.,  2.,  1.,  2.,  0.,  3.],
           [ 3.,  3.,  2.,  1.,  3.,  0.]])
    """
    pass
    
def lengthThreePaths(W):
    """
    Returns the number of all shortest paths of length 3.0 where the index of the
    starting vertex i is smaller than the index of the goal vertex j (called p on
    the lecture slides)

    Parameters:
    -----------
    W : np.ndarray , the edge weight matrix representation of a graph (floats)

    Returns:
    --------
    int : the number of all shortest paths of length 3

    Examples:
    ---------
    >>> W = np.array([[0.0, inf, 1.0, inf, inf, inf], \
                      [inf, 0.0, 1.0, inf, inf, inf], \
                      [1.0, 1.0, 0.0, 1.0, 1.0, inf], \
                      [inf, inf, 1.0, 0.0, inf, 1.0], \
                      [inf, inf, 1.0, inf, 0.0, inf], \
                      [inf, inf, inf, 1.0, inf, 0.0]])
    >>> lengthThreePaths(W)
    3
    """
    pass
    
def boilingPoint(W):
    """
    Returns the boiling point prediction as introduced on the lecture slides.

    Parameters:
    -----------
    W : np.ndarray , the edge weight matrix representation of a graph (floats)

    Returns:
    --------
    float : the predicted boiling point of the molecule

    Raises:
    -------
    TypeError: if A is not a two-dimensional squared and symmetric edge weight 
               matrix with A[i,i] == 0 for all possible i  

    Examples:
    ---------
    >>> W = np.array([[0.0, inf, 1.0, inf, inf, inf], \
                      [inf, 0.0, 1.0, inf, inf, inf], \
                      [1.0, 1.0, 0.0, 1.0, 1.0, inf], \
                      [inf, inf, 1.0, 0.0, inf, 1.0], \
                      [inf, inf, 1.0, inf, 0.0, inf], \
                      [inf, inf, inf, 1.0, inf, 0.0]])
    >>> round(boilingPoint(W),3)
    49.664
    """

    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    

