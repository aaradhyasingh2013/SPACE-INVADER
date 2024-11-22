import math
import random
import pygame
SCREEN_WIDTH= 800
SCREEN_HIGHT= 500
PLAYER_START_X= 370
PLAYER_START_Y= 380
ENEMY_START_MIN= 50
ENEMY_START_MAX= 150
ENEMY_SPEED_X= 4
ENEMY_SPEED_Y= 40
BULLET_SPEED_Y= 10
COLLISION_DISTANCE= 27
pygame.init()
screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
background= pygame.image.load('space.png')
pygame.display.set_caption("space invader")
playerImg= pygame.image.load('fighterplane.png')
playerX= PLAYER_START_X
playerY= PLAYER_START_Y
playerX+change= 0
enemyImg=[]
enemyX=[]
enemyY=[]
ememyX_change=[]
enemyY_change=[]
num_of_enemies= 6



