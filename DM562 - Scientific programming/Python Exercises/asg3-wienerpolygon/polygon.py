"""polygon.py

Lab 3: Wiener Index / Polygons
------------------------------
This lab has two independent parts based on wiener.py and
polygon.py (this file). 

Hint: Start with the implementations for polygon.py, to ensure you get
most of the points with a small amount of work.

Number of point to be achieved in polygon.py : 92
Number of point to be achieved in wiener.py :   8


norm(x):                      15 
mean(x):                      15 
initPoints(num):              20 
matrixM(num):                 20 
invMatrixM(M):                10
updatePoints(M, x, y):        10
pairCS(num):                   1 (more complicated)
convEllipse(x, y):             1 (more complicated)


In this part of the lab assignment you basically have to implement
methods to allow you to visualize the series of polygons as shown and
explained in the lecture "From Random Polygon to Ellipse".  We will
provide an additional file which will use this file via an import.


Do not touch the imports in this file, and specifically, do not import
matplotlib in this file! Use the provided file linalg-ellipse.py for
visualization. The imports listed below should be enough.

The functions /docstring/s again contain some real examples and usage
of the functions. You can run these examples by executing the script
from command line:

python3 polygon.py

Note that the unit tests for the final grading may contain different
tests, and that certain requirements given below are not tested in the
tesing before the final testing.

"""

import numpy as np
import math

def norm(x):
    """
    Returns the L^2 norm of a vector x

    Parameters
    ----------
    x       : np.ndarray : a numpy array of floats

    Returns
    -------
    float   : the L^2 norm of x

    Examples
    --------
    >>> A = np.array([1.0, 2.0, 3.0, 3.0, 1.0, 1.0])
    >>> norm(A)
    5.0
    """
    sum = 0
    for component in x:
        sum = sum + component**2
    return math.sqrt(sum)

def mean(x): 
    """
    Returns the mean of a the values of vector x

    Parameters
    ----------
    x       : np.ndarray : a numpy array of floats

    Returns
    -------
    float   : the mean of all values of vector x

    Examples
    --------
    >>> A = np.array([1.0, 2.0, 3.0, 3.0, 1.0, 1.0])
    >>> mean(A)
    1.8333333333333333
    """
    return np.sum(x) / x.size

def initPoints(num):
    """
    Randomly chose the points of the initial polygon. As described on
    the slides and in the additional material, we chose all the
    points (x_i, y_i), such that for the vector x=(x_1, ..., x_n) as
    well as y=(y_1, ..., y_n) it will hold that mean(x) = 0.0 and
    norm(x) = 1.0 (resp. mean(y) = 0.0 and norm(y) = 1.0 )

    Parameter
    ---------
    int  :  num  : the number of points of the initial polygon

    Returns
    -------
    tuple : (x,y) where x as well as y is a 1-dimensional np.ndarray of floats (length num)

    Raises
    ------
    ValueError    if num<=2

    Examples
    --------
    >>> round(norm(initPoints(5)[0]),2)
    1.0
    >>> abs(round(mean(initPoints(5)[1]),2))
    0.0
    >>> print(type(initPoints(5)))
    <class 'tuple'>
    >>> print(type(initPoints(5)[0]))
    <class 'numpy.ndarray'>
    >>> len(initPoints(5)[0])
    5
    """
    if num <= 2:
        raise ValueError("Cannot create a polygon with less than 3 points")
    x = np.random.random_sample(num)
    y = np.random.random_sample(num)
    x = x - mean(x)
    y = y - mean(y)
    x = x / norm(x)
    y = y / norm(y)
    return (x,y)
    
    

def matrixM(num):
    """ 
    Returns the matrix used for the matrix vector multiplication for one iteration
    as explained on page 11 on the slide set

    Parameter
    ---------
    int  :  num  : the number of points of the initial polygon

    Returns
    -------
    2-dimensional numpy.ndarray of shape (num, num)

    Example
    -------
    matrixM(4)
    array([[ 0.5,  0.5,  0. ,  0. ],
           [ 0. ,  0.5,  0.5,  0. ],
           [ 0. ,  0. ,  0.5,  0.5],
           [ 0.5,  0. ,  0. ,  0.5]])
    """
    out = np.array([[0.5 if x==y or x-1==y else 0 for x in range(0, num)] for y in range(0, num)])
    out[num-1,0] = 0.5
    return out

def invMatrixM(M):
    """ 
    Returns the inverse of matrix M, where M can be assumed to
    be a matrix which results from the method matrixM.

    Parameter
    ---------
    M : 2-dimensional squared numpy.ndarray 

    Returns
    -------
    a 2-dimensional squared numpy.ndarray : the inverse of matrix M

    Raises
    ------
    ValueError : if the number of rows or columns is not odd

    Example
    -------
    >>> invMatrixM(matrixM(3))
    array([[ 1., -1.,  1.],
           [ 1.,  1., -1.],
           [-1.,  1.,  1.]])
    """
    if M.shape[0] % 2 == 0 or M.shape[1] % 2 == 0 or M.ndim > 2:
        raise ValueError("Cannot invert matrix with even number of columns or rows")
    #So, numpy have a special matrix object which can be created directly from array like object,
    #and this matrix object have exponents defined. Including the inverse.
    #The test get angry that it returns a matrix and not an array even though
    #they are functionally equivilant. So, more object creation!
    return np.array(np.matrix(M)**-1)
        
def updatePoints(M, x, y):
    """
    Update the arrays x and y according to slide 15 on the slide set, i.e.,
    the the vector x (resp. y) result from a multiplication M*x and a subsequent
    normalization of the result

    Paramaters
    ----------
    M, x, y (see above definitions)

    Returns
    --------
    tuple : (newx,newy) where newx as well as newy is a 1-dimensional np.ndarray of floats 

    Raises
    ------
    ValueError : if the L2 norm of either x or y is not 1.0 (allow a small deviation of 1e-06

    Example
    -------
    >>> (x,y)=(np.array([ 0.09335276, -0.39213569,  0.45454744,  0.47834171, -0.63410622]),np.array([-0.25395211,  0.1276667 ,  0.80838746, -0.21242824, -0.46967381]))
    >>> M = matrixM(len(x))
    >>> np.around(updatePoints(M@M@M,x,y),3)
    array([[ 0.282,  0.659,  0.03 , -0.571, -0.4  ],
           [ 0.607,  0.375, -0.387, -0.585, -0.01 ]])
    """
    if round(norm(x), 6) != 1.0 or round(norm(y),6) != 1.0:
        raise ValueError("Norm of vector x or y not 1.0 (withing margin of 10^-6)")
    #Force array to be vertical for correct multiplication
    x = M @ x.reshape(-1,1)
    y = M @ y.reshape(-1,1)
    #Make array horisontal again. Using reshape creates a list in a list
    x = x.flatten()
    y = y.flatten()
    #Normalize
    x = x - mean(x)
    y = y - mean(y)
    x = x / norm(x)
    y = y / norm(y)
    return (x,y)

def pairCS(num):
    """ 
    Returns the vectors c and s as explained on slide 21/27 of the lecture slides
    (https://dm561.github.io/assets/DM561-DM562-RandomPolygon.pdf).
    (see also page 11 in the article https://www.cs.cornell.edu/cv/ResearchPDF/EllipsePoly.pdf)

    Parameter
    ---------
    int  :  num  : the number of points of the initial polygon

    Returns 
    -------
    tuple : (c,s) where c as well as s are a 1-dimensional np.ndarray of floats (of length num)
    
    Raises
    ------
    ValueError    if num<=2

    Examples
    --------
    >>> np.around(pairCS(5),3)
    array([[ 0.632,  0.195, -0.512, -0.512,  0.195],
           [ 0.   ,  0.602,  0.372, -0.372, -0.602]])
    """
    if num <= 2:
        raise ValueError("Parameter must be at least 3")
    tau = [0] + [2*i*math.pi / num for i in range(1,num)]
    root = math.sqrt(2 / num)
    c = np.array([root * math.cos(tn) for tn in tau])
    s = np.array([root * math.sin(tn) for tn in tau])
    return (c,s)
    

def convEllipse(x, y):
    """Returns the converged ellipse-like polygon u^{(0)} and v^{(o)} as
    explained on slide 21/27 of the lecture slides
    (https://dm561.github.io/assets/DM561-DM562-RandomPolygon.pdf).

    (see also page 17 in the article
    https://www.cs.cornell.edu/cv/ResearchPDF/EllipsePoly.pdf, but
    note that the formulas in the article has typos. The ellipse-like
    polygon is the converged polygon for even iterations, the polygon
    for odd iterations would look different)

    Parameter
    ---------
    x, y  : the x coordinates and y coorindates of the initial point set,
            both x and y are 1-dimensional np.ndarrays (the length corresponds
            to the number of initial points)
                  

    Returns 
    -------
    np.array of points where each points is a 1-dimensional np.ndarray of 
             length 2, encoding the x and y coordinate of a point of the
             converged ellipse-like polygon.
    
    Raises
    ------
    ValueError    if num<=2

    Examples
    --------
    >>> (x,y)=(np.array([ 0.09335276, -0.39213569,  0.45454744,  0.47834171, -0.63410622]),np.array([-0.25395211,  0.1276667 ,  0.80838746, -0.21242824, -0.46967381]))
    >>> np.around(convEllipse(x,y),3)
    array([[-0.618, -0.37 ],
           [-0.061,  0.374],
           [ 0.58 ,  0.601],
           [ 0.419, -0.002],
           [-0.321, -0.602]])

    """
    #Note the errors supposedly raised by this funtion is invalid.
    #Calculate c and s with same size as the input vectors
    (c,s) = pairCS(x.size)
    #Calculate vectors of x and y coordinates (u and v) of elepsis that is converged towards
    u = ((c @ x.reshape(-1,1)) / dist(c,s,x)) * c + ((s @ x.reshape(-1,1)) / dist(c,s,x)) * s
    v = ((c @ y.reshape(-1,1)) / dist(c,s,y)) * c + ((s @ y.reshape(-1,1)) / dist(c,s,y)) * s
    #Return those vectors as an ndarray of points (which also takes the form of ndarrays with size=2)
    return np.concatenate((u.reshape(-1,1),v.reshape(-1,1)),axis=1)
    

def dist(cosv,sinv,cordv):
    """Intermidiate scalar value for calculating sinus and cosinus of vectors
    Parameter
    ---------
    cosv, sinv  :   The vectors returned from pairCS(num)
    cordv       :   Vector to operate on. All inputs must have same length
                    and is expected to be "flat" (horisontal) numpy ndarrays
    
    Returns
    -------
    Scalar value to assist in other calculations"""
    return math.sqrt((cosv @ cordv.reshape(-1,1))**2+(sinv @ cordv.reshape(-1,1))**2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
