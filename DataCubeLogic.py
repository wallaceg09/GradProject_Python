import bge
import mathutils

ROTATE_RADIANS = 3.14 / 2.0

def rotateDataCube(controller):
	mouseWheelUpSensor = controller.sensors['MouseWheelUp']
	mouseWheelDownSensor = controller.sensors['MouseWheelDown']
	leftAltKeyboardSensor = controller.sensors['LAlt']
	leftControlKeyboardSensor = controller.sensors['LControl']
	mouseOverSensor = controller.sensors['MouseOver']
	'''
	If the mouse wheel is scrolled up then rotate positive on the Z axis if left alt is also pressed or rotate positive on the Y axis if left control is also pressed otherwise rotate positive on the X axis
	'''
	if mouseWheelUpSensor.positive:
		objectParent = __getCube(mouseOverSensor)
		if objectParent is not None:
			if leftAltKeyboardSensor.positive:
				rotateZPositive(objectParent)
			elif leftControlKeyboardSensor.positive:
				rotateYPositive(objectParent)
			else:
				rotateXPositive(objectParent)
	'''
	If the mouse wheel is scrolled down then rotate negative on the Z axis if left alt is also pressed or rotate negative on the Y axis if left control is also pressed otherwise rotate negative on the X axis
	'''
	if mouseWheelDownSensor.positive:
		objectParent = __getCube(mouseOverSensor)
		if objectParent is not None:
			if leftAltKeyboardSensor.positive == True:
				print('if')
				rotateZNegative(objectParent)
			elif leftControlKeyboardSensor.positive == True:
				print('elif')
				rotateYNegative(objectParent)
			else:
				rotateXNegative(objectParent)
'''
TODO: Consider creating an animation for each of the rotations
'''
def rotateXPositive(objectParent):
	print('Rotating x positive')
	objectParent.applyRotation(mathutils.Vector((ROTATE_RADIANS, 0.0, 0.0)))
def rotateXNegative(objectParent):
	print('Rotating x negative')
	objectParent.applyRotation(mathutils.Vector((-ROTATE_RADIANS, 0.0, 0.0)))
def rotateYPositive(objectParent):
	print('Rotating y positive')
	objectParent.applyRotation(mathutils.Vector((0.0, ROTATE_RADIANS, 0.0)))
def rotateYNegative(objectParent):
	print('Rotating y negative')
	objectParent.applyRotation(mathutils.Vector((0.0, -ROTATE_RADIANS, 0.0)))
def rotateZPositive(objectParent):
	print('Rotating z positive')
	objectParent.applyRotation(mathutils.Vector((0.0, 0.0, ROTATE_RADIANS)))
def rotateZNegative(objectParent):
	print('Rotating z negative')
	objectParent.applyRotation(mathutils.Vector((0.0, 0.0, -ROTATE_RADIANS)))

def __getCube(mouseOverSensor):
		objectHit = mouseOverSensor.hitObject
		if objectHit is not None:#This is needed because every few updates the objectHit would be 'None' for some reason
			print(objectHit)
			return objectHit.parent