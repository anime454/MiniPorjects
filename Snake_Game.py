import pygame 
import random as rand
import sys
from pygame.locals import *

pygame.init()

displaySize = pygame.display.set_mode((400,400))

pygame.display.set_caption('This is my first Snake game')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
        
