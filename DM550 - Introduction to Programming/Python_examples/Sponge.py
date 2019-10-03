from vpython import *

spcolor = vector(1,0,1)

maxiterations = 3
size = 3**maxiterations

dummy = box(pos=vector(0,0,0), size=vector(0.0001,0.0001,0.0001), color = spcolor)
boxlist = []
ultbox = dummy


def buildsponge(x, y, z, length, iterations):
	global boxlist
	global ultbox
	if iterations > 0:
		length /= 3
		iterations -= 1
		splay(x,y,z + length, length, iterations)
		splay(x,y,z - length, length, iterations)
		buildsponge(x - length, y + length, z, length, iterations)
		buildsponge(x + length, y + length, z, length, iterations)
		buildsponge(x - length, y - length, z, length, iterations)
		buildsponge(x + length, y - length, z, length, iterations)
		print("We need to go deeper")
		return None
		
	print("Box!")
	boxlist.append(box(pos=vector(x,y,z), size=vector(1,1,1), color = vector(1-x / size, 1-y / size, 1-z / size)))
	return None

def splay(x, y, z, length, iterations):
	length
	buildsponge(x - length, y + length, z, length, iterations)
	buildsponge(x, y + length, z, length, iterations)
	buildsponge(x + length, y + length, z, length, iterations)
	
	buildsponge(x - length, y, z, length, iterations)
	buildsponge(x + length, y, z, length, iterations)
	
	buildsponge(x - length, y - length, z, length, iterations)
	buildsponge(x, y - length, z, length, iterations)
	buildsponge(x + length, y - length, z, length, iterations)
	return None	

buildsponge(0,0,0, size, maxiterations)
print("Done")