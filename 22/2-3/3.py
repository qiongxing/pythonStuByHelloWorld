import sys,pickle
from PyQt4 import QtCore,QtGui,uic

# 记载创建的ui
form_class =uic.loadUiType("like.ui")[0]

class MyWindowClass(QtGui.QMainWindow,form_class):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)

        self.btnSave.clicked.connect(self.save)

    def save(self):
        name = self.nameEdit.text()
        age = self.ageBox.text()
        color = self.colorEdit.text()
        foot = self.footEdit.text()
        saveFile=open("pickleList.pkl","w")
        saveList = [name,age,color,foot]
        pickle.dump(saveList,saveFile)
        saveFile.close()
        QtGui.QMessageBox.information(self,"提示","保存成功")


app=QtGui.QApplication(sys.argv)
myWindow= MyWindowClass()
myWindow.show()
app.exec_()