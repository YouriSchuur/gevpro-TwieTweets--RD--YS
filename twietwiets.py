#!/usr/bin/python3
#twietwiets.py
#Roy David & Youri Schuur

import sys
from PyQt4 import QtGui, QtCore
import random

class twietwiets(QtGui.QWidget):
    """This program creates twietwiets from tweet.txt using dpw.cd
    (a dutch pronounciation dictionairy)"""

    def __init__(self):
        
        #super(twietwiets, self).__init__()
        self.tweetfile = open("tweets.txt", "r")
        self.pronfile = open("dpw.cd", "r")
        self.create_prondict()
        self.get_usable_tweets()
        self.get_twietwiet()

    def create_prondict(self):
        pronlist = []
        self.prondict = {}
        for line in self.pronfile:
            pronlist.append(line.split("\\"))
        for pron_word in pronlist:
            key = pron_word[1]
            value = pron_word[3]
            self.prondict[key] = value
        return self.prondict

    def get_usable_tweets(self):
        tweetlist = []
        self.usable_tweetlist = []
        for line in self.tweetfile:
            tweetlist.append(line.split())
        for tweet in tweetlist:
            if tweet[-1] in self.prondict:
                self.usable_tweetlist.append(tweet)
        return self.usable_tweetlist

    def get_twietwiet(self):
        tweetdict = {}
        self.twietwiet = []
        for tweet in self.usable_tweetlist:
            key = tweet[-1]
            value = self.prondict.get(key, 'unknown')
            tweetdict[key] = value
        while self.twietwiet == []:
            self.tweet1 = random.choice(self.usable_tweetlist)
            tweet2 = random.choice(self.usable_tweetlist)
            tweet1_value = tweetdict.get(self.tweet1[-1], 'unknown')
            tweet1_value = tweet1_value.strip("'")
            tweet2_value = tweetdict.get(tweet2[-1], 'unknown')
            tweet2_value = tweet2_value.strip("'")
            """len > 2, anders krijg je twietwiets waarbij ook op ik zou moeten rijmen omdat
            de value, dus de uitspraak vanaf het 2e teken is genomen"""
            if len(tweet2_value) > 2 and len(tweet1_value) > 2:
                if tweet2 != self.tweet1[1:] and tweet2_value[1:] == tweet1_value and tweet2_value != tweet1_value:
                    self.twietwiet.append(self.tweet1[1:])
                    self.twietwiet.append(tweet2[1:])
                else:
                    tweet2 = random.choice(self.usable_tweetlist)
            else:
                tweet2 = random.choice(self.usable_tweetlist)       
        return self.twietwiet
        
        
if __name__ == '__main__':
    twietwiets()
   
    
        


