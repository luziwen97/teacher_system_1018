
''':var
查看表格键对关系界面
'''
import read_config
from PyQt5.QtWidgets import QDialog
import read_setting
from PyQt5 import QtCore, QtWidgets
import pymysql
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
import sys


class Ui_Dialog_2(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


        self.setupUi()
        # 第一行按钮布局管理
    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
        self.hLayout1 = QHBoxLayout()
        self.hLayout2 = QHBoxLayout()

        self.button_1 = QPushButton("Button1")
        self.button_1.setMinimumSize(60, 30)
        self.button_1.setMaximumSize(120, 30)
        self.button_1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.hLayout1.addWidget(self.button_1)

        self.button_2 = QPushButton("Button2")
        self.button_2.setMinimumSize(60, 30)
        self.button_2.setMaximumSize(120, 30)
        self.button_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.hLayout1.addWidget(self.button_2)



        self.button_1.setText("新增键值对")
        self.button_2.setText("删除")
        self.button_1.clicked.connect(self.btn_1)
        self.button_2.clicked.connect(self.btn_2)
        # 第二行按钮布局管理

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tableWidget.setMinimumSize(200, 800)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['公共键', '关联表1', '关联表2'])  # 字段名
        self.hLayout2.addWidget(self.tableWidget)
        self.init_data()

        # 整体垂直布局管理
        self.layout.addLayout(self.hLayout1)
        self.layout.addLayout(self.hLayout2)

        self.setLayout(self.layout)



    def init_data(self):
        A = read_setting.read_setting_info()
        self.tableWidget.setRowCount(len(A))
        self.tableWidget.setColumnCount(3)  # table表的字段，第0列是键，第1列是表1名，第2列是表2名，

        for i in range(len(A)):
            key_list = list(A[i].keys())
            key = key_list[0]
            value_list = A[i][str(key)]
            name_a = value_list[0]
            name_b = value_list[1]
            key = QtWidgets.QTableWidgetItem(key)
            name_a = QtWidgets.QTableWidgetItem(name_a)
            name_b = QtWidgets.QTableWidgetItem(name_b)
            self.tableWidget.setItem(i, 0, key)
            self.tableWidget.setItem(i, 1, name_a)
            self.tableWidget.setItem(i, 2, name_b)

    def btn_1(self):
        #新增键值对
        '''
        首先获取现在的tablewidget的行数，getRowCount
        然后新增一行，setRowCount(len+1)

        :return:
        '''
        RowCount=self.tableWidget.rowCount()
        print(RowCount)
        self.tableWidget.setRowCount(RowCount+1)
        combox_0 = QtWidgets.QComboBox()
        combox_1 = QtWidgets.QComboBox()
        combox_2 = QtWidgets.QComboBox()
        table_names = read_config.get_table_names()
        for i in table_names:
            combox_1.addItem(i)
            combox_2.addItem(i)
        self.tableWidget.setCellWidget(RowCount, 0, combox_1)
        self.tableWidget.setCellWidget(RowCount, 1, combox_1)
        self.tableWidget.setCellWidget(RowCount, 2, combox_2)

        


    def btn_2(self):
        #删除
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_Dialog_2()
    window.resize(200, 1000)
    window.show()

    sys.exit(app.exec_())








