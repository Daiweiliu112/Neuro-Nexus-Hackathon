from django.contrib import admin
from .models import (
    Game,
    GameTrain,
    Client,
    Score,
    Image,
    ImageSet
    )
import csv
from django.http import HttpResponse



class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response


class GameAdmin(admin.ModelAdmin):
    list_display = ('title','body')
    search_fields = ()
    
    actions = ["export_user_csv"]


admin.site.register(Game, GameAdmin)


class GameTrainAdmin(admin.ModelAdmin):
    list_display = ('user','game','index')
    search_fields = ()
    
    actions = ["export_user_csv"]


admin.site.register(GameTrain, GameTrainAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('is_active','clinician','email','id_num')
    search_fields = (['is_active'])

    actions = ["export_user_csv"]

admin.site.register(Client, ClientAdmin)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user','index','game_train')
    search_fields = ()
    
    actions = ["export_user_csv"]

admin.site.register(Score, ScoreAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title','clinician')
    search_fields = ()

    actions = ["export_user_csv"]

admin.site.register(Image, ImageAdmin)


class ImageSetAdmin(admin.ModelAdmin):
    list_display = ('title','clinician')
    search_fields = ()

    actions = ["export_user_csv"]

admin.site.register(ImageSet, ImageSetAdmin)