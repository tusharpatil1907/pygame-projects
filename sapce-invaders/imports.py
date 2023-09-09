import pygame
# from pygame import *
import random
import os
import time
# init fonts in pygame
pygame.font.init()


# bg image.# imitialize pygame window SIZE.
WIDTH,HEIGHT = 750,750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# IMPORT IMAGES IN PYGAME.
BG_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('assets','background-black.png')),(WIDTH,HEIGHT))

# image in game things
RED_SAPCESHIP = pygame.image.load(os.path.join('assets','pixel_ship_red_small.png'))
GREEN_SAPCESHIP = pygame.image.load(os.path.join('assets','pixel_ship_green_small.png'))
BLUE_SAPCESHIP = pygame.image.load(os.path.join('assets','pixel_ship_blue_small.png'))

# main spaceship
YELLOW_SAPCESHIP = pygame.image.load(os.path.join('assets','pixel_ship_blue_small.png'))

RED_LASER = pygame.image.load(os.path.join('assets',"pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join('assets',"pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join('assets',"pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join('assets',"pixel_laser_yellow.png"))
