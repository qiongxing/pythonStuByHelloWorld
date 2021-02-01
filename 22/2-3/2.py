import sys
from PyQt4 import QtCore,QtGui,uic
import random

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
        like_file= open("like.txt","w")
        print>>like_file,"姓名："+name
        print>>like_file,"年龄："+str(age)
        print>>like_file,"最喜欢颜色："+color
        print>>like_file,"最喜欢食物："+foot
        like_file.close()
        QtGui.QMessageBox.information(self,"提示","保存成功")


app=QtGui.QApplication(sys.argv)
myWindow= MyWindowClass()
myWindow.show()
app.exec_()