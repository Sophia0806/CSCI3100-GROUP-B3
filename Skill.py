import math
class skill:
    def __init__(self,name):
        self._name = name
        #data = 
        self._maxcd = 0
        self._contents = []#the content that need to be used
        self.reset()
    
    def reset(self):
        #reset the data
        self._cd = self._maxcd
    
    def update(self):
        if self._cd > 0:
            self._cd -= 1
            
    def cast(self,pos,direction):
        #run a skill function with the same name in (pos,direction)
        self._cd = self._maxcd