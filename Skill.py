import math
from Skill_functions import*
from Basicfunctions import*
from Item import*
#test
from Localdata import*

class skill:
    def __init__(self,name):
        self._name = name
        #these value get from database
            #data = models.skill.get(name = self._name)
        data = skilllist[name]
        self._maxcd = data['cd']
        self.reset()
    
    def reset(self):
        #reset the data
        self._cd = self._maxcd
    
    def update(self):
        if self._cd > 0:
            self._cd -= 1
            
    def cast(self,user,pos,direction):
        #run a skill function with the same name in (pos,direction)
        if self._cd <= 0:
            self._cd = self._maxcd
            function = eval(self._name)
        #skill name is the same as the correspoding function name
            function(user,pos,direction)