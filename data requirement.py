class character(pygame.sprite.Sprite):
    def __init__(self,name,pos):
        pygame.sprite.Sprite.__init__(self)
        #these data need input from database
        data = #the set of corresponding data 
        self.imagename = #the directory of image file
        self.spd =

class student(character)
    def __init__(self,college,team,player):
        self.weapon = 
        self.skill1 = 
        self.skill2 = 
        self.maxhp = 
        self.hp = self.maxhp 

class game_map:
    def __init__(self,name,gametype):
        data = 
        self.initial_obj =
        
class item(pygame.sprite.Sprite):
    def __init__(self,name,pos):
        data = 
        self.duration = 
        self.kb = 
        self.damage = 
        self.effect = 
        self.imagename =

class projectile(item):
    def __init__(self,name,user,pos,direction):
        self.spd = 

class melee(item):
    def __init__(self,name,user,pos,direction):
        self.spd =
        
class game_object(pygame.sprite.Sprite):
    def __init__(self,name,pos):
        data = 
        self._maxhp = 
        self._hp = self._maxhp
        self._duration = 
        self._attribute = 
        self._imagename =

class skill:
    def __init__(self,name):
        self.cd =
        
class weapon:
    def __init__(self,name):
        self.action =
        self.ammo =
        self.cd =
        self.reloadtime = 
        
class button(pygame.sprite.Sprite):
    def __init__(self,name,pos):
        self._imagename =

class bubble(pygame.sprite.Sprite):
    def __init__(self,pos,content_type,content,corresponding):
        self.duration = 
        self.imagename = 