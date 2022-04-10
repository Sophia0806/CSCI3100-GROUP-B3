#test
from Localdata import*
from Skill import*
class weapon:
    def __init__(self,name):
        self._name = name

        '''
        load data from database
        data = 
        '''
        data = weaponlist[name]
        self._action = skill(data['action'])# the corresponding attack type of the weapon
        self._maxammo = data['ammo'] #max attack times
        self._maxcd = data['cd'] #attack cooldown
        self._reloadtime = data['reloadtime'] #time needed for reload
        self.reset()

    
    def reset(self):
        #resetdata
        self._ammo = self._maxammo 
        self._cd = self._maxcd
        self._reloadcd = self._reloadtime
    
    def update(self):
        if self._cd > 0:
            self._cd -=1
        if self._ammo == 0:
            self.reload() # autoreload when ammo is 0
    
    def attack(self):
        if self._ammo <= 0:
            return False
        elif self._cd > 0:
            return False
        else:
            self._ammo -= 1
            self._cd = self._maxcd
            return True
        
    def reload(self):
        #wait for reload finish
        if self._reloadcd <= 0:
            self._ammo = self._maxammo
            self._reloadcd = self._reloadtime
            #display the weapon is reloading
        else:
            self._reloadcd -= 1