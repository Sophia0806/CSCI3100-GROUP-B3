
class player:
    def __init__(self,userid,username):
        self._id = userid
        self._user = username
        self._character = None #the character currently controlled by the player
        self._pos = [0,0] #the camera position on the map
        self._score = 0
        self._ready = False
        #game could start if there are enogh players and all of them are ready
        
    def command(self,command):
        #receive command
        if command == 'ready':
            self._ready = True
        if check_alive_character(self):
        #player command (e.g.chat,endgame...)
            if command == 'up':
                pass
            #character command (e.g. move,attack...),only able when control an alive character
            
    def check_alive_character(self):
        #check whether the player is controlling a alive character.
        if self._character != None:
            return self._character._alive
        return False
        
    def update_position(self,pos):
        self._pos = pos #x,y
        
    def choose_character(self,character):
        self._character = character
    
    def delete_character(self):
        self._character = None
        
    def add_score(self,score):
        self._score += score
        
    def clear_score(self):
        self._score = 0
    
    def exit_game(self):
        #end the game, and transform the score to the tokens in the useraccount
        pass