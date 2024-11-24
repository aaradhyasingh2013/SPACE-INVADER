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
for _i in range(num_of_enemies):
    ennemyImg.append(pygame.image.load('crab.png'))
    enemyX.append(random.randit(0,SCREEN_WIDTH- 64))# 64
    enemyY.append(random.randit(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
bulletImg= pygame.image.load('bulet.png')
bulletX= 0
bulletY= PLAYER_START_Y
bulletX_change= BULLET_SPEED_Y
bullet_state= "ready"
score_value= 0
front= pygame.font.Font('freesansbold.ttf',32)
textX= 10
textY= 10



