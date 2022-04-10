import pygame
from Basicfunctions import*
from Map import*

class game:
    def __init__(self,gametype):
        self.type = gametype
        self.map = game_map('test',gametype)
        self.players = []#players in the game
        self.minplayers = 0 #minmum players to start
        self.maxplayers = 10 #maxmum players to join
        self.teams = {'a':[],'b':[]}#a,b is 2 player teams
        self._start =False#whether game is started
        #need data
        self.duration = 100000#the maximum game duration,countdown
    
    def start(self):
        #initialze the contents,then start the game
        self.map.generate_objects()
        '''
        except:
            print('error in generating map objects')
        '''
        self.start = True
        
    def end(self):
        #end the game
        #show the outcome,record,return to the main menu,...
        self.start = False
        
    def player_join(self,player):
        for i in self.players:
            if i.id == player.id:
               print('player already joined the game')
        else:
            self.players.append(player)
        
    def player_leave(self,player):
        for i in self.players:
            if i.id == player.id:
               self.players.remove(i)
        else:
            print('player is not in the game')
    
    def check_start(self):
        #check whether is need to start the game
        ready = 0
        for i in self.players:
            if i.ready is False:
                return False
        if len(self.players) >= self.minplayers:
            return True
    
    def check_end(self):
        #check whether is need to end the game
        if self.duration <= 0:
            return True
        return False
            
    def update(self):
        self.duration -= 1
        for i in self.players:
            i.update()
        self.map.update()
        self.map.display()
        #display things in map
        self.check_end()
        
    
    
