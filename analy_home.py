import os
import datetime
import pprint
import tweepy
import requests

client = tweepy.Client(
    os.environ['BEARER_TOKEN'],
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_TOKEN_SECRET'],
    return_type=requests.Response,
    wait_on_rate_limit=True
)

l=[]

try:
    for tweets in tweepy.Paginator(
        client.get_home_timeline,
        tweet_fields=['created_at'],
        max_results=100
    ):
        for tweet in tweets.json()['data']:
            # pprint.pprint(tweet)
            print(tweet['id'])
            date = datetime.datetime.fromisoformat(tweet['created_at'].split('.')[0]).replace(tzinfo=datetime.timezone.utc).astimezone(datetime.timezone(datetime.timedelta(hours=9)))
            print(date)
            l.append(date)

except Exception as e:
    print(e)

week={}

for date in l:
    a=date.strftime('%a')
    if a in week:
        week[a]+=1
    else:
        week[a]=0

print(week)


hours=[0]*24

for date in l:
    h=date.strftime('%H')
    hours[int(h)]+=1

for r in range(24):
    print(r,hours[r])
