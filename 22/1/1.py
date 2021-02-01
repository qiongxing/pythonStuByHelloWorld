import sys
from PyQt4 import QtCore,QtGui,uic
import random

# 记载创建的ui
form_class =uic.loadUiType("create.ui")[0]

def getWord(words):
    return random.choice(words)

class MyWindowClass(QtGui.QMainWindow,form_class):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        adj = open("adj.txt","r")
        self.adj= adj.readlines()[0]
        adj.close()
        adv = open("adv.txt","r")
        self.adv= adv.readlines()[0]
        adv.close()
        lv = open("lv.txt","r")
        self.lv= lv.readlines()[0]
        lv.close()
        noun = open("noun.txt","r")
        self.noun= noun.readlines()[0]
        noun.close()

        self.btnCreate.clicked.connect(self.btn_cleat_click)

    def btn_cleat_click(self):
        self.adjectiveLine.setText(getWord(self.adj.split(",")))
        self.nounLine.setText(getWord(self.noun.split(",")))
        self.advSLine.setText(getWord(self.adv.split(",")))
        self.lvLine.setText(getWord(self.lv.split(",")))



app=QtGui.QApplication(sys.argv)
myWindow= MyWindowClass()
myWindow.show()
app.exec_()
