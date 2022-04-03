import math
import pygame
from pygame.transform import*
#test
from Localdata import*
class bubble(pygame.sprite.Sprite):
    def __init__(self,pos,content_type,content,duration,corresponding):
        pygame.sprite.Sprite.__init__(self)
        selfpos = pos
        try:
            #data = models.bubble.get(name = selfname)
            self.duration = data.duration
            self.imagename = data.imagename #the corresponding image name of college
            selforiginalimage = pygame.image.load(self.imagename).convert_alpha()#the original image file
            self.image = selforiginalimage
            selfcorresponding = corresponding
            selftype = datatype#text or imagename
        except:
            print('this type of bubble does not exist')
        
        selfcontent = content
        # position corresponding to camera/map/character/objects)
    
    def update(self):
        if selfduration > 0:
        # bubbles with negative duration last forever
            selfduration -=1
            if selfduration == 0:
                self.remove()
                
    def remove(self):
        pygame.sprite.Sprite.kill(self)
        
    def display(self,Map):
        pass