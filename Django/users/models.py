from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.name