#coding=utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import RequestContext,loader
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
        game = Game.objects.get(pk=request.GET["cp_id"])
        template = loader.get_template('game/test.html')
        context = RequestContext(request,{
            'game':game,
            })
        return HttpResponse(template.render(context))
    except Exception as e :
        print e
        return HttpResponse("xxxxx")
