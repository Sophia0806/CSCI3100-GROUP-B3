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
        
def get_distance(a,b):
    return math.sqrt((b.pos[1]-a.pos[1])*(b.pos[1]-a.pos[1]) + (b.pos[0]-a.pos[0])*(b.pos[0]-a.pos[0]))

def defeat_enemy(player):
    player.add_score(100)

def deal_damage(player,amount):
    player.add_score(amount)

def heal_ally(player,amount):
    player.add_score(amount)
    
def initialize_canteen():
    area_effect('cantenn_a',None,())
    area_effect('cantenn_b',None,())
    
