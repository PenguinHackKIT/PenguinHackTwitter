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

id=input('id>')

try:
    for followers in tweepy.Paginator(
        client.get_users_followers,
        id=id,
        max_results=1000
    ):
        for follower in followers.json()['data']:
            print(follower['username'])
            try:
                client.follow_user(follower['id'])
            except Exception as e:
                print(e)
except Exception as e:
    print(e)