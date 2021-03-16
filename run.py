import sys
import math
import pygame as pg
import numpy as np
from cubeProj import *

pg.init()

# Constants
WIDTH = 600
HEIGHT = 600
DEPTH = 600
CENTER_OFFSET = 50

def main():

    theta = 0.1
    running = True

    while running:
        # Create Cube
        cube = Cube(WIDTH, HEIGHT, DEPTH, pg)

        # Create the points that form the cube
        cube.generateVertices(CENTER_OFFSET)
        cube.generateEdges(CENTER_OFFSET)

        # Create the transformation, apply it, and display it on the canvas
        cube.createCompositeMatrix(theta)
        cube.applyTransformation()
        cube.displayCube()
        

        # Check to see if the simulation has been exited
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Update screen
        pg.display.update()

        # Increment angle
        theta += 0.005

    # Done! Time to quit.
    pg.quit()


if __name__ == "__main__":
    main()