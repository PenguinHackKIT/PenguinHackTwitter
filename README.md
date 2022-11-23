# PenguinHackTwitter
for [@hacks_penguin](https://twitter.com/hacks_penguin)

## setup.sh
```
$ bash setup.sh
```

## tweepy Client.return_type

If tweepy.Paginator is not used, you can use requests.Response.

```py
client = tweepy.Client(
    os.environ['BEARER_TOKEN'],
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_TOKEN_SECRET'],
    return_type=requests.Response,
    wait_on_rate_limit=True
)
```

## docs

[tweepy](https://docs.tweepy.org/en/stable/index.html)