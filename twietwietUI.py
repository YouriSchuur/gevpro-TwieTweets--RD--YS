#!/usr/bin/python3
# Youri Schuur & Roy David

import sys
from PyQt4 import QtGui, QtCore
import random
import twietwiets


class CreateUI(QtGui.QWidget):
    """ this class creates the UI """
	
    def __init__(self, tweet1, tweet2):
        super(CreateUI, self).__init__()
        self.setWindowTitle('TwieTwiets')
        self.setGeometry(500, 100, 500, 500)
        self.tweet1 = tweet1
        self.tweet2 = tweet2
        self.initUI()
        
    def initUI(self):
        """ create labels and buttons """
        self.tweetButton = QtGui.QPushButton('Start', self)
        self.twieTweetButton = QtGui.QPushButton('New TwieTweet', self)
        self.textBox = QtGui.QTextEdit()
        self.layout = QtGui.QGridLayout()
        self.layout.addWidget(self.tweetButton, 7, 0)
        self.layout.addWidget(self.twieTweetButton, 8, 0)
        self.layout.addWidget(self.textBox, 0, 0)
        self.textBox.setReadOnly(True)
        self.tweetButton.clicked.connect(self.clickedSignal)
        self.twieTweetButton.clicked.connect(self.clickedSignal)
        self.setLayout(self.layout)
        
    def clickedSignal(self):
        """Shows the results, sends the signals to the textBox"""
        source = self.sender()
        self.textBox.clear()
        if source.text() == 'Start':
            twietwiet = ' '.join(str(twietwiet) for twietwiet in self.tweet1)
            self.textBox.append('TwieTwiet: \n\n{}'.format(twietwiet))
            twietwiet = ' '.join(str(twietwiet) for twietwiet in self.tweet2)
            self.textBox.append('\n{}\n\n\n\nWil je een nieuwe TwieTwiet? Klik dan op New TwieTwiet!'.format(twietwiet))
            
        """Roept twietwiets.py aan, en laat elke keer de nieuwe tweet en twieTweet zien"""
        if source.text() == 'New TwieTweet':
            twieTweet_new = twietwiets.twietwiets()
            self.tweet1 = twieTweet_new.twietwiet[0]
            self.tweet2 = twieTweet_new.twietwiet[1]
            twietwiet = ' '.join(str(twietwiet) for twietwiet in self.tweet1)
            self.textBox.append('TwieTwiet: \n\n{}'.format(twietwiet))
            twietwiet = ' '.join(str(twietwiet) for twietwiet in self.tweet2)
            self.textBox.append('\n{}\n\n\n\nWil je nog een nieuwe TwieTwiet? Klik dan weer op New TwieTwiet!'.format(twietwiet))
                
                
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    twieTweet = twietwiets.twietwiets()
    tweet1 = twieTweet.twietwiet[0]
    tweet2 = twieTweet.twietwiet[1]
    widget = CreateUI(tweet1, tweet2)
    widget.show()
    sys.exit(app.exec_())
		
	
		
	
