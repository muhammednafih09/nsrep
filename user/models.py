from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Profile(models.Model):
    user = models.OneToOneField(User)
    usertype = models.CharField(max_length=50)
    image = models.ImageField(upload_to="profile_images")
    
    def __str__(self):  
        return self.user.email

