#test
import pygame
from pygame import Color
from pygame.locals import *
from Serverdata import*
from Character import*

class player:
    def __init__(self,userid,username):
        self._id = userid
        self._user = username
        self._character = None #the character currently controlled by the player
        self._pos = [0,0] #the camera position on the map
        self._score = 0
        self._ready = False
        self._subscreen =None#the part of gamemap that the player can see.
        self.bubbles = pygame.sprite.Group()#bubbles that only the player can see
        '''
        get the character name and team by database(when user select the team and character in html, 
        update this value into the corresponding player database.
        character_name =
        self._team = 
        '''
        self.add_character(character_name)
    
    def update():
        '''
        each get a array(list) of clicked keys from the data base(html get the command every 1/30 sec,
        send to server, and the program will update them in the database)stored in a list
        called commands.
        so as the mouse clicked status and its position, store in mouse_statue = (mouse_status, mouse_pos)
        this function triggers each frame
        '''
        mousecommand(self,mouse_status)
        for i in commands:
            self.keycommand(i)
    
    def get_screen_cut(self):
        rect = pygame.Rect(self.pos[0],self.pos[1],1200,800)
        '''
        screen =
        this is the method that get the screenshot of the map from database
        '''
        self.subscreen = screen.copy()
        sub = screen.subsurface(rect)
        for i in self.bubbles:
            sub.blit(i.image, i.rect)
        if self.team == 'b':
            sub = pygame.transform.flip(sub, True, False)
        string = pygame.image.tostring(sub,"RGB")
        '''
        send the string to corrseponding database(player.screen), the server program need send each RGB string 
        to corresponing client every 1/30 sec, and the html need update the screen showup while receive a new
        RGB string
        '''
    
    def mousecommand(self,mouse_status):
        pass
        
    def keycommand(self,command):
        #receive command
        if check_alive_character(self):
            #update the moving command of the character
            if command == 'k_a':
                self._character.movecommand[0] = 1
            elif command == 'down':
                self._character.movecommand[1] = 1
            elif command == 'left':
                self._character.movecommand[2] = 1
            elif command == 'right':
                self._character.movecommand[3] = 1
            #attack or use skills:
            
    def check_alive_character(self):
        #check whether the player is controlling a alive character.
        if self._character != None:
            return self._character._alive
        return False
        
    def update_position(self,pos):
        self._pos = pos #x,y
    
    def choose_team(self,team):
        if team == 'a' or team == 'b':
            self._team = team
        else:
            print('invalid team')
        
    def add_character(self,character_name):
        self._character = student(character_name,self._team,(Height/2,Width/2))
    
    def delete_character(self):
        self._character.remove()
        self._character = None
        
    def add_score(self,score):
        self._score += score
        
    def clear_score(self):
        self._score = 0
    
    def end_game(self):
        self.delete_character()
        '''
        the player exit the game, and store his score into the data base of corresponding user account,
        also, show the game record in the html of client
        '''