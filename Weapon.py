class weapon:
    def __init__(self,name):
        self._name = name
        self._action = None# the corresponding attack type of the weapon
        self._maxammo = 0
        self._ammo = self._maxammo #max attack times
        self._maxcd = 0 #attack cooldown
        self._reloadtime = 0 #time needed for reload
        self._cd = self._maxcd
    
    def update(self):
        if self._cd > 0:
            self._cd -=1
        if self._ammo == 0:
            self.reload#autoreload when ammo is 0
    
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
        self._ammo = self._maxammo