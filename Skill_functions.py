from Item import*
from Localdata import*

def cc_left(user,pos,direction):
    melee('cc_hammer',user,pos,direction)
    
def cc_right(user,pos,direction):
    melee('cc_shield',user,pos,direction)

def cc_super(user,pos,direction):
    area_effect('feast',user,pos,direction)

def na_left(user,pos,direction):
    melee('na_pen',user,pos,direction)
    projectile('na_ink',user,pos,direction-14)
    projectile('na_ink',user,pos,direction-7)
    projectile('na_ink',user,pos,direction)
    projectile('na_ink',user,pos,direction+7)
    projectile('na_ink',user,pos,direction-14)
    
def na_right(user,pos,direction):
    area_effect('clock',user,pos,direction)

def na_super(user,pos,direction):
    user.hp = user.mhp
    condition = {'name':'na_super','duration':180}
    user.add_condition(condition)  

def uc_left(user,pos,direction):
    projectile('uc',user,pos,direction)
def uc_right(user,pos,direction):
    area_effect('uc_grass',user,pos,direction) 
def uc_super(user,pos,direction):
    area_effect('uc_pond',user,pos,direction) 
    

def shaw_left(user,pos,direction):
    melee('shaw_basic',user,pos,direction)
    
def shaw_right(user,pos,direction):
    condition = {'name':'shaw_down','duration':120}
    user.add_condition(condition)
    
def shaw_super(user,pos,direction):
    skill = skill('shaw_snake')
    npc('snake',user,pos,direction,skill,user._team)
    

def ws_left(user,pos,direction):
    area_effect('ws_basic',user,pos,direction)
    
def ws_right(user,pos,direction):
    condition = {'name':'fridge','duration':60}
    user.add_condition(condition)
    
def ws_super(user,pos,direction):
    projectile('ws_super',user,pos,direction)
    #when it lands, generate a ice-cream that give buff whenpick

def wys_left(user,pos,direction):
    projectile('wys_basic',user,pos,direction)

def wys_right(user,pos,direction):
    area_effect('wys_super',user,pos,direction)
    
def wys_super(user,pos,direction):
    user.hp = user.maxhp*2
    condition = {'name':'wys_mecha','duration':1200}
    user.add_condition(condition)   

def shho_left(user,pos,direction):
    projectile('shho_basic',user,pos,direction)
    #when it lands, generate a heart that heals whenpick
    
def shho_right(user,pos,direction):
    area_effect('shho_right',user,pos,direction)

def shho_super(user,pos,direction):
    area_effect('shho_can',user,pos,user.team)
    

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
    

    