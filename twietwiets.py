#!/usr/bin/python3
#twietwiets.py
#Roy David & Youri Schuur

import sys
from PyQt4 import QtGui, QtCore
import random

class twietwiets(QtGui.QWidget):
    """This program creates twietwiets from tweet.txt using dpw.cd
    (a dutch pronounciation dictionairy)"""

    def __init__(self, tweet1, tweet2):
        super(twietwiets, self).__init__()
        self.setWindowTitle('TwieTweets')
        self.setGeometry(500, 100, 500, 500)
        self.tweet1 = tweet1
        self.tweet2 = tweet2
        tweet1 = self.usable_tweetlist
        tweet2 = self.twietwiet
        self.initUI()
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
            tweet1 = random.choice(self.usable_tweetlist)
            tweet2 = random.choice(self.usable_tweetlist)
            tweet1_value = tweetdict.get(tweet1[-1], 'unknown')
            tweet1_value = tweet1_value.strip("'")
            tweet2_value = tweetdict.get(tweet2[-1], 'unknown')
            tweet2_value = tweet2_value.strip("'")
            """len > 2, anders krijg je twietwiets waarbij ook op ik zou moeten rijmen omdat
            de value, dus de uitspraak vanaf het 2e teken is genomen"""
            if len(tweet2_value) > 2 and len(tweet1_value) > 2:
                if tweet2 != tweet1 and tweet2_value[1:] == tweet1_value[1:] and tweet2_value != tweet1_value:
                    self.twietwiet.append(tweet1)
                    self.twietwiet.append(tweet2)
                else:
                    tweet2 = random.choice(self.usable_tweetlist)
            else:
                tweet2 = random.choice(self.usable_tweetlist)
        return self.twietwiet

	
   
        
    def initUI(self):
        """ create labels and buttons """
        self.tweetButton = QtGui.QPushButton('New Tweet', self)
        self.twieTweetButton = QtGui.QPushButton('New twieTweet', self)
        self.textBox = QtGui.QTextEdit()
        self.layout = QtGui.QGridLayout()
        self.layout.addWidget(self.tweetButton, 7, 0)
        self.layout.addWidget(self.twieTweetButton, 8, 0)
        self.layout.addWidget(self.textBox, 0, 0)
        self.tweetButton.clicked.connect(self.clickedSignal)
        self.twieTweetButton.clicked.connect(self.clickedSignal)
        self.setLayout(self.layout)
        
    def clickedSignal(self):
        source = self.sender()
        self.textBox.clear()
        if source.text() == 'New Tweet':
            self.textBox.append('Tweet: {:>10}'.format(random.choice(self.tweet1)))
                 
        else:
            self.textBox.append('TwieTweet: {:>10}'.format(random.choice(self.tweet2)))
        
if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    
    twietwiets()
    widget = twietwiets(QtGui.QWidget)
    widget.show()
    sys.exit(app.exec_())
        


