"""Messy, but fairly optimized code for drawing the mandelbrot set using
turtle graphics"""

import turtle

"""These values can be modyfied to change the rendering"""

width = 200 			#Size in max distance from 0,0. Medium performance impact
						#width = 500 fits a maximized window on a 1080p screen
height = width 			#Needs to be a square to render properly
maxiterations = 255		#Precision or sharpness. Higher values needed when zooming.Low performance impact
						#A value of 255 gives good colours at 100% zoom
spacing = 1				#Only check every x pixels. Use 1 for perfect image. High performance impact.
						#Use a higher value to test rendering. Usefull when zooming


zoompercent = 100 / 100	#How zoomed in. Modyfies performance of maxiterations
zoomx = 0				#Offset x and y to zoom in on.
zoomy = 0				#These two are supposed to be coordinates on the mandelbrot set, but it changes with zoom.

updatetime = 5 			#number of lines to update at a time. Changeging performance impact


"""Global variables, not supposed to be changed"""
updatecount = 0			

xoffset = 0.75 * width	#Approxymately centers the set on canavas

tu = turtle.Turtle()	#Prepares the turtle
tu.speed(0)
tu.hideturtle()
tu.up()
turtle.tracer(0, 0)
turtle.Screen().colormode(255)
escaped = prevesc = 0


"""Methods"""
def draw(x, y):
	"""Draws a single pixel at x,y"""
	tu.up()
	tu.setpos(x,y)
	tu.down()
	tu.setpos(x + 1,y)
	
def maprangex(val):
	"""Maps a pixel x-coordinate to be rendered to be between -1 and 1"""
	tomax = 1
	tomin = -1
	valnorm = (val + width) / (width + width)
	return (tomin + valnorm * (tomax - tomin) + zoomx) / zoompercent
	
def maprangey(val):
	"""Maps a pixel y-coordinate to be rendered to be between -1 and 1"""
	tomax = 1
	tomin = -1
	valnorm = (val + height) / (height + height)
	return (tomin + valnorm * (tomax - tomin) + zoomy) / zoompercent
	
def mandelbrot(x, y):
	"""Returns true if pixel at x,y is in the (approxemated) mandelbrot set"""
	normx = maprangex(x)
	normy = maprangey(y)
	xcalc = 0.0
	ycalc = 0.0
	iteration = 0
	expon = 2
	while (xcalc**expon + ycalc**expon < 2**expon and iteration < maxiterations):
		temp = xcalc**expon - ycalc**expon + normx
		ycalc = 2*xcalc*ycalc + normy
		xcalc = temp
		iteration += 1
	if (xcalc**expon + ycalc**expon < 2**expon):
		return iteration
	return iteration

def mapcolor(val, maxval):
	"""This sets the turtle pen colour based on how many iterations out
	of the maximum iterations have been reached"""
	norm = val / maxval
	#Red, green and blue components
	r = int(193.80370873*norm**2+61.19629127*norm)
	g = int(-1020*norm**2+1020*norm)
	b = int(193.80370873*norm**2-448.80370873*norm+255)
	
	#Forces colours to be withing 0-255
	r = forcerange(r)
	g = forcerange(g)
	b = forcerange(b)
	tu.pencolor(r, g, b)

def forcerange(colval):
	"""Caps a value at 0 and 255"""
	if colval > 255:
		return 255
	elif colval < 0:
		return 0
	else:
		return colval

"""Main code"""
for y in range(-height, height + 1, spacing):				#For every line
	prevesc = escape = 0									#Reset variables
	for x in range(int(-width*2.5), width + 1, spacing):	#For every pixel in line
		escape = mandelbrot(x, y)							#Checks if pixel escaped
		
		if escape != prevesc:
			if tu.ycor() != y:
				tu.up()
			else:
				tu.down()
			tu.setpos(x + xoffset,y)
			if escape != maxiterations:
				mapcolor(escape, maxiterations)
			else:
				tu.pencolor(0,0,0)
		prevesc = escaped									
	updatecount += 1
	if updatecount > updatetime:							#Updates the drawing every updatetime lines
		turtle.update()
		updatecount = 0

	
turtle.update()						#Final update
turtle.mainloop()					#mainloop prevents the window from freezing