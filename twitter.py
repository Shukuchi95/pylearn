#this is a twitter bot that gets tweets about a random topic and puts them into a file. results stored on my website at 51.75.162.248/untitled.py
#results are updated hourly via a cron job 
#i'm using tweepy to talk to the twitter API

import tweepy
import random
api_key = "x"
api_key_secret = "x"
bearer_token = "x"
access_token = "x"
access_token_secret = "x"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

topics = ["pasta", "dota2", "computers", "star wars", "elden ring", "python"]
topic = random.choice(topics)
emptylist = []
tweets = api.search_tweets(q=f"{topic}", count=100, lang="en")
for tweets in tweets:
    tweet = tweets.text
    username = tweets.user.name
    emptylist.append("@" + username + " " + tweet)

def writetofile(text):
    f = open("untitled.py", "w")
    f.write(f"{text}")


