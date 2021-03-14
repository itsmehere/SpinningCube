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
CENTER_OFFSET = 100

# Colors
gray = (203, 203, 203)

theta = 0

running = True
while running:

    # Create Cube
    cube = Cube(WIDTH, HEIGHT, DEPTH, pg)
    cube.generateVertices(CENTER_OFFSET)
    cube.displayCube()


    # Check to see if the simulation has been exited
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Update screen
    pg.display.update()

    # Increment angle
    theta += 0.01

cube.printNodes()

# Done! Time to quit.
pg.quit()