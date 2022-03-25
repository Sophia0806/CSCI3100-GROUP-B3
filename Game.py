import pygame
import basicfunctions

class game:
    def __init__(self,gametype):
        self._type = gametype

        self._map = None
        self._players = []#players in the game
        self._teams = {'a':[],'b':[]}#a,b is 2 player teams
        self._start =False#whether game is started
        #need data
        self._duration = data._duration#the maximum game duration
    
    def initialize(self):
        #initialze the contents,then start the game
        self.generate_objects()
        self._start = True
        
    def end(self):
        #end the game
        #show the outcome,record,return to the main menu,...
        self._start = False
    
    def check_start(self):
        #check whether is need to start the game
        pass
    
    def check_end(self):
        #check whether is need to end the game
        if self._duration <= 0:
            self.end()
            
    def generate_object(self):
        for i in self._objectlist:
            game_object(i.name,i.pos)
        for i in self._canteenlist:
            canteen(i.name,i.pos,i.team)
            
    def update(self):
        self._duration -= 1
        self._map.update()
        self._map.display()
        #display things in map
        self.check_end()
        
        
    
    
