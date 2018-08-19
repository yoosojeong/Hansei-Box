# from multiselectfield import MultiSelectField
from django.db import models
from _user import models as user_models
from _movie import models as movie_models
from _seat import models as seat_models

class MovieTheaterModel(models.Model):

    movie_time_CHOICES = {
        ('3:00', '3:00'),
        ('6:00', '6:00'),
        ('9:00', '9:00'),
    }

    movie_user = models.ForeignKey(user_models.Profile, on_delete=models.CASCADE, null=True)
    movie_title = models.ForeignKey(movie_models.MovieModel, on_delete=models.CASCADE, null=True)
    movie_seat = models.ManyToManyField(seat_models.MovieSeatModel) 
    movie_data = models.DateField() #date필드 수정, date로 오타 수정
    movie_time = models.CharField(max_length=10, choices=movie_time_CHOICES , null=True)
    


    def get_seat(self):
        return "\n".join([s.movie_column_seat + s.movie_row_seat for s in self.movie_seat.all()])

    