from father_gui import Ui_MainWindow
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtWidgets
import pymysql


class MyMainWindow(QtWidgets.QMainWindow,Ui_MainWindow):#QWidget是因为创建的是QWidget类，Ui_Form创建窗口Form的objectName
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)




if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = MyMainWindow()
    main.showMaximized()#显示窗口
    sys.exit(app.exec_())