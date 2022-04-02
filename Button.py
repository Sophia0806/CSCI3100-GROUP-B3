import pygame
from pygame.transform import*
from Basicfunctions import*
#buttons only shown on client side game

class button(pygame.sprite.Sprite):
    def __init__(self,name,pos):
        self.name = name
        self.pos = pos
        try:
            data = models.button.get(name = self._name)
            self._imagename = '/img/'+self.name+'/.png' #the corresponding image name of college
            self._original_image = pygame.image.load(self.imagename).convert_alpha()#the original image file
            self._image = self._original_image
            self._rect = self._image.get_rect()
            self._clickfunction = self.name
        except:
            print('this type of button does not exist')
        
    def click(self):
        return self.name
    
    def remove(self):
        pygame.sprite.kill(self)