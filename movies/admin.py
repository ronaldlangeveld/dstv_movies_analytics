from django.contrib import admin
from .models import Movies, Channels, Schedule
# Register your models here.

admin.site.register([Movies, Channels, Schedule])