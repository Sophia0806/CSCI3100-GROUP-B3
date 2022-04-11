import pygame
from Basicfunctions import*
from Map import*

class game:
    def __init__(self,gametype):
        self.type = gametype
        '''
        load data from database
        self.map =
        Serverdata.servermap = self.map
        '''
        self.players = []#players in the game
        self.playerids = []#players in the game
        self.teams = {'a':[],'b':[],'n':[]}#a,b is 2 player teams,n is neutral(not used, noly for debug)
        self._start =False#whether game is started
        #need data
        self.duration = 1200#the maximum game duration(sec),countdown
    
    def start(self):
        #initialze the contents,then start the game
        self.map.generate_objects()
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
            self.playerids.append(player.id)
            self.teams[i._team].append(player)
        
    def player_leave(self,player):
        for i in self.players:
            if i.id == player.id:
               self.players.remove(i)
               self.playerids.remove(i.id)
               self.teams[i._team].remove(i)
               i.end_game()
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
        self.map.update()
    
    def big_update(self):
        '''
        get the list of current players in the database
        playerlist = []
        '''
        #check players in database, add new players, and remove left players
        for i in playerlist:
            if i.id not in self.playerids:
                self.player_join(i.id,i.username)
        for i in self.players:
            player_exist = False
            for j in playerlist:
                if i.id == j.id:
                    player_exist = True
            if player_exist = False:
                self.player_leave(i)
                
        for i in self.players:
            i.update()
        self.duration -= 1
        self.check_end()
    

    
    
