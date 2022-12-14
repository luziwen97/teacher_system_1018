# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
import sys,time
from PyQt5.QtCore import  Qt
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 719)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 30, 721, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(810, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(810, 120, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(810, 160, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(810, 200, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.openConn()
        self.load_widget()
        self.pushButton.clicked.connect(self.edit)
        self.pushButton_2.clicked.connect(self.add)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))

    def openConn(self):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('abc.db')
            if db.open():
                print('?????????????????????')
            else:
                print('?????????????????????:' + db.lastError().text())
        except Exception as e:
            print(e.args)

    def sel(self,sql):
        sqlmodel=QtSql.QSqlQueryModel()
        sqlmodel.setQuery(sql)
        rows=sqlmodel.rowCount()
        columns=sqlmodel.columnCount()
        print(rows,columns)
        for i in range(rows):
            for j in range(columns):
                newItem=QtWidgets.QTableWidgetItem(str( sqlmodel.record(i).value(j)))
                self.tableWidget.setItem(i,j,newItem)

    def load_widget(self):
        self.tableWidget.horizontalHeader().setVisible(True)#??????
        self.tableWidget.verticalHeader().setVisible(False) #??????
        self.tableWidget.setSortingEnabled(True)#?????????
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)#??????
        self.tableWidget.setRowCount(10)#??????
        self.tableWidget.setColumnCount(10)#??????
        self.tableWidget.setHorizontalHeaderLabels(['id','date','name','content','num','msg','enable']) #?????????
        self.sel('select * from table1') #??????

        combox=QtWidgets.QComboBox()
        combox.addItem('xxx')
        self.tableWidget.setCellWidget(0,1,combox)

        check=QtWidgets.QCheckBox()
        check.setText('?????????')#??????
        check.setEnabled(True) #????????????
        check.setCheckState(QtCore.Qt.Unchecked) #???????????????
        self.tableWidget.setCellWidget(0,2,check)

        self.tableWidget.setIconSize(QtCore.QSize(150,150)) #??????ico??????
        self.tableWidget.setRowHeight(1, 150)
        self.tableWidget.setColumnWidth(1, 150)
        image=QtWidgets.QTableWidgetItem()
        image.setFlags(QtCore.Qt.ItemIsEnabled) #???????????????
        image.setIcon(QtGui.QIcon('../res/a.jpg'))

        self.tableWidget.setItem(1,1,image)
        self.btn=QtWidgets.QPushButton()
        self.btn.setText('save')
        self.btn.clicked.connect(self.add)
        self.tableWidget.setCellWidget(0,4,self.btn)#??????

        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background:yellow;}")
        #??????????????????
        for i in range(self.tableWidget.rowCount()):
            item0=QtWidgets.QTableWidgetItem(self.tableWidget.item(i,0)) #???????????????????????????
            item0.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(i,0,item0) #??????????????????

    def edit(self):

        index=self.tableWidget.currentIndex()
        rows=self.tableWidget.currentRow()
        columns=self.tableWidget.currentColumn()
        print(rows,columns)


    def add(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())




if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    mainwindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
