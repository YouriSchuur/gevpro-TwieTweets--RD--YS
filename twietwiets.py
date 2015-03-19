#!usr/bin/python3
#twietwiets.py
#Roy David & Youri Schuur

import sys
from PyQt4 import QtGui, QtCore 
import random
from collections import Counter

class twietwiets(QtGui.QWidget):
	def __init__(self, argv):
		super(twietwiets, self).__init__()
		self.setWindowTitle("TwieTwiets")
		self.setGeometry(400, 400, 400, 400)
		self.tweetsfile = open(argv[1])
		self.initUI()
		
	def initUI(self):
		self.grid = QtGui.QGridLayout()
		self.tweetLabel = QtGui.QLabel()
		self.tweetButton = QtGui.QPushButton("Tweet", self)
		self.tweetButton.clicked.connect(self.buttonPushed)
		self.grid.addWidget(self.tweetLabel, 1, 0)
		self.grid.addWidget(self.tweetButton, 1, 4)
		
		
	def buttonPushed(self):
		source = self.sender()
		if source.text() == "Tweet":
			for tweet in self.get_tweets():
				self.grid.addWidget(QtGui.QLabel(str(tweet)))
		self.setLayout(self.grid)
			#self.tweetLabel.setText(tweets.inputTweet())
			
	def get_tweets(self):
		tweets = []
		for line in self.tweetsfile:
			tweets.append(line.split("\n"))
		return random.choice(tweets)
		
	#def clean_tweets(self):
		#for tweet in self.get_tweets():	
		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	twiets = twietwiets(sys.argv)
	twiets.show()
	app.exec_()
