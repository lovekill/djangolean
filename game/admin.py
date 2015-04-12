from django.contrib import admin 
from game.models import Game
from game.models import Chanel
from game.models import User
# Register your models here.
class GameAdmin(admin.ModelAdmin):
    fields = ['game_id','game_name']
admin.site.register(Game)
admin.site.register(Chanel)
admin.site.register(User)
