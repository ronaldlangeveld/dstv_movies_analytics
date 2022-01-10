from movies.models import Movie
from channels.models import Channel, Schedule
from datetime import timedelta, date, datetime
import requests
from django.utils.dateparse import parse_date
from django.utils.timezone import make_aware
import pytz


def daterange(date1, date2):
    for n in range(int((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def run():
    print("Running...")
    # try:
    #     start_date = date(2021, 1, 1)
    #     end_date = date(2022, 1, 23)
    #     for dt in daterange(start_date, end_date):
    #         print(dt.strftime("%Y-%m-%d"))
    #         r = requests.get('https://m-net.dstv.com/tv-guide-day.json?date=%s&channels=28,29,30,31' % dt.strftime("%Y-%m-%d"))
    #         data = r.json()
    #         content = data['content']['channel_shows']
    #         for a in content:
    #             channel = Channel.objects.get(channel_code=a['channel'])
    #             for a in a['shows']:
    #                 # "sub_title": "Rating: PG13, Mystery, 2021",
    #                 movie, created = Movie.objects.get_or_create(title=a['title'])
    #                 if created:
    #                     print('new movie')
    #                     print("Created: %s" % movie)
    #                 else:
    #                     print("Exists: %s" % movie)
    #                 movie.description = a['blurb']
    #                 movie.sub_title = a['sub_title']
    #                 movie.running_time = a['show_length']
    #                 movie.save()
    #                 timestamp = datetime.strptime(a['show_time_start_full'], "%Y-%m-%d %H:%M")

    #                 show_time = make_aware(timestamp, pytz.timezone('Africa/Johannesburg'))
    #                 if Schedule.objects.filter(movie=movie, show_time=show_time, channel=channel).exists():
    #                     print('exists')
    #                 else:
    #                     sched, crtd = Schedule.objects.get_or_create(channel=channel, movie=movie, show_time=show_time)
    #                     sched.premiere=a['is_new']
    #                     sched.save()
    #                     if(crtd == True):
    #                         print('Created: %s' % sched)
    #                     else:
    #                         print('already exists: %s' % sched)
    #                         pass

    #         print(f"{dt.strftime('%Y-%m-%d')} done")

    # except Exception as e:
    #     print(e)

