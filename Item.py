import math
import pygame
from pygame.transform import*

class item(pygame.sprite.Sprite):
    def __init__(self,name,pos):
        self._name = name
        self._pos = pos
        #these value get from database
        #data = 
        self._duration = data._duration #flying time
        self._kb = data._kb#knockback amount
        self._damage = data._damage#attack damage
        self._effect = data._effect#effect on touch
        self._imagename = data._imagename #the corresponding image name of college
        self._image = pygame.image.load(self.imagename).convert_alpha()
        self._removal = data._removal#whether remove when collide
    
    def update(self):
        self._duration -=1
        if self._duration <= 0:
            self._remove
        
    def collide(self,target):
        if self._effect != None:
            #activate the touching effect
            pass
        
    def display(self,Map):
        pass
        
    def remove(self):
        pygame.sprite.kill(self)
        
class projectile(item):
    def __init__(self,name,pos,direction,user):
        item.__init__(self,name,pos)
        self._direction = direction
        self._angle = self._direction
        self._user = user
        self._team = user._team#the character that shoot this, and its corresponding team
        #the angle of self._image, as projectile mat spin, it's not always equals to direcrion
        rotate(self._image, self._direction)#rotate the image to the correct direction(pygame.transform)
        #these value needs to be get from database
        #data = 
        self._spd = data._spd
    
    def update(self):
        self.move()
        rotate(self._image, self._angle)#rotate the image to the correct direction(pygame.transform)
        self._duration -=1
        if self._duration == 0:
            self._remove
    
    def move(self):
        angle = self._direction* math.pi / 180.0
        self._pos[0] += self._spd * math.cos(ang)
        self._pos[1] -= self._spd  * math.sin(ang)
    
    def collide(self,target):
        if target.team != self.team:
            target.hurt(self._damage)
            #knockback the target if able
            if self._effect != None:
                #activate the touching effect
                pass
            if self.removal == True:
                self.remove()

class area_effect(item):
    def __init__(self,name,pos):
        item.__init__(self,name,pos)
        self._user = user
        self._team = user._team#the character that shoot this, and its corresponding team
        #the angle of self._image, as projectile mat spin, it's not always equals to direcrion
    
    def collide(self,target):
        if target.team != self.team:
            target.hurt(self._damage)
            #knockback the target if able
            if self._effect != None:
                #activate the touching effect
                pass
            if self.removal == True:
                self.remove()
        