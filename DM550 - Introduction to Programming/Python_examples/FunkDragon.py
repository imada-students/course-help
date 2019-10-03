"""Messy code for drawing a funky dragon curve using turtle graphics"""


import turtle

#Settings to mess with
length = 1				#Line length in pixels
maxiterations = 15		#15 is fine, 18 is probably max performance wise
startblue = False		#Direction of colour

#Things you can mess with, but maybe shouldn't
tu = turtle.Turtle()
tu.speed(0)
tu.up()
tu.setpos(0, 0)	#Start position
tu.rt(90)				#Start rotation
tu.down()
turtle.Screen().colormode(255)
tu.pencolor(255,0,255)
tu.hideturtle()			#Hiding the turtle
turtle.tracer(0, 0)		#This hides the drawing, speeding the process up massively

#Function definitions
def mapcolor(val, maxval):
	"""This sets the turtle pen colour based on how many iterations out
	of the maximum iterations have been reached"""
	norm = val / maxval
	#Red, green and blue components
	r = int(193.80370873*norm**2+61.19629127*norm)
	g = int(-1020*norm**2+1020*norm)
	b = int(193.80370873*norm**2-448.80370873*norm+255)
	
	"""Other colour schemes. They are all ugly
	b = int(611.9047619*norm**2-356.9047619*norm)
	g = int(-1416.6667*norm**2+1204.1667*norm)
	r = int(546.5853*norm**2-291.5853*norm)"""
	
	"""b = int(1030.952380952*x**2 - 1085.952380952*x + 255)
	g = int(-3750 *x**2 + 6500*x - 2550)
	r = int(-6375 *x**2 + 6375*x - 1338.75)"""
	
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
	

def turtledo(directions):
	"""Makes the turtle draw using a list of turns to make"""
	for dir in directions:
		tu.fd(length)
		
		if dir == 'R':
			tu.setheading(tu.heading() + 90)
		elif dir == 'L':
			tu.setheading(tu.heading() - 90)
	pass
	
def dragon(directions, iterations):
	"""This makes a list of lists of instructions to draw each iteration
	of the dragon curve"""
	#print(directions)
	#mapcolor(iterations, maxiterations)
	#turtledo(directions[2*(maxiterations - iterations)-1:])
	if (iterations < 1):
		#turtledo(directions)
		return
	else:
		revdir = directions
		revdir = list(reversed(revdir))
		for i in range(len(revdir)):
			if revdir[i] == 'R':
				revdir[i] = 'L'
			else:
				revdir[i] = 'R'
		drawdirections.append(list(['R'] + revdir))			#Expands the global list of lists of drawingdirections
		dragon(directions + ['R'] + revdir, iterations - 1)	#Recursively run the dragon curve
	pass

#Main code

drawdirections = [[]]				#Global variable to store drawing directions	

def makedragon():
	#drawdirections = [[]]				#Global variable to store drawing directions	
	dragon(['R'], maxiterations)		#Calculate directions for the dragon curve


	i = maxiterations					
	for instr in drawdirections:
		if startblue:
			mapcolor(maxiterations - i, maxiterations)
		else:
			mapcolor(i, maxiterations)
		
		i -= 1
		turtledo(instr)					#Draws the actual curve
		turtle.update()					#Displays the newly drawn curve
		print(i+1)						#Information to show when finished. 0 = finished


"""for i in range(8):
	tu.up()
	#tu.setpos(0,0)
	tu.down()
	makedragon()
	drawdirections = [[]]
	tu.rt(100)"""
makedragon()

turtle.update()
turtle.mainloop()

