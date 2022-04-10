import pygame
from pygame import Color
from pygame.locals import *
import pgzrun
import math
import random
import time
import sys

from Character import*
from Object import*
from Item import*
from Bubble import*
from Command import*

Width = 2400
Height = 1600
pi = math.pi
fps = 30
screensize = (Width, Height)
screenpos = (Width/2,Height/2)
sizerate = 0.6
start = False

def initialize_gameclient():
    #initialize and show the client side user interface
    global start,tick,screen,user_screen,wallpaper
    pygame.init()
    tick = pygame.time.get_ticks()
    screen = pygame.display.set_mode(screensize,HWSURFACE|DOUBLEBUF|RESIZABLE)
    user_screen = screen.copy()
    user_screen.fill(Color('white')) 
    pygame.display.set_caption('CUHK BIG BATTLE')
    wallpaper = (255,255,255)
    start = True

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'basic':
            initialize_gameclient()
        else:
            print('unknow game type')
            
while start:
    clock.tick(fps)#fps = 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            player_exit()
        elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode((int(screensize[0]*sizerate),
                                                 int(screensize[1]*sizerate)),
                                                 HWSURFACE|DOUBLEBUF|RESIZABLE)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = (int(event.pos[0]/sizerate),int(event.pos[1]/sizerate))
            mouse_down(pos)
        if event.type == pygame.MOUSEBUTTONUP:
            pos = (int(event.pos[0]/sizerate),int(event.pos[1]/sizerate))
            mouse_up(pos)
        if event.type == pygame.MOUSEMOTION:
            pos = (int(event.pos[0]/sizerate),int(event.pos[1]/sizerate))
            mouse_motion(pos)
        if event.type == pygame.KEYDOWN:
            key_down(event.key)
        if event.type == pygame.KEYUP:
            key_up()
            
        screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (Width/2,Height/2))   
        pygame.display.update()