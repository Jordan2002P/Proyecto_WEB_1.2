from django.db import models

# Create your models here.

class Usuario (models.Model):
    username = models.CharField(max_length=30)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password= models.CharField(max_length=128)