from django.db import models

    
class mObject(models.Model):
    # canteen, building
    name = models.CharField(unique=True,max_length=200)
    photo = models.ImageField(upload_to='static/game/images')
    hp = models.IntegerField()
    duration = models.IntegerField()
    def __str__(self):
        return self.name


class Item(models.Model):
    # projectile, melee, area_effect
    name = models.CharField(unique=True,max_length=200)
    photo = models.FileField(upload_to='static/game/image')
    kb = models.IntegerField()
    damage = models.IntegerField()
    duration = models.IntegerField()
    removal = models.BooleanField()
    # not sure about the data type
    effect =  models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Projectile(Item):
    spd = models.IntegerField()

class Melee(Item):
    spd = models.IntegerField()

class Area_effect(Item):
    frequency = models.IntegerField()

class Bubble(models.Model):
    name = models.CharField(unique=True, max_length=200)
    photo = models.FileField(upload_to='static/game/image')
    message = models.CharField(max_length=200, null=True, blank=True)
    duration = models.IntegerField()
    def __str__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField(unique=True, max_length=200)
    photo = models.FileField(upload_to='static/game/image')
    # not sure bout data type
    action = models.CharField(max_length=200) #effect
    ammo = models.IntegerField()
    cd = models.IntegerField()
    reloadtime = models.IntegerField()
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(unique=True,max_length=200)
    photo = models.FileField(upload_to='static/game/image')
    cd = models.IntegerField()
    # not sure bout data type
    content = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.name

class OnMap(models.Model):
    name = models.CharField(unique=True,max_length=200)
    theobject = models.OneToOneField('mObject', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


# Create your models here.
class Character(models.Model):
    # 9 character
    name = models.CharField(unique=True,max_length=200)
    photo = models.ImageField(upload_to='static/game/images')
    hp = models.IntegerField()
    spd = models.IntegerField()
    kb_rate = models.IntegerField()
    skill_1 = models.OneToOneField('Skill', related_name='first_skill', on_delete=models.CASCADE, null=True, blank=True)
    skill_2 = models.OneToOneField('Skill', related_name='second_skill', on_delete=models.CASCADE, null=True, blank=True)
    weapon = models.OneToOneField('Weapon', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class Student(Character):
    uname = models.CharField(unique=True,max_length=200)
    def __str__(self):
        return self.uname

class Npc(models.Model):
    name = models.CharField(unique=True,max_length=200)
    photo = models.ImageField(upload_to='static/game/images')
    hp = models.IntegerField()
    spd = models.IntegerField()
    kb_rate = models.IntegerField()
    skill = models.OneToOneField('Skill', on_delete=models.CASCADE, null=True, blank=True)
    duration = models.IntegerField()
    def __str__(self):
        return self.name

