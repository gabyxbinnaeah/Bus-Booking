from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES =((1,'admin'),
                        (2,'Bus'), 
                        (3,'Book'))
    user_type =models.PositiveIntegerField(choices=USER_TYPE_CHOICES)
class Admin(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    user =models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='user')
    
    def __str__(self):
        return self.email  

