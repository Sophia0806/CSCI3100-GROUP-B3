from Basicfunctions import*
from Character import*
from Object import*
from Item import*
from Bubble import*
#this is the server map
#from . import models
#test
from Localdata import*

class game_map:
    def __init__(self,name,gametype):
        self.name = name
        self.type = gametype
        #these value get from database
        
            #data = models.map.get(name = self.name)
        data = maplist[self.name]
        self.initial_obj = data['objects']
        
        #the initial set of objects
        self.characters = pygame.sprite.Group()
        self.objects = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
    
    def generate_objects(self):
        for i in self.initial_obj:
            new_obj = game_object(i.name,i.pos)
            self.addobj(new_obj)
    
    def addobj(self,obj):
        #add objects into the map
        self.objects.add(obj)
    
    def addcharacter(self,c):
        #add character intp the map
        self.characters.add(c)
    
    def additem(self,i):
        #add item into the map
        self.items.add(i)
    
    def update(self):
        #self.check_collision()
        for i in self.objects:
            i.update()
        for i in self.characters:
            i.update()
        for i in self.items:
            i.update()        
    
    def display(self):
        #display background image
        for i in self.objects:
            localscreen.blit(i.image, i.rect)            
        for i in self.items:
            localscreen.blit(i.image, i.rect)
        for i in self.characters:
            if i.alive:
                localscreen.blit(i.image, i.rect)
             
    def check_collision(self):
    #check_collision between characters and other characters,objects,and items,and between items and objects
    #they active their collide function if able
        for i in self.characters:
                
            for j in self.objects:
                if pygame.sprite.collide_mask(i,j):
                    i.collide(j)
                    j.collide(i)
                    
            for j in self.items:
                if pygame.sprite.collide_mask(i,j):
                    i.collide(j)
                    j.collide(i)
                    
            for j in self.characters:
                if j is not i and pygame.sprite.collide_mask(i,j):
                    i.collide(j)
                    j.collide(i)
        
        for i in self.items:               
            for j in self.objects:
                if pygame.sprite.collide_mask(i,j):
                    i.collide(j)
                    j.collide(i)

                