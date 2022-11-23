import os
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

try:
    for tweets in tweepy.Paginator(
        client.get_home_timeline,
        max_results=50
    ):
        for tweet in tweets.json()['data']:
            # pprint.pprint(tweet)
            print(tweet['text'])
            try:
                client.like(tweet['id'])
            except Exception as e:
                print(e)
except Exception as e:
    print(e)
