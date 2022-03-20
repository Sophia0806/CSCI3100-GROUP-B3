import math
import pygame
from pygame.transform import*
class character(pygame.sprite.Sprite):
    def __init__(self,name,pos):
        #these value needs to be imported from database
        #data =
        self._name = name
        self._direction = 0#a number ranging from 0 to 360 indicate the angle
        self._imagename = data._imagename #the corresponding image name of college
        self._image = pygame.image.load(self.imagename).convert_alpha()
        self._spd = data._spd #speed
        self._kbrate = data._kbrate#knockbackrate
        self._kb = 1# the knockback amount when collide with other character
        self._alive = True #whether is alive (able to be controled and interacted)
        
    def born(self,Game):
        #initialize this on the current map
        self._alive = True
        game.characters.add(self)
        
    @abstractmethod
    def update(self):
        pass
    
    def direction(self,direction):#change the face direction
        self._direction = direction
        
    def move(self,direction):
        #give a direction and move towards iton the current Map
        angle = direction* math.pi / 180.0
        self._pos[0] += self._spd * math.cos(ang)
        self._pos[1] -= self._spd  * math.sin(ang)
    
    def teleport(self,pos)
        #teleport to a position
        self.pos = pos
    
    def collide(self,target):
        #collide with a target, contiues knockback each one until their image do not cover
        pass
    
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
    def __init__(self,team,college):
        self._team = team
        self._player = player
        self._pos = [0,0]#current position[x,y]
        character.__init__(self,college,pos)
        self._weapon = data._weapon
        self._skill = data._skill #a cuple of ('name',cd, maxcd)
        self._maxhp = data._hp #max_health
        self._hp = self._maxhp #health
        self._alive = False #whether is alive (able to be controled and interacted)
        
    def useskill(self,skill):
        #use a skill,including basic attack
        if skill == 'attack':
            if self._weapon.attack == True:#successfully attack
                skill = self._weapon._action(self._pos,self._direction)
    
    def update(self):
        #update the data
        if self._hp < 0:
            self.death()
        self._weapon.update()
        self._skill.update()
        rotate(self._image, self._direction)#rotate the image to the correct direction(pygame.transform)
    
    def death(self):
        #died and teleport to canteen,it will reborn at corresponding canteen later
        self._alive = False
        #functions that update scores

class cat(character):
    def __init__(self,pos):
        name = 'cat'
        character.__init__(self,name,pos)
        self.born(Game)
    
    def update(self):
        #have chance to change direction randomly
        self.move(self._direction)

class bus(character):
    def __init__(self,pos,Game):
        name = 'bus'
        character.__init__(self,name,pos)
        self.born(Game)
    
    def update(self):
        #change the direction along the bus line
        self.move(self._direction)
    
    def move(self,direction):
        #move along the bus line
        pass
