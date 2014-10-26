import bge
from bge import render
import mathutils
from mathutils import Vector

def rotateText(controller):
	scene = bge.logic.getCurrentScene()
	owner = controller.owner
	camera = scene.active_camera
	cameraLocal = camera.localOrientation
	ownerLocal = camera.localOrientation
	#owner.localOrientation = mathutils.Vector((-cameraLocal[0][0], -cameraLocal[0][1], -cameraLocal[0][2]))#FIXME: x local seems to also want to rotate in a strange way
	
def rotateCamera(cont):
	print(cont)
	own = cont.owner
	
	mouse = cont.sensors["mouse"]
	
	xRot = cont.actuators["xRotation"]
	zRot = cont.actuators["zRotation"]
	
	xRot.useLocalDRot= False
	zRot.useLocalDRot = False
	
	cont.activate(xRot)
	cont.activate(zRot)
	
	x = render.getWindowWidth()//2
	y = render.getWindowHeight()//2
	
	screen_center = (x, y)
	
	center = Vector(screen_center)
	
	mouse_position = Vector(mouse.position)
	
	offset = (mouse_position - center) * -0.001
	print (offset)
	
	xRot.dRot = [0, 0,offset.x]
	zRot.dRot = [offset.y, 0, 0]#might cause problems. Check here if something goes wrong
	#xRot.dRot = [offset.y, 0,offset.x]
	
	render.setMousePosition(x,y)