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
    end_time = models.DateTimeField(null=True, blank=True)
    premiere = models.BooleanField(default=False)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="channel_schedule")

    class Meta:
        ordering = ['movie__title', 'show_time']

    def __str__(self):
        return str(f"{self.movie} - {self.show_time}")