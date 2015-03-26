#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Aanroep:
installeer pip en tweepy.
kopieer de mappen pip, tweepy en six.1.9... en het bestand six.py
naar dezelfde map waar twietwietbot ook in zit.
roep aan met ./twietwietbot.py
"""

import tweepy, time, sys, twietwiets

CONSUMER_KEY = 'XPkqjxqIOx8IKifTWPnEi8coU'
CONSUMER_SECRET = 'cBQeVEcNOUlztwyDVnqo4y7nBvvdm3s0iMZ83NBXIroqWeIkcF'
ACCESS_KEY = '3115005287-qmh9xd4wXXqftCxyf1BHW7oRvQHcUKDwTmU6BCo'
ACCESS_SECRET = 'JSn387CHzXcN99iBvXbADGvR51pTQpmYD2w2Rvz9gDydZ'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


twieTweet = twietwiets.twietwiets()
while 1 > 0:
    twietwiet = twieTweet.get_twietwiet()
    """print kun je behouden als je wilt zien
    wat er getweet wordt zonder op twitter te kijken"""
    line1 = " ".join(twietwiet[0])
    line2 = " ".join(twietwiet[1])
    tweet = line1 + '\n' + line2
    print(tweet)
    if len(tweet) <= 140:
        api.update_status(status=tweet)
        time.sleep(3600)
    else:
        twietwiet = twieTweet.get_twietwiet()
        line1 = " ".join(twietwiet[0])
        line2 = " ".join(twietwiet[1])
        tweet = line1 + '\n' + line2
        print(tweet) 

"""gebruik gemaakt van deze website: http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/"""
