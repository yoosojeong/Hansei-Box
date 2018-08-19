from django.contrib import admin

from . import models

@admin.register(models.MovieModel)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'image',
        'ranking',
        'grade',
        'ReservationRate',
    )