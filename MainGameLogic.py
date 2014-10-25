import bge
import mathutils
import random
import xml.etree.ElementTree as ET
import os
import GameLogic

#TODO: Overhaul into an external module...
#TODO: Consider some OOP

#TODO: Figure out if I can dynamically find this information...
print("Initializing SpawnTest globals...")
xOffset = 2.0
yOffset = 2.0
zOffset = 2.0

#bge.logic.addScene('HUD')
#controller = bge.logic.getCurrentController()


def main(controller):
	print("SpawnTest Begin")
	owner = controller.owner

	scene = GameLogic.getCurrentScene()
	print ('Scenes:', bge.logic.getSceneList())

	objects = scene.objects
	hidObjects = scene.objectsInactive

	testDataCubePositioner = hidObjects["DataCubeRoot"]

	cuboidText = hidObjects["DynamicText"]

	#printSceneObjects(scene)

	tmpPath = "C:\\Users\\Glen\\Dropbox\\GradProject\\randomCube.xml" #TODO: Change this to relative path
	tableXMLPath = "C:\\Users\\Glen\\Dropbox\\GradProject\\dataTable.xml"

	#dataCubeFromFile(tmpPath, hidObjects['Cuboid'], cuboidText, testDataCubePositioner, scene)
	dataTable = dataTableFromFile(tableXMLPath)
	
	tableIndex = indexDataTable(dataTable)
	
	dataCubeFromDataTable(dataTable, tableIndex, 'All', None, None, None, None)
	#spawnDataCube(2, 2, 2, scene, hidObjects["Cuboid"], testDataCubePositioner)

	#printSceneObjects(scene)
	print("SpawnTest End")
#Deprecated...
def spawnDataCube(xCuboids, yCuboids, zCuboids, scene, cuboidObject, positioner):
	print("Spawning data cube consisting of", xCuboids, "*", yCuboids, "*", zCuboids, "=", xCuboids*yCuboids*zCuboids, "Cuboids")
	worldPosition = mathutils.Vector((0.0, 0.0, 0.0))
	xOffsetVector = mathutils.Vector((0.0, 0.0, 0.0))
	yOffsetVector = mathutils.Vector((0.0, 0.0, 0.0))
	zOffsetVector = mathutils.Vector((0.0, 0.0, 0.0))
    
	#TODO: optimize to only load the outer cuboids until an operation causes the engine to need new cuboids
	for x in range(xCuboids):
		xOffsetVector = getXOffset(x)
		for y in range(yCuboids):
			yOffsetVector = getYOffset(y)
			for z in range(zCuboids):
				zOffsetVector = getZOffset(z)

				#TODO: Add property for data on each side of the cuboid 
				#TODO: (can be reduced to a simple 3 element list for x, y, z side since only three sides are unique on cube
				#TODO: reciprocal of each side should be the same)

				tmpObject = scene.addObject(cuboidObject, positioner, 0)
				tmpObject.setParent(positioner)
				#print('Parent location =', positioner.worldPosition)
				newLocalPosition = xOffsetVector + yOffsetVector + zOffsetVector - mathutils.Vector((xCuboids/2.0, yCuboids/2.0, zCuboids/2.0))#Subtracting by this vector *should* ensure that the root node is in the center of the cube.
				#print('New local position: ', newLocalPosition)
				tmpObject.localPosition = newLocalPosition
				tmpObject['xFaceData'] = x
				tmpObject['yFaceData'] = y
				tmpObject['zFaceData'] = z
				tmpObject.occlusion = True #Testing occlusion
				spawnText(tmpObject, cuboidText, x , y , z)
				#tmpObject.color = mathutils.Vector((0.0, 0.5, 1.0, 1.0))#TODO: Add this to colorTest()
				#colorTest(tmpObject)

'''
Creates a datacube from an XML file.
Inputs
	filepath - String - The path to the XML file, from which the cube is to be created.
	cuboidObject - - The template object for creating the cuboid. This object should be a hudden object.
	positioner - - An empty object that represents the 
Outputs
'''                
def dataCubeFromFile(filepath, cuboidObject, cuboidText, positioner, scene):
	cubeData = ET.parse(filepath)
	root = cubeData.getroot()
	print("tag:", root.tag)
	print ("attributes", root.attrib)
    
	xCuboids = int(root.attrib['xSize'])
	yCuboids = int(root.attrib['ySize'])
	zCuboids = int(root.attrib['zSize'])

	for child in root.findall('cuboid'):
		#	print (child.tag, child.attrib)
		xOffsetVector = getXOffset(int(child.attrib['x']))
		yOffsetVector = getYOffset(int(child.attrib['y']))
		zOffsetVector = getZOffset(int(child.attrib['z']))
		
		tmpObject = scene.addObject(cuboidObject, positioner, 0)
		tmpObject.setParent(positioner)
		newLocalPosition = xOffsetVector + yOffsetVector + zOffsetVector - mathutils.Vector((xCuboids/2.0, yCuboids/2.0, zCuboids/2.0))#Subtracting by this vector *should* ensure that the root node is in the center of the cube.
		tmpObject.localPosition = newLocalPosition
		tmpObject.occlusion = True
		
		tmpObject['FrontValue'] = child.find('Front').text
		tmpObject['BackValue'] = child.find('Back').text
		tmpObject['LeftValue'] = child.find('Left').text
		tmpObject['RightValue'] = child.find('Right').text
		tmpObject['TopValue'] = child.find('Top').text
		tmpObject['BottomValue'] = child.find('Bottom').text
		
		#for cChild in child:
			#print(cChild.tag, cChild.attrib)
		
		#print(child.get('xValue'), child.get('yValue'), child.get('zValue'))
		
		#tmpObject['xFaceData'] = child.find('xValue').text
		#tmpObject['yFaceData'] = child.find('yValue').text
		#tmpObject['zFaceData'] = child.find('zValue').text
		
		#print(tmpObject['xFaceData'], tmpObject['zFaceData'], tmpObject['yFaceData'])
		
		spawnText(tmpObject, cuboidText, scene)

def dataCubeFromDataTable(dataTable, dataTableIndex, dimensionLimit, cuboidObject, cuboidText, positioner, scene):
	limit = dataTableIndex[dimensionLimit]
	firstDimensionIndices = secondDimensionIndices = thirdDimensionIndices = []
	'''TODO: Move this section to "dataTableFromFile"'''
	#Create an set containing the values of each of the three dimensions.
	for i in range(limit[0], limit[1]):
		firstDimVal = dataTable[i][1]
		secondDimVal = dataTable[i][2]
		thirdDimVal = dataTable[i][3]
		if(firstDimensionIndices.count(firstDimVal) == 0):
			firstDimensionIndices.append(firstDimVal)
		if(secondDimensionIndices.count(secondDimVal) == 0):
			secondDimensionIndices.append(secondDimVal)
		if(thirdDimensionIndices.count(thirdDimVal) == 0):
			thirdDimensionIndices.append(thirdDimVal)
			
	'''print("\n[Debug] First Dimension Indices", firstDimensionIndices)
	print("\n[Debug] Second Dimension Indices", secondDimensionIndices)
	print("\n[Debug] Third Dimension Indices\n", thirdDimensionIndices)'''
	
	#Create a 3d array containing the data of the cube
	#Array initialized to ' ' for each element
	cubeTable = []
	for y in range(len(firstDimensionIndices)):
		currentRow = []
		for x in range(len(secondDimensionIndices)):
			currentCol = []
			for z in range(len(thirdDimensionIndices)):
				currentCol.append(' ')
				pass
			currentRow.append(currentCol)
		cubeTable.append(currentRow)
	
	#Populate the 3d array with its values
	for i in  range(limit[0], limit[1]):
		y = firstDimensionIndices.index(dataTable[i][1])
		x = secondDimensionIndices.index(dataTable[i][2])
		z = thirdDimensionIndices.index(dataTable[i][3])
		value = dataTable[i][4]
		cubeTable[y][x][z] = value
	'''print(cubeTable)'''
	'''End TODO'''
	
	#Create data cube
	
	pass
	
'''
Loads a data table from an XML file.
Returns a two dimensional list of "n" columns containing the data from a "cube()" operations.
output[0] = nth dimension of the cube operation
output[-2] = first diemsnion of the cube operation
output[-1] = the value of the cube operation
'''
def dataTableFromFile(filepath):
	#Open the xml file
	xmlData = ET.parse(filepath)
	root = xmlData.getroot()
	print("tag:", root.tag)
	print ("attributes", root.attrib)
	
	#Get the height of the table from the XML file
	height = int(root.attrib['height'])
	
	#Get the width of the table from the XML file
	width = int(root.attrib['width'])
	
	#Initialize the data table to null-strings
	dataTable = []
	for y in range(height):
		xList = []
		for x in range(width):
			xList.append(" ")
		dataTable.append(xList)
			
	#Insert the data from XML into the table
	for child in root.findall('DataElement'):
		y = int(child.attrib['y'])
		x = int(child.attrib['x'])
		dataTable[y][x] = child.text
	for t in dataTable:
		print (t)
	return dataTable
	
'''
Returns a dict mapping the 4th dimension values to the range values associated with this value.
This dict will then be used to limit data cubes against the 4th dimension.
TODO: consider nesting dicts for even higher dimensionality
'''
def indexDataTable(dataTable):
	outputDict = {}
	currentIndexValue = dataTable[0][0]
	currentLowerBound = 0
	for index in range(1, len(dataTable)):
		nextIndexValue = dataTable[index][0]
		if nextIndexValue != currentIndexValue:
			outputDict[currentIndexValue] = (currentLowerBound, index)
			currentLowerBound = index
			currentIndexValue = nextIndexValue
	print(outputDict)
	return outputDict

def spawnText(cuboidParent, cuboidText, scene):
	#X texts
	#print("[DEBUG]Handling x text")
	tmpText = addText(cuboidParent, cuboidText, mathutils.Vector((1.1, 0.0, 0.0)), mathutils.Vector((0.0, 3.14/2.0, 0.0)), 'RightValue', scene)
	tmpText = addText(cuboidParent, cuboidText, mathutils.Vector((-1.1, 0.0, 0.0)), mathutils.Vector((0.0, -3.14/2.0, 0.0)), 'LeftValue', scene)
	
	#Y texts
	tmpText = addText(cuboidParent, cuboidText, mathutils.Vector((0.0, 1.1 , 0.0)), ((-3.14/2.0, 0.0, 0.0)), 'BackValue', scene)
	tmpText = addText(cuboidParent, cuboidText, mathutils.Vector((0.0, -1.1, 0.0)), mathutils.Vector((3.14/2.0, 0.0, 0.0)), 'FrontValue', scene)
	
	#Z texts
	tmpText = addText(cuboidParent, cuboidText, mathutils.Vector((0.0, 0.0, 1.1)), mathutils.Vector((0.0, 0.0, 0.0)), 'TopValue', scene)
	tmpText = addText(cuboidParent, cuboidText, mathutils.Vector((0.0, 0.0, -1.1)), mathutils.Vector((0.0, 3.14, 0.0)), 'BottomValue', scene)
    
def addText(cuboidParent, cuboidText, displacement, localRotation, axisValueProperty, scene):
	tmpText = scene.addObject(cuboidText, cuboidParent, 0)
	tmpText.setParent(cuboidParent)
	tmpText.applyMovement(displacement, True)
	tmpText.applyRotation(localRotation, True)
	textValue = cuboidParent[axisValueProperty]
	tmpText.text = textValue
	if int(textValue) > 10:
		tmpText.localScale = mathutils.Vector((0.5, 0.5, 0.5))
	return tmpText

'''
Returns the x offest needed to place a cuboid in the world space
Inputs
	xValue - (float) - The "x" position of the cuboid in the cuboid array
Outputs
	mathutils.Vector() - Vector containing the x offset
'''
def getXOffset(xValue):
	return mathutils.Vector((xValue * xOffset, 0.0, 0.0))

'''
Returns the y offest needed to place a cuboid in the world space
Inputs
	yValue - (float) - The "y" position of the cuboid in the cuboid array
Outputs
	mathutils.Vector() - Vector containing the y offset
'''
def getYOffset(yValue):
	return mathutils.Vector((0.0, yValue * yOffset, 0.0))

'''
Returns the z offest needed to place a cuboid in the world space
Inputs
	zValue - (float) - The "z" position of the cuboid in the cuboid array
Outputs
	mathutils.Vector() - Vector containing the z offset
'''
def getZOffset(zValue):
	return mathutils.Vector((0.0, 0.0, zValue * zOffset))
'''
Prints every object held within the scene to the console.
Inputs
	Scene - KX_Scene(PyObjectPlus) - The scene from which objects should be printed.
Outputs
	None
'''
def printSceneObjects(scene):
	print("Scene:", scene)
	for object in scene.objects:
		print(object.name, "is loaded.")
	for hiddenObject in scene.objectsInactive:
		print(hiddenObject.name, "is loaded, but hidden.")
        
def colorTest(cuboidObject):
	meshes = cuboidObject.meshes
	for mesh in meshes:
		print(mesh, "- cuboid mesh. Has", mesh.numMaterials, "materials.")
		for material in mesh.materials:
			materialIDX = material.getMaterialIndex()
			numVertices = mesh.getVertexArrayLength(materialIDX)
			print(material, "Material has", numVertices, "vertices.")
			for vertexIDX in range(numVertices):
				vertex = mesh.getVertex(materialIDX, vertexIDX)
				vertex.setRGBA([random.random(), random.random(), random.random(), 1.0])
#main()

class DataCube:
	def __init__(self):
		pass

class Cuboid:
	FRONT = 0
	BACK = 1
	LEFT = 2
	RIGHT = 3
	TOP = 4
	BOTTOM = 5
	#TODO: add a way to link this object to a DataCube object
	def __init__(self, dataCubeParent, scene, positionVector):
		self.dataCubeParent = dataCubeParent
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