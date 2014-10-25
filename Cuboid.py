import bge

def class Cuboid:
	FRONT = 0
	BACK = 1
	LEFT = 2
	RIGHT = 3
	TOP = 4
	BOTTOM = 5
	#TODO: add a way to link this object to a DataCube object
	def __init__(self, scene):
		self.scene = scene
		self.dataValues = (0, 0, 0, 0, 0, 0)
	
	'''
	Sets the value of a given face.
	'''
	def setFaceValue(self, face, value):
		self.dataValues[face] = value
		pass
	
	'''
	Returns the value associated with a given face.
	'''
	def getFaceValue(self, face):
		return dataValues[face]
		pass