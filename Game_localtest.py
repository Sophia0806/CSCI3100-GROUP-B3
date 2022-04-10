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
from Localdata import*
import Localdata

screen = localscreen.copy()

def initializegameclient(gametype):
    #initialize and show the client side user interface
    pygame.init()
    tick = pygame.time.get_ticks()
    pygame.display.set_caption('CUHK BIG BATTLE')
    Localdata.start = True
    initializelocal()

def initializelocal():
    initializebuttons()
    Localdata.local_game =game('basic')
    Localdata.local_player =player(1,'test')

def initializebuttons():
    for i in Localdata.buttonlist:
        button(i[0],i[1])
    
def printbuttons():
    for i in Localdata.buttons:
        localscreen.blit(i.image, i.rect)
        
def refresh_game():
    if Localdata.enter == False:
        printbuttons()
    else:
        
        Localdata.local_game.update()
        
initializegameclient('basic')

while Localdata.start:
    clock.tick(30)#fps = 60
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
        refresh_game()
        pygame.display.update()
        
        
