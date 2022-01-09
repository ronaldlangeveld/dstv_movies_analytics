from django.db import models

# Create your models here.

class Channels(models.Model):
    name = models.CharField(max_length=100)
    channel_code = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Movies(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    def __str__(self):
        return str(self.title)

class Schedule(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='movie_schedule')
    show_time = models.DateTimeField()
    premiere = models.BooleanField(default=False)
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title