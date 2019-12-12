from django.db import models

# Create your models here.

class Robo(models.Model):
    dir_choices = [('NORTH','NORTH'),('EAST','EAST'),('SOUTH','SOUTH'),('WEST','WEST')]
    name = models.CharField(max_length=100, unique=True)
    x_cordinate = models.IntegerField(default=0)
    y_cordinate = models.IntegerField(default=0)
    direction = models.CharField(choices=dir_choices, max_length=5)
