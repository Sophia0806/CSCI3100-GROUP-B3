class player:
    def __init__(self,username):
        self._user = username
        self._character = None #the character currently controlled by the player
        self._pos = [0,0] #the camera position
        self._score = 0
        
    def command(self,command):
        #receive command
        #player command (e.g.chat,endgame...)
        if self._character != None:
            if self._character._alive:
            #character command (e.g. move,attack...),only able when control an alive character
                pass
    
    def choose_character(self,character):
        self._character = character
        
    def update_score(self,score):
        self._score += score
        
    def clear_score(self):
        self._score = 0
    
    def finish_game(self):
        #end the game, and transform the score to the tokens in the useraccount
        pass