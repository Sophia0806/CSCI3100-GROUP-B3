import pygame
from pygame import Color
from pygame.locals import *
import pgzrun
import math
import random
import time
import sys

from Game import*
from Player import*
from Character import*
from Object import*
from Item import*
from Bubble import*
from Button import*
from Command import*
import Serverdata
from Serverdata import*
big_interval = 30
clock = big_interval
#the interval of per big update is 1 sec, game only upate part of data in normal update to save time.

def initializegame(gametype):
    #initialize and show the client side user interface
    pygame.init()
    tick = pygame.time.get_ticks()
    pygame.display.set_caption('CUHK BIG BATTLE')
    Serverdata.currentgame = game(gametype)
    currentgame = Serverdata.currentgame
        
def update_game():
    clock-=1
    currentgame.update()
    if clock < 0:
        clock = big_interval
        currentgame.big_update()
            
initializegame('basic')

while currentgame is not None:
    clock.tick(30)#fps = 30
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            playerexit()
        elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode((int(screensize[0]*sizerate),
                                                 int(screensize[1]*sizerate)),
                                                 HWSURFACE|DOUBLEBUF|RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = (int(event.pos[0]/sizerate),int(event.pos[1]/sizerate))
            mouse_down(pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = (int(event.pos[0]/sizerate),int(event.pos[1]/sizerate))
            mouse_up(pos)
        elif event.type == pygame.MOUSEMOTION:
            pos = (int(event.pos[0]/sizerate),int(event.pos[1]/sizerate))
            mouse_motion(pos)
        elif event.type == pygame.KEYDOWN:
            key_down(event.key)
        elif event.type == pygame.KEYUP:
            key_up(event.key)
            
        screen.fill(wallpaper)
        screen.blit(pygame.transform.scale(localscreen , localscreen.get_rect().size), (0,0))
        update_game()
        pygame.display.update()
        
        
