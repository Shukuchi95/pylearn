#this is a twitter bot that gets tweets about a random topic and puts them into a file. results stored on my website at 51.75.162.248/untitled.py
#results are updated hourly via a cron job 
#i'm using tweepy to talk to the twitter API

import tweepy
import random

api_key = "X"
api_key_secret = "X"
access_token = "X"
access_token_secret = "X"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
topics = ["dota2", "thechase", "starwars", "computers", "eldenring", "pasta"]
topic = random.choice(topics)

tweets = api.search_tweets(q=f"{topic}", count=10, lang="en")

def writetofile(text):
    f = open("untitled.txt", "w")
    f.write("\n")
    f.write(f"{text}")
    f.write("\n")
writetofile([tweet.text for tweet in tweets])
