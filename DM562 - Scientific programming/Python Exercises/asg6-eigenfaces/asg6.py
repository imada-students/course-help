"""
Lab 6: Eigenfaces
------------------------------

In this lab you should implement three methods for an Eigenface analysis.

Note, that you need to have an installed version of opencv-python. On 
a Ubuntu 18.04 system you can, e.g., use "pip3 install opencv-contrib-python" to
have the newest version of opencv. 

Start with 

distanceImages (50 points), then
projectAndBackProject (25 points) and
indexDistancePairsSortedByDistance (25 points)

Also study and run Eigenface.py, it is the code for the tool presented in
the lecture. The code in lines 106ff of Eigenface.py (currently in comments) 
will only work if you have implemented the necessary methods. The file
helper.py provides helper function to load all the data. 
"""

import cv2
import math
import numpy as np
from helper import *



def cv2Version():
    """
    Ensure you have cv2 version 3.4.4 installed, otherwise the code might
    risk that your solution does not work. We will use cv2 version 3.4.4 
    for testing. 

    Nothing to implement here. (0 points)

    Returns the cv2 version string.

    Example:
    --------
    >>> cv2.__version__
    '3.4.4'
    """
    return cv2.__version__

def distanceImages(dataImg1, dataImg2):
    """
    Computes the distance between two pictures. (50 points)

    Please use the sqrt of the (sum of squared absolute distances) as a metric
    Note, that even though in the case of non-colored pictures, the 3 color
    channels are identical, you do not need to handle this. 
    
    Parameter:
    ------
    dataImg1 : 1-dimensional numpy.ndarray of length width * height * 3
    dataImg2 : 1-dimensional numpy.ndarray of length width * height * 3
    
    Returns:
    --------
    float    : the distance as described above

    Raises:
    -------
    TypeError : if dataImg1 or dataImg2 are not are 1-dimensional array 

    Example:
    --------
    >>> dataImg1=np.array([ 0.18039216,  0.18039216,  0.18039216,  0.20392157,  0.20392157])
    >>> dataImg2=np.array([ 0.49411765,  0.49411765,  0.49411765,  0.49411765,  0.49411765])
    >>> round(distanceImages(dataImg1, dataImg2),3)
    0.681
    """
    if dataImg1.ndim != 1 or dataImg2.ndim != 1:
        raise TypeError("dataImg not one dimensional array")
    return np.sqrt( sum( (dataImg1 - dataImg2) ** 2 ) )
    

def projectAndBackProject(dataImg, mean, eigenVectors):
    """
    Projects a image into the space of eigenVectors, 
    and back-projects the result into the space of 
    images. (25 points)

    Parameters:
    -----------
    dataImg : numpy.ndarray representing the image 
              shape : (length width * height * 3, )

    mean    : numpy.ndarray representing the image 
              shape : (1, length width * height * 3)

    eigenVectors : numpy.ndarray, representing the first k 
                   eigenvectors (principal components)
                   shape : (k, length width * height * 3)

    Note, that the type and shape of mean and eigenVectors is of the type that you can expect
    as a result of cv2.PCACompute. The type and shape of dataImg is the same as the type and
    shape of data[k:,].
    
 
    Returns:
    --------
    np.ndarray : (1-dimensional) of same shape as dataImg
                 for projection and back-projection you can
                 use cv2.PCAProject and cv2.PCABackProject

    Example (Note, the "340" is changed if you do change 
    the parametrization of the PCA method call in the main function) :
    --------
    >>> (projectAndBackProject(data[0,:], mean, eigenVectors)).shape
    (96768,)
    >>> int(projectAndBackProject(data[0,:], mean, eigenVectors)[0]*1000)
    340
    """
    pass

def indexDistancePairsSortedByDistance(data, r, mean, eigenVectors):
    """Returns an array of tuples (i, distance), where i refers to the
    i-th column in the data matrix (i.e., the i-th image
    vector). distance refers to the distance (see distanceImages) of
    that picture, and the picture that is the result of the
    projectAndBackProject method.  The array is sorted according to
    increasing distance values, i.e., (assuming the result array is
    called r), r[0][0] is the index of the picture which is closest
    to the eigenface space, and r[-1][0] is the index of the picture
    which is furthest away from eigenface space. We will use this to detect
    the one picture which is not a face (but the head of a dog).
    (25 points)

    Parameters:
    -----------
    data : 2-dimensional numpy.ndarray representing all images 
           shape : (k, length width * height * 3), where k is
           the number of input pictures

    r    : a range function with arguments, e.g., range(0,10)
           For all corresponding indices within the range, we
           will compute the distance as described above. 

    mean    : numpy.ndarray representing the image 
              shape : (1, length width * height * 3)

    eigenVectors : numpy.ndarray, representing the first k 
                   eigenvectors (principal components)
                   shape : (k, length width * height * 3)'

    Returns:
    --------
    A list of pairs (i, distance) sorted according to increasing distance
    as described above.

    Example (Note, index 12 is the picture of the dog):
    --------
    >>> indexDistancePairsSortedByDistance(data, range(0,20), mean, eigenVectors)[-1][0]
    12

    """
    pass

if __name__ == '__main__':
    # Number of EigenFaces 
    NUM_EIGEN_FACES = 10
    
    # Directory containing images
    dirName = "images/dm561-dm562/"
    
    # Read images
    images = readImages(dirName)
    
    # Size of images
    sz = images[0].shape
    
    # Create data matrix for PCA.
    data = createDataMatrix(images)

    # Compute the eigenvectors from the stack of images created
    # Use only pictures with indices 100 and larger. Note, that
    # changing this will result in failing doctests. 

    mean, eigenVectors = cv2.PCACompute(data[100:], mean=None, maxComponents=NUM_EIGEN_FACES)
    import doctest
    doctest.testmod()
    
    
    
