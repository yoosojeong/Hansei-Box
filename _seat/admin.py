from django.contrib import admin

from . import models

@admin.register(models.MovieSeatModel)
class SeatAdmin(admin.ModelAdmin):

    list_display = (
        'movie_column_seat',
        'movie_row_seat',
    )