#coding=utf-8
from django.db import models

# Create your models here.
class Chanel(models.Model):
    chanel_id = models.AutoField(primary_key=True)
    chanel_name = models.CharField(max_length=32)
    def __str__(self):
        return self.chanel_name.encode('utf-8')

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    chanel = models.ManyToManyField(Chanel)
    def __str__(self):
        return self.game_name.encode('utf-8')

    


class GameChanelRelation(models.Model):
    game = models.ForeignKey(Game)
    chanel = models.ForeignKey(Chanel)
    def __str__(self):
        name_chanel = "game:{0} chanel :{1}".format(game,chanel)
        return name_chanel

class User(models.Model):
    uid = models.CharField(max_length=64,primary_key=True)
    imei = models.CharField(max_length=64)
    imsi = models.CharField(max_length=64)
    def __str__(self):
        return self.uid


