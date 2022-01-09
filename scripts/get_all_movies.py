from movies.models import Movies, Channels, Schedule
from datetime import timedelta, date
import requests


def daterange(date1, date2):
    for n in range(int((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def run():
    print("Running...")
    # try:
    #     start_date = date(2021, 1, 1)
    #     end_date = date(2021, 12, 31)
    #     for dt in daterange(start_date, end_date):
    #         print(dt.strftime("%Y-%m-%d"))
    #         r = requests.get('https://m-net.dstv.com/tv-guide-day.json?date=%s&channels=28,29,30,31' % dt.strftime("%Y-%m-%d"))
    #         data = r.json()
    #         content = data['content']['channel_shows']
    #         for a in content:
    #             channel = Channels.objects.get(channel_code=a['channel'])
    #             for a in a['shows']:
    #                 movie, created = Movies.objects.get_or_create(title=a['title'])
    #                 movie.description = a['blurb']
    #                 movie.save()
    #                 show_time = a['show_time_start_full']
    #                 sched = Schedule()
    #                 sched.movie = movie
    #                 sched.show_time = show_time
    #                 sched.channel = channel
    #                 sched.premiere = a['is_new']
    #                 sched.save()

    #         print(f"{dt.strftime('%Y-%m-%d')} done")

    # except Exception as e:
    #     print(e)

