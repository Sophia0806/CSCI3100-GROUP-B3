import math
pi = math.pi
import pygame
from Basicfunctions import*

def get_angle(a,b):
    #get the angle from a.pos to b.pos,return the arc version of angle
    if b[0] -a[0] == 0:
        if b[1] > a[1]:
            return -pi/2
        else:
            return pi/2
        
    else:
        tan = -(b[1]-a[1])/(b[0]-a[0])
        if b[0]-a[0] > 0:
            return math.atan(tan)
        else:
            return math.atan(tan)+pi
        
    
        
    
def key_function(key):
    #only actived when game started(need update)
    if True: 
        #using wasd to move up,down,left or right
        if key == K_w :
            player.command('up')
        if key == K_a :
            player.command('left')
        if key == K_s :
            player.command('down')
        if key == K_d :
            player.command('right')
