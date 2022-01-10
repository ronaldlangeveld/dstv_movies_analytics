from django.db import models


# Create your models here.

# "sub_title": "Rating: PG13, Mystery, 2021",

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    sub_title = models.CharField(max_length=500, null=True, blank=True)
    rating = models.CharField(max_length=500, null=True, blank=True)
    year = models.IntegerField(default=0, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    running_time = models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return str(self.title)

