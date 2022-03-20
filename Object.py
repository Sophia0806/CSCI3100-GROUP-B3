import math
import pygame
from pygame.transform import*

class game_object(pygame.sprite.Sprite):
    def __init__(self,name,pos):
        self._name = name
        self._pos = pos
        self._team = 'n'
        #these value get from data base
        #data = 
        self._maxhp = data._hp#-1 means unbreakable
        self._hp = self._maxhp
        self._duration = data._duration#-1 means last forever
        self._attribute = data._attribute
        self._imagename = data._image #the corresponding image name of college
        self._image = pygame.image.load(self.imagename).convert_alpha()
    
    def update(self):
        if self._duration > 0:
        # objects with negative duration last forever
            self._duration -=1
            if self._duration == 0:
                self.remove()          
    
    def hurt(self,damage):
        if self.maxhp <0:
            return #objects that maxhp <0 is unbreakable
        self.hp -= damage
        if self.hp < 0:
            self.death()
    
    def remove(self):
        pygame.sprite.kill(self)
    
    def display(self,Map):
        pass
        
class canteen(game_object):
    def __init__(self,name,pos,team):
        game_object.__init__(self,name,pos)
        self._team = team
