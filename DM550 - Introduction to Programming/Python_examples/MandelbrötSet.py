"""Messy, but fairly optimized code for drawing the mandelbrot set using
turtle graphics"""

import turtle

"""These values can be modyfied to change the rendering"""

width = 300 			#Size in max distance from 0,0. Medium performance impact
						#width = 500 fits a maximized window on a 1080p screen
height = width 			#Needs to be a square to render properly
maxiterations = 100		#Precision or sharpness. Higher values needed when zooming. Low performance impact
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
escaped = False
prevesc = False


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
		return True
	return False

"""Main code"""
for y in range(-height, height + 1, spacing):				#For every line
	prevesc = escaped = False								#Reset variables
	for x in range(int(-width*2.5), width + 1, spacing):	#For every pixel in line
		escaped = mandelbrot(x, y)							#Checks if pixel escaped
		if escaped and not prevesc:							#Places a turtle at a escaped pixel, if the previous pixel does not escape
			tu.up()
			tu.setpos(x + xoffset,y)
			tu.down()
		elif not escaped and prevesc or x >= width and escaped:	#Draws a line to the last pixel, if that pixel that escaped, whilst the current did not
			tu.setpos(x + xoffset - 1, y)
		prevesc = escaped									
	updatecount += 1
	if updatecount > updatetime:							#Updates the drawing every updatetime lines
		turtle.update()
		updatecount = 0

	
turtle.update()						#Final update
turtle.mainloop()					#mainloop prevents the window from freezing