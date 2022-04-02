import math
import pygame
import basicfunctions
from abc import ABCMeta
from abc import abstractmethod
from pygame.locals import*
from pygame.transform import*

from Weapon import*
from Skill import*

class character(pygame.sprite.Sprite):
    def __init__(self,name,pos):
        #these value needs to be imported from database
        #data =
        self._name = name
        self._direction = 0#direction of move a number ranging from 0 to 360 indicate the angle
        self._facediraction = 0#the direction of its face, may not always equals to direction
        try:
            data = models.character.get(name = self._name)
            self._data = data
            self._imagename = data._imagename #the corresponding image name of college
            self._original_image = pygame.image.load(self.imagename).convert_alpha()#the original image file
            self._image = self._original_image
            self._rect = self._image.get_rect()#the rect of image
            self._spd = data._spd #speed
            self._kbrate = data._kbrate#knockbackrate
        except:
            print('this type of character does not exist')
        self._kb = 1# the knockback amount when collide with other character
        self._alive = True #whether is alive (able to be controled and interacted)
        self._move = False#indicate whether to move towards its direction
        
    def born(self,Map):
        #initialize this on the current game
        self._alive = True
        
    @abstractmethod
    def update(self):
        pass
    
    def direction(self,direction):#change the face direction
        self._direction = direction
        
    def move(self,direction):
        #give a direction and move towards iton the current Map
        angle = direction* math.pi / 180.0
        self._pos[0] += self._spd * math.cos(ang)
        self._pos[1] -= self._spd * math.sin(ang)
    
    def teleport(self,pos):
        #teleport to a position
        self._pos = pos
    
    def collide(self,target):
        #collide with a target, contiuesly knockback each one until their image do not cover each other
        angle = basicfunctions.get_angle(self,target)
        self.knockback (angle,10)
    
    def knockback(self,direction,kb_range):
        #knockback
        angle = direction* math.pi / 180.0
        kb_range /= self._kbrate
        self._pos[0] -= kb_range * math.cos(ang)
        self._pos[1] += kb_range * math.sin(ang)
    
    def hurt(self,damage):
        #take damage
        if self.alive == False:
            return
            # dead character won't hur or heal
        self._hp -= damage
        if self._hp < 0:
            self.death()
    
    def heal(self,healing):
        #receive healing
        if self.alive == False:
            return
            # dead character won't hur or heal
        self._hp += healing
        self._hp = math.max(self._hp,self.mhp)
            
    def death(self):
        #inactivated from current game
        self._alive = False
    
    def remove(self):
        #permantly remove this from the game
        pygame.sprite.kill(self)
    
    def display(self,Map):
        if self._activated:
            pass
        

class student(character):#the characters controlled by player
    def __init__(self,team,college,player):
        self._team = team
        self._player = player
        self._pos = [0,0]#current position[x,y]
        character.__init__(self,college,pos)
        self._weapon = self._data._weapon
        self._skill = self._data._skill #a cuple of ('name',cd, maxcd)
        self._maxhp = self._data._hp #max_health
        self._hp = self._maxhp #health
        self._alive = False #whether is alive (able to be controled and interacted)
        self._movecommand = [0,0,0,0]#the commands indicate move commands recieved[up,down,left,right\]
    
    def born(self,Map):
        #initialize this on the current game
        self._alive = True
        #reset weapon and skill
        self._weapon.reset()
        self._skill.reset()
        
    def useskill(self,skill):
        #use a skill,including basic attack
        if skill == 'attack':
            if self._weapon.attack == True:#successfully attack
                skill = self._weapon._action(self._pos,self._direction)
    
    def move_direction(self):
        if self._movecommand != [0,0,0,0]:
            cmd = self._movecommand
            self._direction = math.atan((cmd[0]-cmd[1])/(cmd[3]-cmd[2]))
    
    def update(self):
        #update the data
        if self._hp < 0:
            self.death()
        else:
            if self._move:
                self.move(self._direction)
            self._weapon.update()
            self._skill.update()
            self._image = pygame.transform.rotate(self._original_image, self._direction)
            self._rect = self._image.get_rect()
            self._player.update_position(self._pos)
    
    def death(self):
        #died and teleport to canteen,it will reborn at corresponding canteen later
        self._alive = False
        #functions that update scores

class cat(character):
    def __init__(self,pos):
        name = 'cat'
        character.__init__(self,name,pos)
        self._move = True
    
    def update(self):
        #have chance to change direction randomly
        if self._move:
            self.move(self._direction)

class bus(character):
    def __init__(self,pos,Game):
        name = 'bus'
        character.__init__(self,name,pos)
    
    def update(self):
        #change the direction along the bus line
        self.move(self._direction)
    
    def move(self,direction):
        #move along the bus line
        pass
