import sys
from PyQt4 import QtCore,QtGui,uic

# 记载创建的ui
form_class =uic.loadUiType("tempconv-menu.ui")[0]

class MyWindowClass(QtGui.QMainWindow,form_class):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.btnCtoF.clicked.connect(self.btnCtoFClicked)
        self.btnFtoC.clicked.connect(self.btnFtoCClicked)
        self.actionF_To_C.triggered.connect(self.btnFtoCClicked)
        self.actionC_To_F.triggered.connect(self.btnCtoFClicked)
        self.actionExit.triggered.connect(self.menuExit_selected)

    def btnCtoFClicked(self):
        cel = float(self.editCel.text())
        fahr = cel *9.0/5 +32
        self.spinFahr.setValue(int(fahr+0.5))

    def btnFtoCClicked(self):
        fahr = self.spinFahr.value()
        cel = (fahr-32) *5.0/9
        cel_text = '%.2f'%cel
        self.editCel.setText(str(cel_text))

    def menuExit_selected(self):
        self.close()
app=QtGui.QApplication(sys.argv)
myWindow= MyWindowClass()
myWindow.show()
app.exec_()
