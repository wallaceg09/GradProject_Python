import bge

#Mouse constants
#FIXME: see if these constants are correct
RIGHT_MOUSE = 189
#LEFT_MOUSE = 

#Event constants
#FIXME: see if these constants are correct
JUST_PRESSED = 1
HELD = 2
JUST_RELEASED = 3
def rightMouseButton(cont):
	if(bge.logic.mouse.events[RIGHT_MOUSE] == JUST_PRESSED):
		print("Right button clicked!")
		#TODO: Make safe
		tmp = eval(input("Input something!"))
		print(tmp)
def leftMouseButton(cont):
	print ("Left button clicked!")