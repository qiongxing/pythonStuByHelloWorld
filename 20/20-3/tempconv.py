import sys
from PyQt4 import QtCore,QtGui,uic

# 记载创建的ui
form_class =uic.loadUiType("tempconv.ui")[0]

class MyWindowClass(QtGui.QMainWindow,form_class):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.btnCtoF.clicked.connect(self.btnCtoFClicked)
        self.btnFtoC.clicked.connect(self.btnFtoCClicked)

    def btnCtoFClicked(self):
        cel = float(self.editCel.text())
        fahr = cel *9.0/5 +32
        self.spinFahr.setValue(int(fahr+0.5))

    def btnFtoCClicked(self):
        fahr = self.spinFahr.value()
        cel = (fahr-32) *5.0/9
        cel_text = '%.2f'%cel
        self.editCel.setText(str(cel_text))

app=QtGui.QApplication(sys.argv)
myWindow= MyWindowClass()
myWindow.show()
app.exec_()
