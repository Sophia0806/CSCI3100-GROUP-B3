from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.user)
admin.site.register(models.ConfirmString)
admin.site.register(models.Profile)