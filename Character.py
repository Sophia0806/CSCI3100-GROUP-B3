import math
import pygame
from Basicfunctions import*
from pygame.locals import*
from pygame.transform import*

from Weapon import*
from Skill import*
#test
import Localdata
from Localdata import*

class character(pygame.sprite.Sprite):
    def __init__(self,name,pos):
        pygame.sprite.Sprite.__init__(self)
        #these value needs to be imported from database
        #data =
        self.name = name
        self.direction = 0#direction of move a number ranging from 0 to 360 indicate the angle
        self.facediraction = 0#the direction of its face, may not always equals to direction
        self.conditions = []#the conditions list of it
            #data = models.character.get(name = self.name)
        data = characterlist[name]
        self.pos =pos
        self.data = data
        self.imagename = 'image/testman.png' #the corresponding image name of college
        self.originalimage = pygame.image.load(self.imagename).convert_alpha()#the original image file
        self.image = self.originalimage
        self.rect = self.image.get_rect()#the rect of image
        self.rect.center = self.pos
        self.spd = data['spd'] #speed
        self.kbrate = 1#knockbackrate
        self.kb = 1# the knockback amount when collide with other character
        self.alive = True #whether is alive (able to be controled and interacted)
        self.ismove = False#indicate whether to move towards its direction
        Localdata.local_game.map.characters.add(self)
        
    def born(self,Map):
        #initialize this on the current game
        self.alive = True
        
    def update(self):
        self.image = pygame.transform.rotate(self.originalimage, self.direction)
        for i in self.conditions:
            i['duration'] -=1
            if i['duration'] <= 0:
                self.conditions.remove(i)
    
    def direction(self,direction):#change the face direction
        self.direction = direction
        
    def move(self,movecommand):
        #give a direction and move towards iton the current Map
        
        self.pos[0] += self.spd * (movecommand[3]-movecommand[1])
        self.pos[1] += self.spd * (movecommand[2]-movecommand[0])
        self.rect.center = self.pos
        
    
    def teleport(self,pos):
        #teleport to a position
        self.pos = pos
    
    def collide(self,target):
        #collide with a target, contiuesly knockback each one until their image do not cover each other
        pass
    
    def knockback(self,direction,kbrange):
        #knockback
        angle = direction* math.pi / 180.0
        kbrange /= self.kbrate
        self.pos[0] -= kbrange * math.cos(angle)
        self.pos[1] += kbrange * math.sin(angle)
    
    def hurt(self,damage):
        #take damage
        if self.alive == False:
            return
            # dead character won't hur or heal
        self.hp -= damage
        if self.hp < 0:
            self.death()
    
    def heal(self,healing):
        #receive healing
        if self.alive == False:
            return
            # dead character won't hur or heal
        self.hp += healing
        self.hp = math.max(self.hp,self.mhp)
            
    def death(self):
        #inactivated from current game
        self.alive = False
    
    def addcondition(self,condition):
        #if already has the condition, update the duration, else add a new condition
        for i in self.conditions:
            if i['name'] == condition['name']:
                i['duration'] = Math.max(i['duration'],condition['duration'])
                return
        self.conditions.append(condition)
        
    def remove(self):
        #permantly remove this from the game
        pygame.sprite.Sprite.kill(self)
    
    
    def display(self,Map):
        if self.activated:
            pass
        

class student(character):#the characters controlled by player
    def __init__(self,college,team,player):
        self.team = team
        self.player = player
        self.pos = [0,0]#current position[x,y]
        character.__init__(self,college,self.pos)
        
        self.weapon = weapon(self.data['weapon'])
        self.skill1 = skill(self.data['skill1'])
        self.skill2 = skill(self.data['skill2'])#a cuple of ('name',cd, maxcd)
        self.maxhp = self.data['hp'] #maxhealth
        self.hp = self.maxhp #health
        self.alive = False #whether is alive (able to be controled and interacted)
        self.movecommand = [0,0,0,0]#the commands indicate move commands recieved[up,down,left,right\]
    
    def born(self):
        #initialize this on the current game
        self.alive = True
        #reset weapon and skill
        self.weapon.reset()
        self.skill1.reset()
        self.skill2.reset()
        
    def useskill(self,skill):
        #use a skill,including basic attack
        if skill == 'attack':
            if self.weapon.attack() == True:#successfully attack
                skill = self.weapon._action
            else:
                return
        skill.cast(self,self.pos,self.direction)

    
    def setdirection(self,direction):
        self.direction = direction
    
    def movetest(self):
        if self.movecommand != [0,0,0,0]:
            self.ismove = True
            self.move(self.movecommand)
        else:
            self.ismove = False
    
    def update(self):
        #update the data
        if self.hp < 0:
            self.death()
        else:
            self.movetest()
            self.weapon.update()
            self.skill1.update()
            self.skill2.update()
            self.image = pygame.transform.rotate(self.originalimage, self.direction)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
        #update conditions
        for i in self.conditions:
            i['duration'] -=1
            if i['duration'] <= 0:
                self.conditions.remove(i)
    
    def death(self):
        #died and teleport to canteen,it will reborn at corresponding canteen later
        self.alive = False
        #functions that update scores

class npc(character):
    def __init__(self,name,pos,direction,skill,team):
        character.__init__(self,name,pos)
        self.direction = direction#direction of move a number ranging from 0 to 360 indicate the angle
        self.facediraction = direction#the direction of its face, may not always equals to direction
        self.move = True
        self.skill = skill
        self.team = team
        self.skill.reset()
    
    def update(self):
        #in game, all npc with team will move towards the nearest opponent, updates per second
        if self.move:
            self.move(self.direction)
        if self.skill.cd == 0:
            self.skill
        if self.move:
            self.move(self.direction)
        

class bus(character):
    def __init__(self,pos,Game):
        name = 'bus'
        character.init(self,name,pos)
    
    def update(self):
        #change the direction along the bus line
        self.move(self.direction)
    
    def move(self,direction):
        #move along the bus line
        pass
