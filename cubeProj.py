import numpy as np
import copy as cp
import math

class Cube:
    def __init__(self, width, height, depth, pg, canvas):
        self.w = width
        self.h = height
        self.d = depth
        self.pg = pg
        self.canvas = canvas
        self.nodes = []
        self.compositeMatrix = ""
    

    def addPoint(self, point):
        point = np.append(point, 1)
        self.nodes.append(point)


    def generatePoints(self, CENTER_OFFSET):
        # Generate the vertices of the cube
        minX = (self.w / 2) - CENTER_OFFSET
        maxX = (self.w / 2) + CENTER_OFFSET

        minY = (self.h / 2) + CENTER_OFFSET
        maxY = (self.h / 2) - CENTER_OFFSET

        minZ = (self.d / 2) - CENTER_OFFSET
        maxZ = (self.d / 2) + CENTER_OFFSET

        # Create cube vertices
        vertices = np.array([(x, y, z) for x in (minX, maxX) for y in (minY, maxY) for z in (minZ, maxZ)])

        for vertex in vertices:
            self.addPoint(vertex)

        # Generate the  edges of the cube
        edgeDensity = 15

        # Z Axis Edges
        for i in range(0, len(vertices) - 1, 2):
            Zpts = self.pointsBetween(vertices[i], vertices[i + 1], edgeDensity)
            
            for point in Zpts:
                self.addPoint(point)

        # Y Axis Edges
        for i in range(0, int(len(vertices) / 2)):
            Ypts = self.pointsBetween(vertices[i], vertices[i + 4], edgeDensity)
            
            for point in Ypts:
                self.addPoint(point)

        # X Axis Edges
        Xpts = self.pointsBetween(vertices[0], vertices[2], edgeDensity)
        Xpts.extend(self.pointsBetween(vertices[1], vertices[3], edgeDensity))
        Xpts.extend(self.pointsBetween(vertices[4], vertices[6], edgeDensity))
        Xpts.extend(self.pointsBetween(vertices[5], vertices[7], edgeDensity))
            
        for point in Xpts:
            self.addPoint(point)

    
    def pointsBetween(self, p1, p2, density):
        vector = p2 - p1
        vector = vector / density

        ptsBtn = []
        currentPt = p1

        while True:
            currentPt = currentPt + vector

            if str(currentPt) != str(p2):
                ptsBtn.append(currentPt)
            else:
                break

        return ptsBtn


    def distBetween(self, p1, p2):
        squaredDist = (p2[0] - p1[0]) ** 2 +  (p2[1] - p1[1]) ** 2 +  (p2[2] - p1[2]) ** 2
        return math.sqrt(squaredDist)


    def createCompositeMatrix(self, theta_x, theta_y, theta_z):
        cos_x = np.cos(theta_x)
        sin_x = np.sin(theta_x)

        cos_y = np.cos(theta_y)
        sin_y = np.sin(theta_y)

        cos_z = np.cos(theta_z)
        sin_z = np.sin(theta_z)

        x = -1 * self.w / 2
        y = -1 * self.h / 2
        z = -1 * self.d / 2

        translationMatrix1 = [[1, 0, 0, x],
                              [0, 1, 0, y],
                              [0, 0, 1, z],
                              [0, 0, 0, 1]]

        rotationMatrixX = [[1, 0, 0, 0],
                           [0, cos_x, -sin_x, 0],
                           [0, sin_x, cos_x, 0],
                           [0, 0, 0, 1]]

        rotationMatrixY = [[cos_y, 0, sin_y, 0],
                           [0, 1, 0, 0],
                           [-sin_y, 0, cos_y, 0],
                           [0, 0, 0, 1]]

        rotationMatrixZ = [[cos_z, -sin_z, 0, 0],
                           [sin_z, cos_z, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]]

        translationMatrix2 = [[1, 0, 0, -x],
                              [0, 1, 0, -y],
                              [0, 0, 1, -z],
                              [0, 0, 0, 1]]

        transformations = [translationMatrix2, rotationMatrixX, rotationMatrixY, rotationMatrixZ, translationMatrix1]
        self.compositeMatrix = transformations[0]

        for i in range(1, len(transformations)):
            self.compositeMatrix = np.matmul(self.compositeMatrix, transformations[i])


    def applyTransformation(self):
        for i in range(0, len(self.nodes)):
            self.nodes[i] = np.matmul(self.compositeMatrix, self.nodes[i])


    def displayCube(self):
        # Clear screen to show next set of points
        self.canvas.fill((0, 0, 0))

        for node in self.nodes:
            self.pg.draw.circle(self.canvas, (255, 255, 255), (int(node[0]), int(node[1])), 2, 0)