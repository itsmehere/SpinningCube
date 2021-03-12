class cubeProjection:
    def __init__(self, w, h, pg):
        self.width = w
        self.height = h
        self.screen = pg.display.set_mode((w, h))
        self.screen.fill((203, 203, 203))

        # List of cube nodes
        self.nodes = {}

        # Set pygame caption
        pg.display.set_caption('Analysis Project - 3D Spinning Cube')

    def addNode(self, i, node):
        self.nodes[i] = node