import pygame
import random
import numpy as np
pygame.init()



landscape_area = np.zeros((10,10))
previousXpos=700
previousYpos=500
countLifeForGraph=0
average=0

#########     Changeable variables       ############ maxcreature=10,foodcount=40,maxmovecount=20
maxCreatures = 10   #max creatures 39
food_count = 40
max_life_cycle = 1
maxMoveCount = 15

######       PY-Game variables   ###########
clock = pygame.time.Clock()
win = pygame.display.set_mode((1200,650))
run = True
font = pygame.font.SysFont(None,30)

######        COLORS     ###############
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)