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

THETA_INCREMENT_X = 0.0015
THETA_INCREMENT_Y = 0.0015
THETA_INCREMENT_Z = 0.0015

def main():

    # Create Canvas
    canvas = pg.display.set_mode((WIDTH, HEIGHT))
    canvas.fill((0, 0, 0))
    pg.display.set_caption('Analysis Project - 3D Spinning Cube')

    # Create Cube
    cube = Cube(WIDTH, HEIGHT, DEPTH, pg, canvas)
    cube.generatePoints(CENTER_OFFSET)

    running = True
    
    while running:

        # Apply transformation and display it
        cube.createCompositeMatrix(THETA_INCREMENT_X, THETA_INCREMENT_Y, THETA_INCREMENT_Z)
        cube.applyTransformation()
        cube.displayCube()

        # Check to see if the simulation has been exited
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        pg.display.update()

    pg.quit()


if __name__ == "__main__":
    main()