from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class TeamLead(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, null=True)
#     # email = models.EmailField(name="email address", blank=True)
#     profile_pic = models.ImageField(default="default.png",null=True, blank=True)

#     def __str__(self):
#         return self.name

# class Member(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="", default="default.png", blank=True)

#     @property
#     def get_instance(self):
#         return self