from django.db import models

class MovieModel(models.Model):

    title =  models.CharField(max_length=80)
    image = models.ImageField(upload_to="media/",null=True, blank=True)
    ranking = models.CharField(max_length=80)
    grade = models.CharField(max_length=80)
    ReservationRate = models.CharField(max_length=80)

    def __str__(self):
        return self.title

#class MovietheaterModel(models.Model):
#class MovieChooseModel(models.Model):


