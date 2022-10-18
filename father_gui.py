
import pymysql
import read_config
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import *
from PyQt5 import QtCore,  QtWidgets
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import pandas as pd
import read_setting
from childgui_1 import Ui_Dialog_1
from childgui_2 import Ui_Dialog_2

import os

class childWindow_1(QDialog):
    #数据导入界面实例化
    def __init__(self):
        super().__init__()
        QDialog.__init__(self)
        self.child = Ui_Dialog_1()
        self.child.setupUi(self)

class childWindow_2(QDialog):
    #查看关系键对界面实例化
    def __init__(self):
        super().__init__()
        QDialog.__init__(self)
        self.child = Ui_Dialog_2()
        self.child.setupUi(self)



class PdTable(QAbstractTableModel):
    # 显示df的table_view，主界面下方表格
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    # 显示数据
    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    # 显示行和列头
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.axes[0][col]
        return None

#GUI主界面布局及控件相关
class Ui_MainWindow(object):
    def __init__(self):
        self.cwd = os.getcwd()
        self.db=None
        self.host=None
        self.port=None
        self.user=None
        self.password=None
        self.database=None
        self.charset=None

        self.df_list=[]
        self.chose_tabel=[]
        self.main_table="教师"

        self.df_ok=None



    def setupUi(self, MainWindow):
        #ui设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1445, 913)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(300, 50, 200, 50))
        self.button_2.setObjectName("数据新增")

        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(500, 50, 200, 50))
        self.button_3.setObjectName("查看键值对关系")

        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(700, 50, 200, 50))
        self.button_4.setObjectName("刷新数据及键值对")

        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(900, 50, 200, 50))
        self.button_5.setObjectName("数据导出")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(1250, 50, 200, 50))
        self.label_1.setObjectName("label")

        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(1150, 100, 291, 31))
        self.comboBox_1.setObjectName("sheet选择器")

        self.listWidget_1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_1.setGeometry(QtCore.QRect(1150, 140, 291, 200))
        self.listWidget_1.setObjectName("listWidget_1")

        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(1150, 350, 291, 300))
        self.listWidget_2.setObjectName("listWidget_2")

        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(1150, 660, 291, 200))
        self.listWidget_3.setObjectName("listWidget_3")

        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(1200, 870, 200, 50))
        self.button_6.setObjectName("绘制表格")

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(100, 120, 1000, 800))
        self.tableView.setObjectName("表格显示窗口")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1445, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        #ui控件逻辑关联
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


        self.button_2.setText(_translate("MainWindow", "数据新增"))
        self.button_3.setText(_translate("MainWindow", "查看表格关系键对"))
        self.button_4.setText(_translate("MainWindow", "刷新数据及键值对"))
        self.button_5.setText(_translate("MainWindow", "数据表格导出成Excel"))
        self.button_6.setText(_translate("MainWindow", "绘制表格"))
        self.label_1.setText(_translate("MainWindow", "数据库内数据表"))


        self.button_2.clicked.connect(self.btn_2)
        self.button_3.clicked.connect(self.btn_3)
        self.button_4.clicked.connect(self.btn_4)
        self.button_5.clicked.connect(self.btn_5)
        self.button_6.clicked.connect(self.btn_6)
        self.comboBox_1.activated[str].connect(self.combox_1)
        self.listWidget_1.itemClicked.connect(self.listwidget_1)





    def btn_2(self):
        #调出数据新增界面
        child_window = childWindow_1()
        child_window.exec_()



        pass
    def btn_3(self):
        #调出键值对关系
        child_window = childWindow_2()
        child_window.exec_()
        self.btn_4()
        #查看表格关系键对
        pass

    def btn_4(self):
        #刷新数据及键对
        try:
            self.comboBox_1.clear()
            self.listWidget_1.clear()
            self.listWidget_2.clear()
            self.listWidget_3.clear()
            model = PdTable(pd.DataFrame([]))
            self.tableView.setModel(model)
            self.tablenames = read_config.get_table_names()

            for i in self.tablenames:
                self.comboBox_1.addItem(str(i))

            self.relation_ship = read_setting.read_setting_for_father_gui()
            self.relation_ship_keys_list = list(self.relation_ship.keys())
            self.relation_ship_values_list = list(self.relation_ship.values())
        except Exception as reason:
            print("btn_5问题原因%s" % reason)



    def btn_5(self):
        #数据表格导出成EXCEL
        try:
            fileName_save = QFileDialog.getSaveFileName(self,
                                                        "文件保存",
                                                        self.cwd,  # 起始路径
                                                        "Excel Files (*.xlsx)")  # 设置文件扩展名过滤,用双分号间隔)

            print(fileName_save[0])
            print(self.df_ok)
            if str(fileName_save[0]) != "":
                self.df_ok.to_excel(str(fileName_save[0]), sheet_name="sheet1", index=False)
                QMessageBox.information(None, "提示", "表格导出成功")
            if str(fileName_save[0]) == "":
                QMessageBox.information(None, "提示", "没有保存数据,请重新保存。")  # 调用弹窗提示
                return fileName_save[0]
        except Exception as reason:
            print("btn_5问题原因%s"%reason)



    def btn_6(self):
        try:
            # 绘制表格
            widgetres = []
            # 获取listwidget中条目数
            count = self.listWidget_2.count()
            # 遍历listwidget中的内容
            for i in range(count):
                widgetres.append(self.listWidget_2.item(i).text())
            df_0 = pd.DataFrame([])

            for i in range(len(self.df_list)):
                if i == 0:
                    df_0 = self.df_list[i]
                elif i >= 0:
                    df_0 = pd.merge(df_0, self.df_list[i], on='教师ID', suffixes=("", "_"))
            df = df_0[widgetres]
            model = PdTable(df)
            self.tableView.setModel(model)
            self.df_ok = df
        except Exception as reason:
            print("绘制表格错误原因:%s"%reason)



    def combox_1(self,item):
        # 选取数据库中选择的表的所有列名，然后显示在listwidget1中
        try:
            self.listWidget_1.clear()  # 清除列名表

            columnsnames = read_config.get_columns_names(str(item))  # 获取所选表在sql中对应的所有列名

            print(columnsnames)
            print(self.relation_ship_values_list)
            exist = 0
            print(len(self.relation_ship_values_list))
            for i in range(len(self.relation_ship_values_list)):
                print(i)
                print("exist:%s" % exist)
                print(self.relation_ship_values_list[i])
                if str(item) in self.relation_ship_values_list[i] or item == "教师":
                    exist = 1
                    for i in columnsnames:
                        self.listWidget_1.addItem(str(i))
                    break
                if i == len(self.relation_ship_values_list) - 1 and exist == 0:
                    QMessageBox.information(None, "提示", "这是一张新表             \n请先添加: 键值对 \n这次就不通报批评了！")
        except Exception as reason:
            print("comboBox1出错原因是%s"%reason)




    def listwidget_1(self,item):
        ''':var
        获取listwidget2和listwidget中的条目名

        '''
        try:


            exist=0
            # 选取list1中的列名添加进list3中用于merge,并将所用到的表格添加到list2中
            # 获取listwidget_2中所有的列名
            widgetres2 = []
            widgetres3 = []

            # 获取listwidget中条目数
            count = self.listWidget_2.count()
            # 遍历listwidget中的内容
            for i in range(count):
                widgetres2.append(self.listWidget_2.item(i).text())

            # 获取listwidget中条目数
            count = self.listWidget_3.count()
            # 遍历listwidget中的内容
            for i in range(count):
                widgetres3.append(self.listWidget_3.item(i).text())

            self.tablenames = read_config.get_table_names()  # 获取sql中所有表名

            print(widgetres3)
            print(widgetres2)
            print(item.text())
            print(self.relation_ship_values_list)
            # 判断listwidget_1当前点击的字段名在listwidget_2中是否存在，存在提示，不存在则添加
            table = read_config.get_table_names()

            if item.text() in widgetres2:
                QMessageBox.information(None, "ListWidget", item.text() + "已存在")  # 显示出消息提示框
            else:
                # 如果不存在list2中，判断是否存在键值对里，或者是否为主表
                for i in range(len(self.relation_ship_values_list)):
                    if self.comboBox_1.currentText() in self.relation_ship_values_list[i] :
                        exist=1
                        # 判断是否存在键值对里相关的表，如果是
                        if self.comboBox_1.currentText() not in widgetres3:
                            #判断表是否在listwidget3中，如果不在
                            df1_name = self.relation_ship_values_list[i][0]
                            df2_name = self.relation_ship_values_list[i][1]

                            if df1_name in table and df2_name in table:
                                #判断是否在数据库里

                                self.listWidget_3.addItem(self.comboBox_1.currentText())
                                self.listWidget_2.addItem(item.text())

                                key = self.relation_ship_keys_list[i]
                                df1 = read_config.get_table(str(df1_name))
                                df2 = read_config.get_table(str(df2_name))

                                widgetres3 = []
                                # 获取listwidget中条目数
                                count = self.listWidget_3.count()
                                # 遍历listwidget中的内容
                                for i in range(count):
                                    widgetres3.append(self.listWidget_3.item(i).text())

                                if  df1_name in widgetres3 and df2_name in widgetres3:
                                    print("重复merge")

                                else:
                                    df = pd.merge(df1, df2, on=str(key), suffixes=("", "_"))
                                    self.df_list.append(df)
                                    print(self.df_list)
                                self.chose_tabel.append(self.comboBox_1.currentText())
                                QMessageBox.information(None, "ListWidget",
                                                        "你选择了: %s;" % str(item.text()) + "\n你引用了: %s;" % str(
                                                            self.comboBox_1.currentText()))  # 显示出消息提示框
                            else:
                                QMessageBox.information(None, "提示", "有张关联表不再数据库里")
                        else:
                            self.listWidget_2.addItem(item.text())
                            QMessageBox.information(None, "ListWidget",
                                                    "你选择了: %s;" % str(item.text()) + "\n你引用了: %s;" % str(
                                                        self.comboBox_1.currentText()))  # 显示出消息提示框

                # 如果不存在键值对里判断是否为主表
                if self.comboBox_1.currentText() == self.main_table:
                    exist = 1
                    if self.comboBox_1.currentText() not in widgetres3:
                        self.listWidget_3.addItem(self.comboBox_1.currentText())
                    else:
                        pass

                    self.listWidget_2.addItem(item.text())
                    df = read_config.get_table(self.comboBox_1.currentText())
                    self.df_list.append(df)
                    QMessageBox.information(None, "ListWidget",
                                            "你选择了: %s;" % str(item.text()) + "\n你引用了: %s;" % str(
                                                self.comboBox_1.currentText()))  # 显示出消息提示框
                if exist == 0:
                    # 如果不存在键值对也不是主表
                    # 请先添加键值对
                    QMessageBox.information(None, "提示", "请先添加键值对，这张表不在键值对中")
            pass
        except Exception as reason:
            print("listWidget1报错原因是%s:" %reason)
