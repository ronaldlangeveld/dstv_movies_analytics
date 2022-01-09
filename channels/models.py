from django.db import models
from movies.models import Movie

# Create your models here.


class Channel(models.Model):
    name = models.CharField(max_length=100)
    channel_code = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_schedule')
    show_time = models.DateTimeField()
    premiere = models.BooleanField(default=False)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="channel_schedule")

    def __str__(self):
        return self.movie.title