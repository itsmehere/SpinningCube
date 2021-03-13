import numpy as numpy

class CubeProjection:
    def __init__(self, w, h, pg):
        self.width = w
        self.height = h
        self.pg = pg
        self.screen = pg.display.set_mode((w, h))
        self.layers = {}

        # Set pygame caption
        pg.display.set_caption('Analysis Project - 3D Spinning Cube')

    def addLayer(self, id, points):
        self.layers[1] = points

    def display(self):
        self.screen.fill((203, 203, 203))

        for layer in self.layers.values():
            for node in layer:
                self.pg.draw.circle(self.screen, (0, 0, 0), (int(node[0]), int(node[1])), 4, 0)

class Cube:
    def __init__(self, w, h, d, o):
        self.w = w
        self.h = h
        self.d = d
        self.o = o
        
        # List of cube nodes
        self.nodes = numpy.zeros((0,4))

    def generateVertices(self):
        minX = (self.w / 2) - self.o
        maxX = (self.w / 2) + self.o

        minY = (self.h / 2) + self.o
        maxY = (self.h / 2) - self.o

        minZ = (self.d / 2) - self.o
        maxZ = (self.d / 2) + self.o

        # Create cube vertices
        return numpy.array([(x, y, z) for x in (minX, maxX) for y in (minY, minX) for z in (minZ, maxZ)])