#-*- encoding = utf-8 -*-
import hashlib
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from Windows.MainWindow import Ui_MainWindow


class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        self.exit_btn.clicked.connect(lambda :sys.exit())
        self.encry_btn.clicked.connect(self.encry)
        self.file_btn.clicked.connect(self.file_choose)
        self.clear_btn.clicked.connect(lambda :self.original_text.setText(''))
    def encry(self):
        text=self.original_text.toPlainText()
        result=hashlib.md5(text.encode()).hexdigest()
        self.res_shower.setText(result)
        print("[==>加密成功<==]\n|{%s}==>{%s}|"%(text,result))

    def file_choose(self):
        filename,filetype=QFileDialog.getOpenFileName(self,"打开文件","/","文本文件(*.txt);全部文件(*.*)")
        if filename!="":
            f=open(filename,'r',encoding='utf-8')
            text=f.read()
            self.original_text.setText(text)
            self.encry()

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    ui=MyWindow()
    ui.show()
    sys.exit(app.exec_())