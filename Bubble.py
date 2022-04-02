import math
import pygame
from pygame.transform import*

class bubble(pygame.sprite.Sprite):
    def __init__(self,pos,content_type,content,duration,corresponding):
        self._pos = pos
        try:
            data = models.bubble.get(name = self._name)
            self._duration = data._duration
            self._imagename = data._imagename #the corresponding image name of college
            self._original_image = pygame.image.load(self.imagename).convert_alpha()#the original image file
            self._image = self._original_image
            self._corresponding = corresponding
            self._type = data._type#text or imagename
        except:
            print('this type of bubble does not exist')
        
        self._content = content
        # position corresponding to camera/map/character/objects)
    
    def update(self):
        if self._duration > 0:
        # bubbles with negative duration last forever
            self._duration -=1
            if self._duration == 0:
                self.remove()
                
    def remove(self):
        pygame.sprite.kill(self)
        
    def display(self,Map):
        pass