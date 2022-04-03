import math
import pygame
from abc import ABCMeta
from abc import abstractmethod
from pygame.locals import *
from pygame.transform import*
from Basicfunctions import*
#from . import models
from Localdata import*
import Localdata

class item(pygame.sprite.Sprite):
    def __init__(self,name,pos):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.pos = [0,0]
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        #these value get from database
            #data = models.item.get(name = self.name)
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
        Localdata.local_game.map.items.add(self)   
        
    
    def update(self):
        self.duration -=1
        if self.duration <= 0:
            self.remove()
        
    def collide(self,target):
        if self.effect != None:
            #activate the touching effect
            pass
        if self.removal == True:
                self.remove()
        
    def display(self,Map):
        pass
        
    def remove(self):
        pygame.sprite.Sprite.kill(self)
        
class projectile(item):
    def __init__(self,name,user,pos,direction):
        item.__init__(self,name,pos)
        self.direction = direction
        self.spd = self.data['spd']
        self.angle = self.direction
        self.user = user
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
        if self.duration == 0:
            self.remove()
    
    def move(self):
        angle = self.direction* math.pi / 180.0
        self.pos[0] += self.spd * math.cos(angle)
        self.pos[1] -= self.spd  * math.sin(angle)
    
    def collide(self,target):
        if target.team != self.team:
            target.hurt(self.damage)
            #knockback the target if able
            if self.effect != None:
                #activate the touching effect
                pass
            if self.removal == True:
                self.remove()
       

class melee(item):
    def __init__(self,name,user,pos,direction):
        item.__init__(self,name,pos)
        self.angle = direction
        self.user = user
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
        
    
    def update(self):
        self.move()
        if self.duration <= 0 or self.user.alive == False:
            self.remove()
        self.angle += self.spd
        self.pos = self.user.pos
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.duration -=1
    
    def move(self):
        angle = self.direction* math.pi / 180.0
        self.pos[0] = self.user.pos[0]
        self.pos[1] = self.user.pos[1]
    
    def collide(self,target):
        if target.team != self.team:
            print(1)
            target.hurt(self.damage)
            #knockback the target if able
            if self.effect != None:
                #activate the touching effect
                pass
            if self.removal == True:
                self.remove()

class area_effect(item):
    def __init__(self,user,name,pos):
        item._init__(self,name,pos)
        self.user = user
        self.team = user.team#the character that shoot this, and its corresponding team
        #the angle of self.image, as projectile mat spin, it's not always equals to direcrion
        self.frequency = self.data['frequency'] #the interval between each trigger.0 indicates never trigger
    
    def collide(self,target):
        if target.team != self.team:
            target.hurt(self.damage)
            #knockback the target if able
            if self.effect != None:
                #activate the touching effect
                pass
            if self.removal == True:
                self.remove()
                
    def move(self):
        if self.user is not None:
           self.pos[0] = self.user.pos[0]
           self.pos[1] = self.user.pos[1]
        