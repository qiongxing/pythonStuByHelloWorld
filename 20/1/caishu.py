import sys,random
from PyQt4 import QtCore,QtGui,uic

# 记载创建的ui
form_class =uic.loadUiType("caishu.ui")[0]

class MyWindowClass(QtGui.QMainWindow,form_class):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.secret = random.randint(1,99)
        self.guess=0
        self.tries = 0
        self.submit.clicked.connect(self.submitClick)

    def submitClick(self):
        self.guess = self.numberBox.value()
        if self.guess != self.secret and self.tries < 6:
            if self.guess < self.secret:
                self.showLabel.setText("too low")
            elif self.guess > self.secret:
                self.showLabel.setText("too high")
            elif self.guess == self.secret:
                self.showLabel.setText("good!")
        else :
            self.showLabel.setText("no more,"+str(self.secret))
        self.tries+= 1

app=QtGui.QApplication(sys.argv)
myWindow= MyWindowClass()
myWindow.show()
app.exec_()
