import math
import pygame
from pygame.locals import*
from pygame.transform import*
#test
from Localdata import*
pygame.font.init()
f = pygame.font.Font('Tahoma.ttf',32)

class bubble(pygame.sprite.Sprite):
    def __init__(self,name,pos,corresponding):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        '''
        load data from database
        data = 
        '''
        self.duration = data.duration
        self.imagename = data.imagename #the corresponding image name of college
        self.originalimage = pygame.image.load(self.imagename).convert_alpha()#the original image file
        self.rect = self.image.get_rect()#the rect of image
        self.rect.center = self.pos#the rect of image
        self.image = self.originalimage
        selfcorresponding = corresponding#None, or a player's screen        
        if self.corresponding is not None:
            self.corresponding.bubbles.add(self)
        else:
            servermap.bubbles.add(self)   
    
    def update(self):
        if selfduration > 0:
        # bubbles with negative duration last forever
            selfduration -=1
            if selfduration == 0:
                self.remove()
                
    def remove(self):
        pygame.sprite.Sprite.kill(self)

class name_text(pygame.sprite.Sprite):
    #the nametexts show on characters
    def __init__(self,corresponding,content):   
        self.corresponding = corresponding#a character's figure
        self.image = f.render(content,True,(0,0,0))
        self.rect =self.content.get_rect
        self.pos = [0,0]
        self.pos[0] = self.corresponding.pos[0]
        self.pos[1] = self.corresponding.pos[1]-100
        self.rect.center = self.pos
        servermap.bubbles.add(self)
        
    def update(self):
        if self.corresponding.alive is False:
            self.remove()
        self.pos[0] = self.corresponding.pos[0]
        self.pos[1] = self.corresponding.pos[1]-100
        if selfduration > 0:
        # bubbles with negative duration last forever
            selfduration -=1
            if selfduration == 0:
                self.remove()
                
    def remove(self):
        pygame.sprite.Sprite.kill(self)