from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(unique=True,max_length=200)
    photo = models.FileField(upload_to='static/img')
    hp = models.IntegerField()
    spd = models.IntegerField()
    kb_rate = models.IntegerField()
    
class mObject(models.Model):
    name = models.CharField(unique=True,max_length=200)
    photo = models.FileField(upload_to='static/img')
    hp = models.IntegerField()
    duration = models.IntegerField()

class Item(models.Model):
    name = models.CharField(unique=True,max_length=200)
    photo = models.FileField(upload_to='static/img')
    kb = models.IntegerField()
    damage = models.IntegerField()
    duration = models.IntegerField()
    removal = models.BooleanField()
    # not sure about the data type
    effect =  models.CharField(max_length=200)

class Bubble(models.Model):
    name = models.CharField(unique=True, max_length=200)
    photo = models.FileField(upload_to='static/img')
    duration = models.IntegerField()

class Weapon(models.Model):
    name = models.CharField(unique=True, max_length=200)
    photo = models.FileField(upload_to='static/img')
    # not sure bout data type
    action = models.CharField(max_length=200) #effect
    ammo = models.IntegerField()
    cd = models.IntegerField()
    reloadtime = models.IntegerField()

class Skill(models.Model):
    name = models.CharField(unique=True,max_length=200)
    photo = models.FileField(upload_to='static/img')
    cd = models.IntegerField()
    # not sure bout data type
    content = models.FileField()

class OnMap(models.Model):
    name = models.CharField(unique=True,max_length=200)
    theobject = models.OneToOneField('mObject', on_delete=models.CASCADE)