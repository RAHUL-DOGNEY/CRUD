from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    pwd = models.CharField(max_length=50)
   