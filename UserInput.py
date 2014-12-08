import bge
import MainGameLogic

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
		owner = cont.owner
		print(owner)
		print("Right button clicked!")
		MainGameLogic.clearDataCube(owner['dataCube'])
		uInput = input("Input something!")
		owner['dataCube'] = MainGameLogic.dataCubeFromDataTable(owner['dataTable'], owner['tableIndex'], uInput, owner['cuboidObject'], owner['cuboidText'], owner['cubePositioner'], owner['scene'])
		#TODO: Make safep
		#print(tmp)
def numberOneKey(cont):
	JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
	#keyboard = bge.logic.keyboard
	keyboard = cont.sensors["OneKey"]
	key_status = keyboard.getKeyStatus(bge.events.ONEKEY) 
	#print(type(keyboard))
	#print(key_status)
	if key_status is 1:
		owner = cont.owner
		cube = owner['dataCube']
		for y in range(0, len(cube)):
			for x in range(0, len(cube[0])):
				for z in range(0, len(cube[0][0])):
					if x is not 0:
						MainGameLogic.toggleVisible(cube[y][x][z])
	#print(key)
	'''if keyboard.events[key] == JUST_ACTIVATED:
		print("Test")'''
def numberTwoKey(cont):
	JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
	#keyboard = bge.logic.keyboard
	keyboard = cont.sensors["TwoKey"]
	key_status = keyboard.getKeyStatus(bge.events.TWOKEY) 
	#print(type(keyboard))
	print(key_status)
	if key_status is 1:
		owner = cont.owner
		cube = owner['dataCube']
		for y in range(0, len(cube)):
			for x in range(0, len(cube[0])):
				for z in range(0, len(cube[0][0])):
					#not(x == 0 and z == 0) >> 
					if not(x is 0 and z is 0):
						print(y, x, z)
						MainGameLogic.toggleVisible(cube[y][x][z])
						
def numberThreeKey(cont):
	JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
	#keyboard = bge.logic.keyboard
	keyboard = cont.sensors["ThreeKey"]
	key_status = keyboard.getKeyStatus(bge.events.THREEKEY) 
	#print(type(keyboard))
	print(key_status)
	if key_status is 1:
		owner = cont.owner
		cube = owner['dataCube']
		for y in range(0, len(cube)):
			for x in range(0, len(cube[0])):
				for z in range(0, len(cube[0][0])):
					#not(x == 0 and z == 0) >> 
					if not(x is 0 and y is 0 and z is 0):
						print(y, x, z)
						MainGameLogic.toggleVisible(cube[y][x][z])
#def leftMouseButton(cont):
#	print ("Left button clicked!")