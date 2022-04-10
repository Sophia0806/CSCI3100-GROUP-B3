import pygame
from pygame import Color
from pygame.locals import *
import math
#this file is a temporary storage for local running game.
#we need to change its including into a database.

#the basic variables for local test,it will be different in online verison
local_player = None
local_game = None
start = False
enter = False
buttons = []

#the display setting
Width = 1200
Height = 900
fps = 30
sizerate = 1
wallpaper = (0,255,255)
screensize = (Width, Height)
screenpos = (Width/2,Height/2)
localscreen = pygame.display.set_mode((int(screensize[0]*sizerate),
                                                 int(screensize[1]*sizerate)),
                                                 HWSURFACE|DOUBLEBUF|RESIZABLE)
