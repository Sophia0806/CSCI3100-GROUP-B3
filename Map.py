from Basicfunctions import*
from Character import*
from Object import*
from Item import*
from Bubble import*
#this is the server map
from Serverdata import*

class game_map:
    def __init__(self,name,gametype):
        self.name = name
        self.type = gametype

        data = models.map.objects.get(key=name) 
        self.initial_obj = data.objects
        
        #the initial set of objects
        self.characters = pygame.sprite.Group()
        self.objects = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.bubbles = pygame.sprite.Group()
    
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
            if i.type == 'npc':
                self.update_npc(i)
        for i in self.items:
            i.update()
        for i in self.bubbles:
            i.update()       
    
    def update_npc(self,npc):
        #mpc without team move randomly
        if npc.team == 'n':
            return
        #npc with team turn to its nearest opponent
        elif npc.team == 'a':
            opponent = 'b'            
        elif inpc.team == 'b':
            opponent = 'a'
        
        mindist = npc.seerange
        target = None
        #search for nearest alive opponent within its seerange
        for i in self.characters:
            if i.alive == True and i.team == opponent:
                dist = get_distance(npc,i)
                if dist < mindist:
                    mindist = dist
                    target = i
        #turn its direction to the opponent
        if target != None:
            direction = get_angle(a,b)
            npc.direction = direction
        
    
    def display(self):
        #display background image
        for i in self.objects:
            screen.blit(i.image, i.rect)            
        for i in self.items:
            screen.blit(i.image, i.rect)
        for i in self.bubbles:
            screen.blit(i.image, i.rect)
        for i in self.characters:
            if i.alive:
                screen.blit(i.image, i.rect)
        '''
        this is the method that update the screen file in the database
        '''
             
    def check_collision(self):
    #check_collision between characters and other characters,objects,and items,and between items and objects
    #they active their collide function if able
    #test rect collision first then mask to save the calculating time
        for i in self.characters:    
            for j in self.objects:
                if pygame.Rect.colliderect(i.rect,j.rect):
                    if pygame.sprite.collide_mask(i,j):
                        i.collide(j)
                        j.collide(i)
                    
            for j in self.items:
                if pygame.Rect.colliderect(i.rect,j.rect):
                    if pygame.sprite.collide_mask(i,j):
                        i.collide(j)
                        j.collide(i)
                    
            for j in self.characters:
                if j is not i and pygame.Rect.colliderect(i.rect,j.rect):
                    if pygame.sprite.collide_mask(i,j):
                        i.collide(j)
                        j.collide(i)
        
        for i in self.items:               
            for j in self.objects:
                if pygame.Rect.colliderect(i.rect,j.rect):
                    if pygame.sprite.collide_mask(i,j):
                        i.collide(j)
                        j.collide(i)

                