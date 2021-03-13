import sys
import math
import pygame as pygame
import numpy as numpy
from cubeProj import *

pygame.init()

# Constants
WIDTH = 600
HEIGHT = 600
DEPTH = 600
CENTER_OFFSET = 100

# Colors
gray = (203, 203, 203)

running = True
while running:

    cubeProj = CubeProjection(WIDTH, HEIGHT, pygame)

    cube = Cube(WIDTH, HEIGHT, DEPTH, CENTER_OFFSET)
    cubeProj.addLayer(1, cube.generateVertices())
    cubeProj.display()

    # Check to see if the simulation has been exited
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update screen
    pygame.display.update()

# Done! Time to quit.
pygame.quit()