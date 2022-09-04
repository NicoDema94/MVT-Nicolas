from django.db import models


class Familia(models.Model):
    nombre = models.CharField(max_length=128)
    age = models.IntegerField()
    nacimiento = models.DateField()
    

