from Basicfunctions import*
from Character import*
from Object import*
from Item import*
from Bubble import*
#this is the server map
#from . import models

class game_map:
    def __init__(self,name,gametype):
        self._name = name
        self._type = gametype
        #these value get from database
        try:
            data = models.map.get(name = self._name)
            self._initial_obj = data.objects
        except:
            print('this type of map does not exist')
        #the initial set of objects
        self._characters = pygame.sprite.Group()
        self._objects = pygame.sprite.Group()
        self._items = pygame.sprite.Group()
    
    def generate_objects(self):
        for i in self._initial_obj:
            new_obj = game_object(i.name,i.pos)
            self.addobj(new_obj)
    
    def addobj(self,obj):
        #add objects into the map
        self._objects.add(obj)
    
    def addcharacter(self,c):
        #add character intp the map
        self._characters.add(c)
    
    def additem(self,i):
        #add item into the map
        self._items.add(i)
    
    def update(self):
        self.check_collision()
        for i in self._objects:
            i.update()
        for i in self._characters:
            i.update()
        for i in self._items:
            i.update()        
    
    def display(self):
        #display background image
        for i in self._characters:
            if i._activate:
                i.display()
        for i in self._objects:
            i.display()            
        for i in self._items:
            i.display()
    
    def check_collision(self):
    #check_collision between characters and other characters,objects,and items,and between items and objects
    #they active their collide function if able
        for i in self._characters:
            for j in self._characters:
                while pygame.sprite.collide_mask(i,j):
                    i.collide(j)
                    j.collide(i)
                
            for j in self._objects:
                while pygame.sprite.collide_mask(i,j):
                    i.collide(j)
                    j.collide(i)
                    
            for j in self._items:
                while pygame.sprite.collide_mask(i,j):
                    i.collide(j)
                    j.collide(i)
        
        for i in self._items:               
            for j in self._objects:
                f pygame.sprite.collide_mask(i,j):
                    i.collide(j)
                    j.collide(i)

                