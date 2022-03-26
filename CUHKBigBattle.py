import pygame
from pygame import Color
from pygame.locals import *
import pgzrun
import math
import random
import time
import sys

Width = 2400
Height = 1600
pi = math.pi
fps = 30
screensize = (Width, Height)
sizerate = 0.6

pygame.init()
t = pygame.time.get_ticks()
screen = pygame.display.set_mode(screensize,HWSURFACE|DOUBLEBUF|RESIZABLE)
fake_screen = screen.copy()
fake_screen.fill(Color('white')) 
pygame.display.set_caption('CUHK BIG BATTLe')
wallpaper = (255,255,255)

while True:
    clock.tick(fps)#fps = 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
            key_function(event.key)
        if event.type == pygame.KEYUP:
            key_up()
            
        fake_screen.fill(wallpaper)
        screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (0, 0))   
        pygame.display.update()