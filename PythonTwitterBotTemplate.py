### PythonTwitterBotTemplate.py is a Python Template to create a bot that posts on Twitter.
### Copyright (C) 2021  Capn-Cast0rBean

### This program is free software: you can redistribute it and/or modify
### it under the terms of the GNU Affero General Public License as published
### by the Free Software Foundation, either version 3 of the License, or
### (at your option) any later version.

### This program is distributed in the hope that it will be useful,
### but WITHOUT ANY WARRANTY; without even the implied warranty of
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
### GNU Affero General Public License for more details.

### You should have received a copy of the GNU Affero General Public License
### along with this program.  If not, see <https://www.gnu.org/licenses/>.





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
