import math
import pygame
from pygame.transform import*
class bubble(pygame.sprite.Sprite):
    def __init__(self,pos,content_type,content,duration,corresponding):
        self._pos = pos
        self._type = content_type#text or imagename
        self._content = content
        self._duration = duration
        self._corresponding = corresponding
        # position corresponding to camera/map/character/objects)
        if self._type == 'text':
            pass
        if self._type == 'image':
            pass
    
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