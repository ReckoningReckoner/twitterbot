from api import send_tweet
import time
import sys

tweets = open("./tweets.txt").readlines()
last_index = open("./lastindex.txt", "r+")
time_delay = 1

i = int(last_index.readline())
while True:
    try:
        tweet = tweets[i].rstrip()
        send_tweet(tweet)
        time.sleep(1)
        if i < len(tweets) - 1:
            i += 1
        else:
            i = 0
    except:
        last_index.truncate()
        last_index.seek(0)
        last_index.write(str(i + 1))
        sys.exit()
