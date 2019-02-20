import pygame 
import random as rand
import sys
from pygame.locals import *
# draw snake body 
x = 15  
y = 15
def DRAW(x,y):
    pygame.draw.rect(displaySize,red,(x,y,15,15))
# check key input 
def KEY_INPUT(input_key):
    if input_key == 273:
        DRAW(x,y+1)
    if input_key == 274:
        DRAW(x,y-1) 
    if input_key == 275:
        DRAW(x+1,y) 
    if input_key == 276:
        DRAW(x-1,y)


pygame.init()

displaySize = pygame.display.set_mode((400,400))
red = (255,0,0)
#x = 100
#y = 200
#width = 100
#height = 100
pygame.display.set_caption('This is my first Snake game')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            KEY_INPUT(event.key)
            print(event.key)
    pygame.display.update()
        




