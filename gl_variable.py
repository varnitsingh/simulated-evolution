import pygame
import random
import numpy as np
pygame.init()



landscape_area = np.zeros((10,10))
previousXpos=800
previousYpos=300

#########     Changeable variables       ############
maxCreatures = 5   #max creatures 39
food_count = 30
max_life_cycle = 1
maxMoveCount = 10

######       PY-Game variables   ###########
clock = pygame.time.Clock()
win = pygame.display.set_mode((1200,600))
run = True

######        COLORS     ###############
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)