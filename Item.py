import math
import pygame
from abc import ABCMeta
from abc import abstractmethod
from pygame.locals import *
from pygame.transform import*
from Basicfunctions import*
#from . import models
from Effectfunctions import*
from Serverdata import*

class item(pygame.sprite.Sprite):
    def __init__(self,name,user,pos):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.type = 'item'
        self.pos = [0,0]
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        self.user = user
        '''
        load data from database
        data = 
        '''
        data = itemlist[name]
        self.data = data
        self.duration = data['duration'] #flying time
        self.kb = data['kb'] #knockback amount
        self.damage = data['damage'] #attack damage
        self.effect = data['effect'] #effect on touch
        self.imagename = data['imagename']  #the corresponding image name of college
        self.removal = True#whether remove when collide
        self.kbrate = 0 #knockbackrate = 0 means items can not be knockbacked
        self.original_image = pygame.image.load(self.imagename).convert_alpha()#the original image file
        self.image = self.original_image
        self.rect = self.image.get_rect()
        servermap.items.add(self)   
        
    
    def update(self):
        if self.duration > 0:
            self.duration -=1
        elif self.duration == 0:
            self.remove()
        
    def collide(self,target):        
        if target.team != self.team:
            target.hurt(self.damage,self.user)
            
        if self.effect != None and target.type == 'character':
            #activate the touching effect
            function = eval(self.effect)
            function(self,target)
            
        if self.removal == True:
            self.remove()
        
    def display(self,Map):
        pass
        
    def remove(self):
        pygame.sprite.Sprite.kill(self)
        
class projectile(item):
    def __init__(self,name,user,pos,direction):
        item.__init__(self,name,user,pos)
        self.direction = direction
        self.spd = self.data['spd']
        self.angle = self.direction
        self.team = user.team#the character that shoot this, and its corresponding team
        #the angle of self.image, as projectile mat spin, it's not always equals to direcrion
        self.image = pygame.transform.rotate(self.original_image, self.direction)
        self.rect = self.image.get_rect()
        #rotate the image to the correct direction,and update the rectangle (pygame.transform)        
    
    def update(self):
        self.move()
        self.image = pygame.transform.rotate(self.original_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.duration -=1
        if self.duration > 0:
            self.duration -=1
        elif self.duration == 0:
            self.remove()
    
    def move(self):
        angle = self.direction* math.pi / 180.0
        self.pos[0] += self.spd * math.cos(angle)
        self.pos[1] -= self.spd  * math.sin(angle)
       

class melee(item):
    def __init__(self,name,user,pos,direction):
        item.__init__(self,name,user,pos)
        self.angle = direction
        self.pos = [0,0]
        self.pos[0] = self.user.pos[0]
        self.pos[1] = self.user.pos[1]
        self.team = user.team#the character that shoot this, and its corresponding team
        #the angle of self.image, as projectile mat spin, it's not always equals to direcrion
        self.direction = direction
        self.spd = self.data['spd']
        self.image = pygame.transform.rotate(self.original_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        #these value needs to be get from database
        #data = 
        self.initial_angle = self.spd*self.duration/2
        self.angle -= self.initial_angle
        self.hitlist = []#store the characters hit by this, a melee weapon could only hit each character once
        
    
    def update(self):
        self.move()
        if self.duration > 0:
            self.duration -=1
        if self.duration <= 0 or self.user.alive == False:
            self.remove()
        self.angle += self.spd
        self.pos = self.user.pos
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    def move(self):
        angle = self.direction* math.pi / 180.0
        self.pos[0] = self.user.pos[0]
        self.pos[1] = self.user.pos[1]
        
    def collide(self,target):
        #remember each character hit by this, they won't hit again.
        if target in self.hitlist:
            return
        else:
            self.hitlist.append(target)
        
        if target.team != self.team:
            target.hurt(self.damage,self.user)
            
        if self.effect != None:
            #activate the touching effect
            function = eval(self.effect)
            function(self,target)
            
        if self.removal == True:
            self.remove()
    

class area_effect(item):
    def __init__(self,name,user,pos):
        item._init__(self,name,user,pos)
        self.team = user.team#the character that shoot this, and its corresponding team
        #the angle of self.image, as projectile mat spin, it's not always equals to direcrion
        self.frequency = self.data['frequency'] #the interval between each trigger.0 indicates never trigger
        self.cd = self.frequency
        
    def update(self):
        #update the effect trigger interval
        self.cd -= 1
        if self.cd == 0:
            self.cd = self.frequency
        if self.duration > 0:
            self.duration -=1
        elif self.duration == 0:
            self.remove()
    
    def collide(self,target):
        if self.cd >0:
            #if the effect is in cooldown, return.
            return
        
        if target.team != self.team:
            target.hurt(self.damage,self.user)
            
        if self.effect != None and target.type == 'character':
            #activate the touching effect
            function = eval(self.effect)
            function(self,target)

    def move(self):
        if self.user is not None:
           self.pos[0] = self.user.pos[0]
           self.pos[1] = self.user.pos[1]
        