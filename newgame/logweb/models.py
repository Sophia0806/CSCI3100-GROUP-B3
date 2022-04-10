from django.db import models

# Create your models here.
class user(models.Model):
    # user_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=256)
    # token is the total score the user get from previous games. default as zero.
    token = models.IntegerField(default=0)

    # c_time for the admin to list users
    c_time = models.DateTimeField(auto_now_add=True)
    # profile photo for now
    # profile_photo = models.ImageField(default='default.jpg', upload_to="images/")
    # 1017 to record whether the account has been verified
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname
    
    class Meta:
        ordering = ["-c_time"]

class Profile(models.Model):
    user = models.OneToOneField('user', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images")

    def __str__(self):
        return f'{self.user.nickname} Profile'

# 1017 email verification part
class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('user', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.nickname + ":   " + self.code

    class Meta:
        ordering = ["-c_time"]

