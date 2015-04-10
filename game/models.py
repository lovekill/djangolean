from django.db import models

# Create your models here.
class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=50)
    create_time = models.DateTimeField()

class Chanel(models.Model):
    chanel_id = models.AutoField(primary_key=True)
    chanel_name = models.CharField(max_length=32)
    game = models.ManyToManyField(Game)

class User(models.Model):
    uid = models.CharField(max_length=64,primary_key=True)
    imei = models.CharField(max_length=64)
    imsi = models.CharField(max_length=64)


