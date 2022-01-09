from django.contrib import admin
from . models import Channel, Schedule
# Register your models here.

admin.site.register([Channel, Schedule])