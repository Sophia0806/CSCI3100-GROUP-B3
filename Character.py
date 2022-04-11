import math
import pygame
from Basicfunctions import*
from pygame.locals import*
from pygame.transform import*

from Weapon import*
from Skill import*
#test
from Serverdata import*

class character(pygame.sprite.Sprite):
    def __init__(self,name,pos):
        pygame.sprite.Sprite.__init__(self)
        #these value needs to be imported from database
        #data =
        self.name = name
        self.type = 'character'
        self.direction = 0#direction of face from 0 to 360 indicate the angle
        self.conditions = []#the conditions list of it
        '''
        load data from database
        data = 
        '''
        data = data = models.character.objects.get(key=name)
        self.pos =pos
        self.data = data
        self.imagename = data.image #the corresponding image name of college
        self.originalimage = pygame.image.load(self.imagename).convert_alpha()#the original image file
        self.image = self.originalimage
        self.rect = self.image.get_rect()#the rect of image
        self.rect.center = self.pos
        self.spd = data.spd #speed
        self.kbrate = 1#knockbackrate
        self.kb = 1# the knockback amount when collide with other character
        self.alive = True #whether is alive (able to be controled and interacted)
        self.canmove = True#indicate whether to move towards its direction
        self.canattack = True#indicate whether to move towards its direction
        servermap.characters.add(self)
        
    def born(self,Map):
        #initialize this on the current game
        self.alive = True
        
    def update(self):
        self.canmove = True
        self.canattack = True
        for i in self.conditions:
            if i['name'] == 'fridge':
                i.hp+=2 #heal 2hp per 1/30 sec
            if i['name'] == 'pause' or i['name'] == 'fridge':
                #can't move and attack conditions
                self.canmove = False
                self.canattack = False   
            if i['name'] == 'shaw_down' or i['name'] == 'na_super':
                #can't attack conditions
                self.canattack = False
            if i['name'] == 'shaw_down'or i['name'] == 'na_super'or i['name'] == 'fridge'or i['name'] == 'wys_super':
                #at these conditions, character have new image
                self.imagename = self.imagename.rstirp('.png')
                self.imagename += '_1.png'
                self.originalimage = pygame.image.load(self.imagename).convert_alpha()
                self.image = self.originalimage
                self.rect = self.image.get_rect()#the rect of image
                self.rect.center = self.pos
                
            #update the condition
            i['duration'] -=1
            if i['duration'] <= 0:
                self.conditions.remove(i)
                if i['name'] == 'shaw_down'or i['name'] == 'na_super'or i['name'] == 'fridge'or i['name'] == 'wys_super':
                    self.imagename = self.imagename.rstirp('_1.png')
                    self.imagename += '.png'
                    self.originalimage = pygame.image.load(self.imagename).convert_alpha()#the original image file
                    self.image = self.originalimage
                    self.rect = self.image.get_rect()#the rect of image
                    self.rect.center = self.pos
    
    def direction(self,direction):#change the face direction
        self.direction = direction
        
    def move(self,movecommand):
        #give a direction and move towards iton the current Map
        spd = self.spd
        for i in self.conditions:
            if i['name'] == 'slow':
                spd = int(self.spd/2)
            elif i['name'] == 'accelerated' or i['name'] == 'wys_spuer' or i['name'] == 'shaw_down'or i['name'] == 'na_super':
                spd = int(self.spd*1.5)
            
        self.pos[0] += spd * (movecommand[3]-movecommand[1])
        self.pos[1] += spd * (movecommand[2]-movecommand[0])
        self.rect.center = self.pos        
    
    def teleport(self,pos):
        #teleport to a position
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
    
    def collide(self,target):
        #if collide with a character, knockback target for 50 distance
        if target.type == 'character':
            knockback(target,get_angle(target,self),50)
    
    def knockback(self,direction,kbrange):
        #knockback
        angle = direction* math.pi / 180.0
        kbrange /= self.kbrate
        self.pos[0] -= kbrange * math.cos(angle)
        self.pos[1] += kbrange * math.sin(angle)
    
    def hurt(self,attacker,damage):
        #take damage
        if self.alive == False:
            return
            # dead character won't hur or heal
        for i in self.conditions:
            #can't move conditions
            if i['name'] == 'na_super' or 'fridge' or 'shaw_down':
                damage = 0
        self.hp -= damage
        if self.hp < 0:
            self.death(attacker)
            
        #update the damage calculation
        deal_damage(attacker,damage)
    
    def heal(self,healer,healing):
        #receive healing
        if self.alive == False:
            return
            # dead character won't hur or heal
        self.hp += math.max(self.mhp-self.hp,healing)#if hp >= maxhp, can't be healed
        
        #update the healing calculation
        if healer is not None and healer != self :
            heal_ally(healer,healing)
            
    def death(self):
        #inactivated from current game
        self.alive = False
        self.remove()
    
    def addcondition(self,condition):
        #if already has the condition, update the duration, else add a new condition
        for i in self.conditions:
            if i['name'] == 'shaw_down' or i['name'] == 'na_super',i['name'] == 'fridge':
                #at these conditions, character are immue
                return
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
        
        self.type = 'student'
        self.weapon = weapon(self.data.weapon)
        self.skill1 = skill(self.data.skill1)
        self.skill2 = skill(self.data.skill2)#a cuple of ('name',cd, maxcd)
        self.maxhp = self.data.hp #maxhealth
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
        name_text(self,self.player.username)
        
    def useskill(self,skill):
        #use a skill,including basic attack
        if skill == 'attack':
            if self.weapon.attack() == True:#successfully attack
                skill = self.weapon._action
            else:
                return
        skill.cast(self,self.pos,self.direction)

    
    def setdirection(self,direction):
        #reverse the face direction if its team b
        if self.team == 'b':
            self.direction = -direction+pi
        else:
            self.direction = direction
    
    def movetest(self):
        if self.canmove:
            #move, and then clear the ,ove commands
            if self.team == 'b':
                #reverse the direction if its team b                
                tmp = self.movecommand[1]
                self.movecommand[1] = self.movecommand[3]
                self.movecommand[3] = tmp
                self.move(self.movecommand)
            else:
                self.move(self.movecommand)
            self.movecommand = [0,0,0,0]
    
    def update(self):
        #update the data
        if self.hp < 0:
            self.death()
        else:
            self.movetest()
            self.weapon.update()
            self.skill1.update()
            self.skill2.update()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
        #update conditions
        for i in self.conditions:
            i['duration'] -=1
            if i['duration'] <= 0:
                self.conditions.remove(i)
    
    def death(self,killer):
        #died and teleport to canteen,it will reborn at corresponding canteen later
        self.alive = False
        if self.team == 'a':
            pos = []
        if self.team == 'b':
            pos = []
        self.teleport(pos) 
        defeat_enemy(killer.player)
        #functions that update scores

class npc(character):
    def __init__(self,name,pos,direction,skill,team):
        character.__init__(self,name,pos)
        self.type = 'npc'
        self.direction = direction#direction of move a number ranging from 0 to 360 indicate the angle
        self.facediraction = direction#the direction of its face, may not always equals to direction
        self.move = True
        self.maxduration = self.data.duration
        self.seerange = 600
        self.duration = self.maxduration
        self.skill = skill
        self.team = team
        self.skill.reset()
        self.maxcd = 30
        self.cd = self.maxcd
    
    def update(self):
        #in game, all npc with team will move towards the nearest opponent, updates per second
        if self.duration > 0:
            self.duration -= 1
        if self.hp < 0 or self.duration == 0:
            self.death()
            return
        if self.move:
            self.move(self.direction)
        if self.cd == 0:
            self.useskill()
            self.cd = self.maxcd
        else:
            self.cd -= 1
        if self.move:
            self.move(self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    def useskill(self):
        function = eval(self.skill)
        function(user,pos,direction)

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
