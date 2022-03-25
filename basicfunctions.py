import math
import pygame
pi = math.pi

def get_angle(a,b):
    #get the angle from a.pos to b.pos,return the arc version of angle
    if b._pos[0] -a.pos[0] == 0:
        if b._pos[1] > a.pos[1]:
            return pi/2
        else:
            return -pi/2
        
    else:
        tan = (b._pos[1]-a.pos[1])/(b.pos[0]-a.pos[0])
        return math.atan(tan)