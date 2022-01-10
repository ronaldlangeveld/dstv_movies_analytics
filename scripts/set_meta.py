from movies.models import Movie, Genre
from channels.models import Channel, Schedule
from datetime import timedelta, date
import requests



def run():
    for a in Schedule.objects.filter(end_time=None):
        
        
        try:
            print(a)
            a.end_time = a.show_time + timedelta(minutes=a.movie.running_time)


            a.save()
            
            
            

        except Exception as e:
            print(e)
        # Split Rating: PG13, Drama, 2018 into ['PG13', 'Drama', '2018']
        # rating = a.sub_title.split(',')[0].split(':')[1].strip()
        # genre = a.sub_title.split(',')[1].strip()
        # year = a.sub_title.split(',')[2].strip()
        # year = a.sub_title.split(',')[2].strip()
        # genre = a.sub_title.split(',')[0].strip()
        # print(year)

