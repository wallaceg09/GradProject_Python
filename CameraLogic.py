import bge
import mathutils

def rotateText(controller):
	scene = bge.logic.getCurrentScene()
	owner = controller.owner
	camera = scene.active_camera
	cameraLocal = camera.localOrientation
	ownerLocal = camera.localOrientation
	#owner.localOrientation = mathutils.Vector((-cameraLocal[0][0], -cameraLocal[0][1], -cameraLocal[0][2]))#FIXME: x local seems to also want to rotate in a strange way