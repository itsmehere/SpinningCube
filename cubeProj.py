import numpy as np
import copy as cp

class Cube:
    def __init__(self, width, height, depth, pg):
        self.w = width
        self.h = height
        self.d = depth
        self.pg = pg
        self.nodes = []
        self.compositeMatrix = ""

        self.canvas = self.pg.display.set_mode((self.w, self.h))
        self.canvas.fill((0, 0, 0))
        self.pg.display.set_caption('Analysis Project - 3D Spinning Cube')
    

    def addPoint(self, point):
        point = np.append(point, 1)
        self.nodes.append(point)


    def generateVertices(self, CENTER_OFFSET):
        minX = (self.w / 2) - CENTER_OFFSET
        maxX = (self.w / 2) + CENTER_OFFSET

        minY = (self.h / 2) + CENTER_OFFSET
        maxY = (self.h / 2) - CENTER_OFFSET

        minZ = (self.d / 2) - CENTER_OFFSET
        maxZ = (self.d / 2) + CENTER_OFFSET

        # Create cube vertices
        vertices = np.array([(x, y, z) for x in (minX, maxX) for y in (minY, minX) for z in (minZ, maxZ)])

        for vertex in vertices:
            self.addPoint(vertex)

    
    def generateEdges(self, CENTER_OFFSET):
        # Generate edges of the cube
        return NotImplementedError

    def createCompositeMatrix(self, theta):
        cos = np.cos(theta)
        sin = np.sin(theta)

        x = -1 * self.w / 2
        y = -1 * self.h / 2
        z = -1 * self.d / 2

        translationMatrix1 = [[1, 0, 0, x],
                              [0, 1, 0, y],
                              [0, 0, 1, z],
                              [0, 0, 0, 1]]

        rotationMatrixY = [[cos, 0, sin, 0],
                           [0, 1, 0, 0],
                           [-sin, 0, cos, 0],
                           [0, 0, 0, 1]]

        rotationMatrixX = [[1, 0, 0, 0],
                           [0, cos, -sin, 0],
                           [0, sin, cos, 0],
                           [0, 0, 0, 1]]

        translationMatrix2 = [[1, 0, 0, -x],
                              [0, 1, 0, -y],
                              [0, 0, 1, -z],
                              [0, 0, 0, 1]]

        transformations = [translationMatrix2, rotationMatrixY, rotationMatrixX, translationMatrix1]
        self.compositeMatrix = transformations[0]

        for i in range(1, len(transformations)):
            self.compositeMatrix = np.matmul(self.compositeMatrix, transformations[i])


    def applyTransformation(self):
        for i in range(0, len(self.nodes)):
            self.nodes[i] = np.matmul(self.compositeMatrix, self.nodes[i])
            # print(self.nodes[i])


    def displayCube(self):
        for node in self.nodes:
            self.pg.draw.circle(self.canvas, (255, 255, 255), (int(node[0]), int(node[1])), 4, 0)