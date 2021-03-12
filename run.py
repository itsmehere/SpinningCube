import sys
import math
import pygame as pygame
from cubeProj import cubeProjection

pygame.init()

# Colors
gray = (203, 203, 203)

running = True
while running:

    cubeProj = cubeProjection(500, 500, pygame)

    # Check to see if the simulation has been exited
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update screen
    pygame.display.update()

# Done! Time to quit.
pygame.quit()