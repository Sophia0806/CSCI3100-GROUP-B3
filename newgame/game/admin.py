from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Character)
admin.site.register(models.Student)
admin.site.register(models.Item)
admin.site.register(models.mObject)
admin.site.register(models.Bubble)
admin.site.register(models.Weapon)
admin.site.register(models.Skill)
admin.site.register(models.OnMap)
admin.site.register(models.Npc)
admin.site.register(models.Projectile)
admin.site.register(models.Melee)
admin.site.register(models.Area_effect)
