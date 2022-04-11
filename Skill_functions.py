import random
from Item import*
from Localdata import*

def cc_left(user,pos,direction):
    melee('hammer',user,pos,direction)
    
def cc_right(user,pos,direction):
    area_effect('bell_aoe',user,pos,direction)

def cc_super(user,pos,direction):
    for x in [-350,0,350]:
        for y  in [-350,0,350]:
             fpos = [pos[0]+x,pos[1]+y]
             item('food',user,fpos,0)

def na_left(user,pos,direction):
    melee('brush',user,pos,direction)
    projectile('ink',user,pos,direction-14)
    projectile('ink',user,pos,direction-7)
    projectile('ink',user,pos,direction)
    projectile('ink',user,pos,direction+7)
    projectile('ink',user,pos,direction-14)
    
def na_right(user,pos,direction):
    area_effect('clock',user,pos,direction)

def na_super(user,pos,direction):
    user.hp = user.mhp
    condition = {'name':'na_super','duration':180}
    user.add_condition(condition)  

def uc_left(user,pos,direction):
    projectile('boomerang’',user,pos,direction)
def uc_right(user,pos,direction):
    projectile('frog',user,pos,direction) 
def uc_super(user,pos,direction):
    area_effect('grass',user,pos,direction)  
    

def shaw_left(user,pos,direction):
    melee('womanfoot',user,pos,direction)
    
def shaw_right(user,pos,direction):
    condition = {'name':'shaw_down','duration':120}
    user.add_condition(condition)
    
def shaw_super(user,pos,direction):
    skill = 'shaw_left'
    npc('SHAW_snake',user,0,direction,skill,user._team)    

def ws_left(user,pos,direction):
    area_effect('wsbeat',user,pos,direction)
    
def ws_right(user,pos,direction):
    condition = {'name':'fridge','duration':60}
    user.add_condition(condition)
    
def ws_super(user,pos,direction):
    projectile('dessertbullet',user,pos,direction)
    #when it lands, generate a ice-cream that give buff whenpick

def wys_left(user,pos,direction):
    projectile('card',user,pos,direction)

def wys_right(user,pos,direction):
    area_effect('wys_movie',user,pos,direction)
    
def wys_super(user,pos,direction):
    user.hp = user.maxhp*2
    condition = {'name':'wys_mecha','duration':1200}
    user.add_condition(condition)   

def shho_left(user,pos,direction):
    projectile('heartbullet',user,pos,direction)
    #when it lands, generate a heart that heals whenpick
    
def shho_right(user,pos,direction):
    for x in [-200,0,200]:
        for y  in [-200,0,200]:
             fpos = [pos[0]+x,pos[1]+y]
             item('heart',user,fpos,0)

def shho_super(user,pos,direction):
    npc('SHHO_sculpture',user,pos,0,'sculpture_heart',user._team)

def sculpture_heart(user,pos,direction):
    rset = [-200,200]
    x = random.choice(rset)
    y = random.choice(rset)
    fpos = [pos[0]+x,pos[1]+y]
    item('heart',user,fpos,0)

def mc_left(user,pos,direction):
    melee('moring_star',user,pos,direction)
def mc_right(user,pos,direction):
    pass
def mc_super(user,pos,direction):
    pass
    
def cw_left(user,pos,direction):
    projectile('cw_basic',user,pos,direction)
def cw_right(user,pos,direction):
    condition = {'name':'bicycle','duration':120}
    user.add_condition(condition)
def cw_super(user,pos,direction):
    pass
    

    