import twitter
from secrets import consumer_key, consumer_secret
from secrets import access_token_key, access_token_secret

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret,
                  sleep_on_rate_limit=True)


def send_tweet(msg):
    status = api.PostUpdate(msg)
    print(status.user.name)
    print(status.text)
