import turtle

size =  729	#The side length of the coloured square
			#Powers of 3 works best. Products of powers of 3 works ok
			#Any number can be used, but the squares will be rounded to integer pixel coordinates

tu = turtle.Turtle()
turtle.Screen().colormode(255)
tu.pencolor(200,10,255)
tu.fillcolor(200,10,255)
turtle.hideturtle()
def straightright(l):
	tu.fd(l)
	tu.right(90)

def square(l):
	for i in range(4):
		straightright(l)

def fillwhite(x, y, length, depht):
	if depht <= 0:
		return None
	elif length > 40:
		pass
		turtle.update()
	tu.up()
	tu.setx(x)
	tu.sety(y)
	
	length /= 3
	
	tu.fd(length)
	tu.rt(90)
	tu.fd(length)
	tu.lt(90)
	tu.down()
	tu.begin_fill()
	square(length)
	tu.end_fill()
	
	fillwhite(x, y, length, depht -1)
	fillwhite(x + length, y, length, depht -1)
	fillwhite(x + 2*length, y, length, depht -1)
	y -= length
	fillwhite(x, y, length, depht -1)
	fillwhite(x + 2*length, y, length, depht -1)
	y -= length
	fillwhite(x, y, length, depht -1)
	fillwhite(x + length, y, length, depht -1)
	fillwhite(x + 2*length, y, length, depht -1)
	
turtle.tracer(0,0)
tu.hideturtle()	
turtle.setundobuffer(None)
tu.up()
tu.setpos(-size//2, size//2)
tu.down()
tu.begin_fill()
square(size)
tu.end_fill()
tu.pencolor(255,255,255)
tu.fillcolor(255,255,255)

fillwhite(-size//2,size//2,size, 5)
turtle.update()
turtle.mainloop()