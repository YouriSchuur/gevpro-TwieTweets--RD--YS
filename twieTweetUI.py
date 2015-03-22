#!/usr/bin/python3
# Youri Schuur & Roy David

import sys
from PyQt4 import QtGui, QtCore
import random



class CreateUI(QtGui.QWidget):
    """ this class creates the UI """
	
    def __init__(self, tweet1, tweet2):
        super(CreateUI, self).__init__()
        self.setWindowTitle('TwieTweets')
        self.setGeometry(500, 100, 500, 500)
        self.tweet1 = tweet1
        self.tweet2 = tweet2
        self.initUI()
        
        
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
    tweet1 = ['this', 'is', 'an', 'example']
    tweet2 = ['these', 'are', 'some', 'random', 'words']
    widget = CreateUI(tweet1, tweet2)
    widget.show()
    sys.exit(app.exec_())
		
	
		
	
