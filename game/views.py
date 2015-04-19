#coding=utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import RequestContext,loader
from django.shortcuts import render_to_response
from django.core import serializers
from game.models import Game
from game.models import Chanel
import json
# Create your views here.
def init(request):
    try:
        game = Game.objects.get(pk=request.GET["cp_id"])
        jsondirc={"code":0,"dsce":'success'}
        jsondirc[game.game_id]=game.game_name
        chaneldict = []
        for c in game.chanel.all():
            cdict={}
            cdict[c.chanel_id]=c.chanel_name
            chaneldict.append(cdict)
        jsondirc["chanel"] = chaneldict
        return HttpResponse(json.dumps(jsondirc))
    except Exception as e :
        print e 
        faidict = {"code":1,"desc":"game_id not fund"}
        return HttpResponse("error")

def testTemp(request):
    try:
        games = Game.objects.all()
        data =[]
        for ga in games:
            dict = {"gameId":ga.game_id,"gameName":ga.game_name}
            data.append(dict)
        string = json.dumps(data)
        return HttpResponse(string)
    except Exception as e :
        print e
        return HttpResponse("xxxxx")

def easyui(request):
    return render_to_response('game/test.html')
