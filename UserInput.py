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
	#print(bge.types.SCA_MouseSensor.getButtonStatus(cont.sensors["RightButton"]))
	rightButton = cont.sensors["RightButton"]
	buttonStatus = rightButton.getButtonStatus(bge.events.RIGHTMOUSE)
	
	if(buttonStatus == bge.logic.KX_INPUT_JUST_ACTIVATED):
		print("Right button clicked!")
		#TODO: Make safe
		tmp = eval(input("Input something!"))
		print(tmp)
def leftMouseButton(cont):
	print ("Left button clicked!")