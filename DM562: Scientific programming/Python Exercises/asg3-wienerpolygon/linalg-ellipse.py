"""linalg-ellipse.py

This file is provided for convenience and visualization only.  It
assumes you implemented all the methods in polygon.py, otherwise it
will very likely not work. This file will not be included in the
testing of your implementation. 

"""

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import math
import sys
from polygon import *

# You probably won't need this if you're embedding things in a tkinter plot...
# but it won't hurt
plt.ion()

# Play with the number of points, use small numbers to debug your code
num = 21
fig = plt.figure()
ax = fig.add_subplot(111)

# Inititalise the matrix M
M = matrixM(num)

# For potential speedup
M2 = np.linalg.matrix_power(M,2)
M10 = np.linalg.matrix_power(M,10)
M100 = np.linalg.matrix_power(M,100)
M500 = np.linalg.matrix_power(M,500)

# For backward steps
if num%2 == 1:
    Minv = invMatrixM(M)

# The following is a bit redundant, but x and y are according to the representation
# of the polygon in the paper and on the slides, whereas points is needed for drawing
# the polygon
(x,y) = initPoints(num)

points = np.array([ (x[i], y[i]) for i in range(num) ])

# convEllipse returns an np.array of pairs, where each pair corresponds to
# a point on the converged ellipse. We will plot this in red.  
ellipsePoints = convEllipse(x, y)
ellipsePolygon = Polygon(ellipsePoints, closed=True, fill=False, color='red')

# Backwards in time simulation including drawing of the polygons Set
# to "if True:" if you want to first do some backward steps
# 
if False:
    for i in range(0,20):
        polygon = Polygon(points, closed=True, fill=False)
        ax.cla()
        ax.set_xlim(-0.5, 0.5)
        ax.set_ylim(-0.5, 0.5)
        xP=[first for (first,second) in points]
        yP=[second for (first,second) in points]
        ax.scatter(xP, yP, linewidth=2)
        ax.add_patch(polygon)
        ax.add_patch(ellipsePolygon)
        fig.canvas.draw()
        fig.canvas.flush_events()
        # the following pause is necessary on some systems
        plt.pause(.01)
        (x, y) = updatePoints(Minv, x, y)
        points = np.array([ (x[i], y[i]) for i in range(len(M)) ])

# Forward simulation: the main loop for visualization
for i in range(1,num*num):
        polygon = Polygon(points, closed=True, fill=False)
        ax.cla()
        ax.set_xlim(-0.5, 0.5)
        ax.set_ylim(-0.5, 0.5)
        xP=[first for (first,second) in points]
        yP=[second for (first,second) in points]
        ax.scatter(xP, yP, linewidth=2)
        ax.add_patch(polygon)
        ax.add_patch(ellipsePolygon)
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        # Uncomment if you want to use "return" to visualize
        # one step after the other
        
        #k=input()
        #if k=="q":
        #    sys.exit()
        plt.pause(.01)

        # Change M to M10 or M100 if you want to make more steps at once
        # but be careful with numerical issues!
        (x,y)  = updatePoints(M, x, y)
        points = np.array([ (x[i], y[i]) for i in range(len(M)) ])

