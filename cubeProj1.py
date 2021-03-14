import numpy as np
import copy as cp

class Cube:
    def __init__(self, width, height, depth, pg):
        self.w = width
        self.h = height
        self.d = depth
        self.pg = pg
        self.nodes = []

        self.canvas = self.pg.display.set_mode((self.w, self.h))
        self.canvas.fill((203, 203, 203))
        self.pg.display.set_caption('Analysis Project - 3D Spinning Cube')
    
    def addPoint(self, point):
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

    def rotateAroundY(self, theta):
        for i in range(0, len(self.nodes)):
            node = cp.deepcopy(self.nodes[i])

            cos = np.cos(theta)
            sin = np.sin(theta)

            x = self.w / 2
            y = self.h / 2
            
            rotationMatrixY = [[cos, 0, sin],
                               [0, 1, 0],
                               [-sin, 0, cos]]
            
            self.nodes[i] = np.matmul(node, rotationMatrixY)

    def displayCube(self):
        for node in self.nodes:
            self.pg.draw.circle(self.canvas, (0, 0, 0), (int(node[0]), int(node[1])), 4, 0)