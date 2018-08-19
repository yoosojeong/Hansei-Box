from django.db import models

class MovieSeatModel(models.Model):

    movie_seat_column_CHOICES = {

        ('세로', (
            ("A", "A"),
            ("B", "B"),
            ("C", "B"),
            ("D", "D"),
            ("E", "E"),
            ("F", "F"),
            ("G", "G"),
            ("H", "H"),
            ("I", "I"),
            ("J", "J"),
            ("K", "K"),
            ("L", "L"),
            ("M", "M"),
            ("N", "N"),
            )
        )
    }

    movie_seat_row_CHOICES = {
    
        ('가로', (
            ('01', '01'),
            ('02', '02'),
            ('03', '03'),
            ('04', '04'),
            ('05', '05'),
            ('06', '06'),
            ('07', '07'),
            ('08', '08'),
            ('09', '09'),
            ('10', '10'),
            ('11', '11'),
            ('12', '12'),
            ('13', '13'),
            ('14', '14'),
            ('15', '15'),
            ('16', '16'),
            ('17', '17'),
            ('18', '18'),
            ('19', '19'),
            ('20', '20'),
            ('21', '21'),
            ('22', '22'),
            )   
        )
    }

    movie_column_seat = models.CharField(max_length=10, choices=movie_seat_column_CHOICES, blank=True)
    movie_row_seat = models.CharField(max_length=10, choices=movie_seat_row_CHOICES, blank=True)

    def __str__(self):
        return '%s%s' % (self.movie_column_seat, self.movie_row_seat)