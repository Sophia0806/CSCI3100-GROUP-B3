import pygame
from pygame.transform import*
from Basicfunctions import*
#buttons only shown on client side game
#testonly
import Localdata
from Localdata import*
from Command import*

class button(pygame.sprite.Sprite):
    def __init__(self,name,pos):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.pos = pos
        
            #data = models.button.get(name = self.name)
        self.imagename = 'image/'+self.name+'.png' #the corresponding image name of college
        self.originalimage = pygame.image.load(self.imagename).convert_alpha()#the original image file
        self.image = self.originalimage
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        Localdata.buttons.append(self)

        
    def click(self):
        function = eval(self.name)
        join_game()
    
    def remove(self):
        pygame.sprite.Sprite.kill(self)