import math
from Skill_functions import*
from Basicfunctions import*
from Item import*

class skill:
    def __init__(self,name):
        self._name = name
        #these value get from database
        try:
            data = models.skill.get(name = self._name)
            self._maxcd = data._maxcd
            self._contents = data._contents#the content that need to be used
            self.reset()
        except:
            print('this type of skill do not exist')
    
    def reset(self):
        #reset the data
        self._cd = self._maxcd
    
    def update(self):
        if self._cd > 0:
            self._cd -= 1
            
    def cast(self,pos,direction):
        #run a skill function with the same name in (pos,direction)
        self._cd = self._maxcd
        skill = eval(self.name)
        #skill name is the same as the correspoding function name
        skill(pos,direction)