
''':var
查看表格键对关系界面
'''
import read_config
from PyQt5.QtWidgets import QDialog
import read_setting
from PyQt5 import QtCore, QtWidgets
import pymysql
from PyQt5.QtWidgets import *




class Ui_Dialog_2(object):
    def __init__(self):
        pass

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(50, 50, 100, 40))
        self.label_1.setObjectName("关联表1:")

        self.comboBox_1 = QtWidgets.QComboBox(Dialog)
        self.comboBox_1.setGeometry(QtCore.QRect(155, 50, 200, 40))
        self.comboBox_1.setObjectName("sheet选择盒")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(355, 50, 100, 40))
        self.label_2.setObjectName("表1公共键:")

        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(460, 50, 200, 40))
        self.comboBox_2.setObjectName("sheet选择盒")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 100, 40))
        self.label_3.setObjectName("关联表2:")

        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(155, 100, 200, 40))
        self.comboBox_3.setObjectName("sheet选择盒")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(355, 100, 100, 40))
        self.label_4.setObjectName("表2公共键:")

        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(460, 100, 200, 40))
        self.comboBox_4.setObjectName("sheet选择盒")

        self.button_1 = QtWidgets.QPushButton(Dialog)
        self.button_1.setGeometry(QtCore.QRect(665, 50, 95, 95))
        self.button_1.setObjectName("新增")

        self.button_2 = QtWidgets.QPushButton(Dialog)
        self.button_2.setGeometry(QtCore.QRect(410, 155, 200, 40))
        self.button_2.setObjectName("删除")

        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(200, 155, 200, 40))
        self.comboBox_5.setObjectName("sheet选择盒")

        self.tableWidget=QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(100, 210, 600, 350))
        self.tableWidget.setObjectName("tableWidget")


        self.button_1.setText("新增")
        self.button_2.setText("删除")

        self.label_1.setText("关联表1:")
        self.label_2.setText("表1公共键:")
        self.label_3.setText("关联表2:")
        self.label_4.setText("表2公共键:")

        self.label_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)

        self.comboBox_1.activated[str].connect(self.combobox_1)
        self.comboBox_2.activated[str].connect(self.combobox_2)
        self.comboBox_3.activated[str].connect(self.combobox_3)
        self.comboBox_4.activated[str].connect(self.combobox_4)
        #self.comboBox_5.activated[str].connect(self.combobox_5)
        self.btn_3()
        table_names=read_config.get_table_names()
        for i in table_names:
            self.comboBox_1.addItem(i)
            self.comboBox_3.addItem(i)

        self.button_1.clicked.connect(self.btn_1)
        self.button_2.clicked.connect(self.btn_2)

        A = read_setting.get_sections()
        A = A[1:]
        for i in A:
            self.comboBox_5.addItem(str(i))
    def combobox_1(self,text):
        self.comboBox_2.clear()
        columns_name=read_config.get_columns_names(text)
        for i in columns_name:
            self.comboBox_2.addItem(i)

        pass
    def combobox_2(self):
        pass
    def combobox_3(self,text):
        self.comboBox_4.clear()
        columns_name = read_config.get_columns_names(text)
        for i in columns_name:
            self.comboBox_4.addItem(i)
        pass
    def combobox_4(self):
        pass
    def btn_1(self):
        if self.comboBox_2.currentText()==self.comboBox_4.currentText():
            if self.comboBox_1.currentText!=self.comboBox_3.currentText():

                key = self.comboBox_2.currentText()
                table_a = self.comboBox_1.currentText()
                table_b = self.comboBox_3.currentText()
                if key != "" and table_a != "" and table_b != "":
                    read_setting.write_setting(key, table_a, table_b)
                    QMessageBox.information(None, "提示", "新键值对添加成功")
                    self.btn_3()
                    self.comboBox_5.clear()
                    A = read_setting.get_sections()
                    A = A[1:]
                    for i in A:
                        self.comboBox_5.addItem(str(i))
            else:
                QMessageBox.information(None, "提示", "关联表一致")
        else:
            QMessageBox.information(None, "提示", "公共键不一致")


    def btn_2(self):
        self.msg = QMessageBox()
        self.msg.setStandardButtons(self.msg.Yes | self.msg.No)
        self.msg.setIcon(self.msg.Question)
        self.msg.setText("确定删除这个键值对?")
        self.msg.buttonClicked.connect(self.msgbtn)
        self.msg.exec_()

    def msgbtn(self, i):
        a = i.text().strip("&")
        if a == "Yes":
            text = str(self.comboBox_5.currentText())
            read_setting.remove_section(text)
            self.comboBox_5.clear()
            A = read_setting.get_sections()
            A = A[1:]
            for i in A:
                self.comboBox_5.addItem(str(i))
            self.btn_3()

    def btn_3(self):
        A= read_setting.read_setting_info()
        self.tableWidget.setRowCount(len(A))
        self.tableWidget.setColumnCount(3)  #table表的字段，第0列是键，第1列是表1名，第2列是表2名，

        for i in range(len(A)):
            key_list=list(A[i].keys())
            key = key_list[0]
            value_list = A[i][str(key)]
            name_a=value_list[0]
            name_b=value_list[1]
            key=QtWidgets.QTableWidgetItem(key)
            name_a = QtWidgets.QTableWidgetItem(name_a)
            name_b = QtWidgets.QTableWidgetItem(name_b)
            self.tableWidget.setItem(i,0,key)
            self.tableWidget.setItem(i, 1, name_a)
            self.tableWidget.setItem(i, 2, name_b)







