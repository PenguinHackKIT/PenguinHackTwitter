import os
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

client.follow_user(input('id>'))
