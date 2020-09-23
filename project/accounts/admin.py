from django.contrib import admin
from .models import (
    Game,
    GameTrain,
    Client,
    Score,
    Image,
    ImageSet,
    )

class GameAdmin(admin.ModelAdmin):
    list_display = ('title','body')
    search_fields = ()

admin.site.register(Game, GameAdmin)


class GameTrainAdmin(admin.ModelAdmin):
    list_display = ('user','game','index')
    search_fields = ()

admin.site.register(GameTrain, GameTrainAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('is_active',)
    search_fields = (['is_active'])

admin.site.register(Client, ClientAdmin)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user','index','game_train')
    search_fields = ()

admin.site.register(Score, ScoreAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title','clinician')
    search_fields = ()

admin.site.register(Image, ImageAdmin)


class ImageSetAdmin(admin.ModelAdmin):
    list_display = ('title','clinician')
    search_fields = ()

admin.site.register(ImageSet, ImageSetAdmin)