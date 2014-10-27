import bge
from bge import render
import math
import mathutils
from mathutils import Vector

def rotateText(controller):
	scene = bge.logic.getCurrentScene()
	owner = controller.owner
	camera = scene.active_camera
	cameraLocal = camera.localOrientation
	ownerLocal = camera.localOrientation
	#owner.localOrientation = mathutils.Vector((-cameraLocal[0][0], -cameraLocal[0][1], -cameraLocal[0][2]))#FIXME: x local seems to also want to rotate in a strange way

'''
Courtesy of: http://www.cgmasters.net/free-tutorials/fps-mouselook-script-plus-real-text/
Modified by Glen Wallace
'''	
def rotateCamera(cont):
	#print(cont)

	owner = cont.owner
	parent = owner.parent
	
	mouse = cont.sensors["mouse"]
	
	sensitivity = 0.05
	
	#camera rotation limits
	high_limit = 180
	low_limit = 0
	
	h = render.getWindowHeight()//2
	w = render.getWindowWidth()//2
	y = (h-mouse.position[1])*sensitivity
	x = (w-mouse.position[0])*sensitivity
	'''print('H W:', h, w)
	print('Mouse position:', mouse.position)
	print('Y X:', y, x)'''
	
	rot = owner.localOrientation.to_euler()
	pitch = abs(math.degrees(rot[0]))
	
	pitch += y
	
	if(pitch) < low_limit:
		pitch = low_limit
	elif(pitch) > high_limit:
		pitch = high_limit
	rot[0] = math.radians(pitch)
	
	owner.localOrientation = rot.to_matrix()
	
	parentRotation = parent.localOrientation.to_euler()
	yaw = math.degrees(parentRotation[2]) + x #Check this if anything goes wrong
	parentRotation[2] = math.radians(yaw)
	parent.localOrientation = parentRotation.to_matrix()

	
	render.setMousePosition(int(w),int(h))
