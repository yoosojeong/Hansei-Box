from django.contrib import admin

from . import models

@admin.register(models.MovieTheaterModel)
class TheaterAdmin(admin.ModelAdmin):

    list_display = (
        'movie_user',
        'movie_title',
        'movie_data',
        'get_seat',
        'movie_time',
    )