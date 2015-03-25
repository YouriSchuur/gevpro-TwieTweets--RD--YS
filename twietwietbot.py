#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, twietwiets

CONSUMER_KEY = 'XPkqjxqIOx8IKifTWPnEi8coU'
CONSUMER_SECRET = 'cBQeVEcNOUlztwyDVnqo4y7nBvvdm3s0iMZ83NBXIroqWeIkcF'
ACCESS_KEY = '3115005287-qmh9xd4wXXqftCxyf1BHW7oRvQHcUKDwTmU6BCo'
ACCESS_SECRET = 'JSn387CHzXcN99iBvXbADGvR51pTQpmYD2w2Rvz9gDydZ'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

"""Van het groepje: TweetMe overgenomen"""
twieTweet = twietwiets.twietwiets()
while 1 > 0:
    twietwiet = twieTweet.get_twietwiet()
    print(twietwiet)
    line1 = " ".join(twietwiet[0])
    line2 = " ".join(twietwiet[1])
    tweet = line1 + '\n' + line2
    if len(line1) <= 128 and len(line2) <= 128:
        api.update_status(status=tweet)
        time.sleep(3600)

"""used this tutorial: http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/"""
