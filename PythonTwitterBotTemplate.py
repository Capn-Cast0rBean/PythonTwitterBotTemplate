### PythonTwitterBotTemplate.py ###
### Created by Capn-Cast0rBean ###

### IMPORTS ###

import time
import tweepy





### OUTPUT FUNCTION ###

def twitterPost():
    return ("This bot will tweet the return value of the function twitterPost().")





### TWITTER OUTPUT ###

hoursBetweenTweet = 1

CONSUMER_KEY = 'Enter your Consumer Key here.'
CONSUMER_SECRET = 'Enter your Consumer Secret Key here.'
ACCESS_KEY = 'Enter your Access Key here.'
ACCESS_SECRET = 'Enter your Access Secret Key here.'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    postThis = twitterPost()
    if len(postThis) <= 140:
        api.update_status(status=postThis)
        print(postThis)
        time.sleep(hoursBetweenTweet * 3600)
