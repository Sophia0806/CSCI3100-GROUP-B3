class game_map:
    def __init__(self,name,gametype):
        self._name = name
        self._type = gametype
        #these value needs to be imported from database
        #data = 
        self._objects = data.objects
        self._characters = pygame.sprite.Group()
        self._objects = pygame.sprite.Group()
        self._items = pygame.sprite.Group()
    
    def generate_objects(self):
        for i in self._objects:
            game_object(i.name,i.pos)
    
    def display(self):
        self.check_collision()
        #display background image
        for i in self._characters:
            if i._activate:
                i.display()
        for i in self._objects:
            i.display()            
        for i in self._items:
            i.display()
    
    def check_collision(self):
        #check_collision between characters,objects,and items, the active their collide function if able