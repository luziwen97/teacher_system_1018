
''':var
数据库的增删改查操作
'''
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import os
import pandas as pd
from PyQt5.QtWidgets import QMessageBox
import read_config

class Ui_Dialog_1(object):
    def __init__(self):
        self.cwd = os.getcwd()
        super(Ui_Dialog_1, self).__init__()
        self.excel_location=None    #excel表位置
        self.pv=0
        self.data_types=["文本型",'日期型','整数型','小数型']
        self.df_toshow=None

    def setupUi(self, Dialog):
        #===============================GUI设计======================
        Dialog.setObjectName("Dialog")
        Dialog.resize(1600, 800)

        #读取数据表button
        self.button_1=QtWidgets.QPushButton(Dialog)
        self.button_1.setGeometry(QtCore.QRect(10, 30, 130, 40))
        self.button_1.setObjectName("读取新的数据表")


        #选择sheet
        self.label_1=QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(10, 80, 80, 40))
        self.label_1.setObjectName("选择sheet")

        #sheet选择盒子
        self.comboBox_1=QtWidgets.QComboBox(Dialog)
        self.comboBox_1.setGeometry(QtCore.QRect(100, 80, 200, 40))
        self.comboBox_1.setObjectName("sheet选择盒")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 125, 80, 40))
        self.label_2.setObjectName("公共键")

        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 125, 200, 40))
        self.comboBox_2.setObjectName("公共键选择盒子")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 215, 80, 40))
        self.label_3.setObjectName("选择字段")

        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(100, 215, 200, 40))
        self.comboBox_3.setObjectName("字段选择盒子")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 80, 40))
        self.label_4.setObjectName("选择数据类型")

        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(100, 260, 200, 40))
        self.comboBox_4.setObjectName("选择数据类型")

        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(100, 650, 200, 40))
        self.comboBox_5.setObjectName("数据类型选择盒子")

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 80, 40))
        self.label_7.setObjectName("次主键——label")

        self.comboBox_6 = QtWidgets.QComboBox(Dialog)
        self.comboBox_6.setGeometry(QtCore.QRect(100, 170, 200, 40))
        self.comboBox_6.setObjectName("次主键选择盒子")


        self.button_2 = QtWidgets.QPushButton(Dialog)
        self.button_2.setGeometry(QtCore.QRect(60, 310, 200, 40))
        self.button_2.setObjectName("添加按钮")


        self.tableView_2=QtWidgets.QTableView(Dialog)
        self.tableView_2.setObjectName("excel数据表信息展示")
        self.tableView_2.setGeometry(QtCore.QRect(350,80,800,320))


        self.button_3 = QtWidgets.QPushButton(Dialog)
        self.button_3.setGeometry(QtCore.QRect(10, 700, 290, 40))
        self.button_3.setObjectName("数据展现")

        self.button_4 = QtWidgets.QPushButton(Dialog)
        self.button_4.setGeometry(QtCore.QRect(10, 650, 80, 40))
        self.button_4.setObjectName("连接数据库")


        self.button_5 = QtWidgets.QPushButton(Dialog)
        self.button_5.setGeometry(QtCore.QRect(10, 750, 290, 40))
        self.button_5.setObjectName("进行数据库更新")


        self.tableView_1 = QtWidgets.QTableView(Dialog)
        self.tableView_1.setObjectName("字段及数据类型展示")
        self.tableView_1.setGeometry(QtCore.QRect(10, 360, 300, 280))

        self.tableView_3 = QtWidgets.QTableView(Dialog)
        self.tableView_3.setObjectName("表信息内容展示")
        self.tableView_3.setGeometry(QtCore.QRect(350,410,800,300))

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(400, 30, 500, 40))
        self.label_5.setObjectName("选择表位置")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(380, 720, 100, 30))
        self.label_6.setObjectName("进度")


        self.button_6 = QtWidgets.QPushButton(Dialog)
        self.button_6.setGeometry(QtCore.QRect(1210, 20, 290, 40))
        self.button_6.setObjectName("完整表格导入数据库")

        self.button_7 = QtWidgets.QPushButton(Dialog)
        self.button_7.setGeometry(QtCore.QRect(930, 30, 200, 40))
        self.button_7.setObjectName("清除")

        self.listWidget_1 = QtWidgets.QListWidget(Dialog)
        self.listWidget_1.setGeometry(QtCore.QRect(1210, 80, 290, 500))
        self.listWidget_1.setObjectName("表格sheet名展示")

        self.button_8 = QtWidgets.QPushButton(Dialog)
        self.button_8.setGeometry(QtCore.QRect(1210, 600, 290, 40))
        self.button_8.setObjectName("读取新的数据表")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(1210, 650, 90, 40))
        self.label_8.setObjectName("选择数据类型")

        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(1210, 700, 90, 40))
        self.label_9.setObjectName("选择数据类型")

        self.comboBox_7 = QtWidgets.QComboBox(Dialog)
        self.comboBox_7.setGeometry(QtCore.QRect(1310, 650, 190, 40))
        self.comboBox_7.setObjectName("选择进行匹配的excel表")

        self.comboBox_8 = QtWidgets.QComboBox(Dialog)
        self.comboBox_8.setGeometry(QtCore.QRect(1310, 700, 190, 40))
        self.comboBox_8.setObjectName("选择进行数据匹配的数据库")

        self.button_9 = QtWidgets.QPushButton(Dialog)
        self.button_9.setGeometry(QtCore.QRect(1210, 750, 290, 40))
        self.button_9.setObjectName("读取新的数据表")
        self.pgb = QtWidgets.QProgressBar(Dialog)
        self.pgb.move(50, 50)
        self.pgb.resize(250, 20)
        self.pgb.setGeometry(QtCore.QRect(480, 720, 680, 30))
        self.pgb.setMinimum(0)
        self.pgb.setMaximum(100)
        self.pv = 0
        self.pgb.setValue(self.pv)



        #===================================GUI文本设置及控件逻辑连接=================
        self.button_1.setText("读取新的数据表")
        self.button_2.setText("添加")
        self.button_3.setText("展现数据")
        self.button_4.setText("连接数据库")
        self.button_5.setText("进行数据更新")
        self.button_6.setText("完整表导入数据库")
        self.button_7.setText("清空操作")
        self.button_8.setText("选择数据表及连接数据库")
        self.button_9.setText("进行ID匹配")


        self.label_1.setText("选择sheet:")
        self.label_2.setText("公共键:")
        self.label_3.setText("选择字段:")
        self.label_4.setText("选择数据类型:")
        self.label_5.setText("选择的表为:")
        self.label_6.setText("进度:")
        self.label_7.setText("次主键:")
        self.label_8.setText("选择进行匹配的表:")
        self.label_9.setText("选择进行匹配的数据库:")


        self.label_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.comboBox_1.activated[str].connect(self.combobox_1)
        self.comboBox_2.activated[str].connect(self.combobox_2)
        self.comboBox_3.activated[str].connect(self.combobox_3)
        self.comboBox_4.activated[str].connect(self.combobox_4)
        self.comboBox_5.activated[str].connect(self.combobox_5)
        #self.comboBox_6.activated[str].connect(self.combobox_6)
        self.comboBox_7.activated[str].connect(self.combobox_7)
        self.comboBox_8.activated[str].connect(self.combobox_8)
        self.button_1.clicked.connect(self.btn_1)
        self.button_2.clicked.connect(self.btn_2)
        self.button_3.clicked.connect(self.btn_3)
        self.button_4.clicked.connect(self.btn_4)
        self.button_5.clicked.connect(self.btn_5)
        self.button_6.clicked.connect(self.btn_6)

        self.button_7.clicked.connect(self.btn_7)
        self.button_8.clicked.connect(self.btn_8)
        self.button_9.clicked.connect(self.btn_9)
        self.listWidget_1.itemClicked.connect(self.listwidget_1)
        for i in self.data_types:

            self.comboBox_4.addItem(i)

            #==============================以下是控件逻辑代码===============================



    def combobox_1(self):
        #根据选择的的sheet,读取表格，并且讲目录传参给公共键及选择的字段
        try:
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            self.comboBox_6.clear()
            df = pd.read_excel(str(self.label_5.text()), sheet_name=str(self.comboBox_1.currentText()))
            self.column_type_df = pd.DataFrame([], columns=['列名', "数据类型"])
            model = PdTable(pd.DataFrame([]))
            self.tableView_1.setModel(model)
            self.tableView_2.setModel(model)
            list_columns = df.columns.to_list()
            self.comboBox_6.addItem("无")
            for i in list_columns:
                self.comboBox_2.addItem(str(i))
                self.comboBox_3.addItem(str(i))
                self.comboBox_6.addItem(str(i))

            print(df.columns.to_list())
            self.df = df
            # 选择的字段做处理
        except Exception as reason:
            print("combobox_1错误原因%s"%reason)
            
        

    def combobox_2(self,text):
        #选择公共键，则，将会以选择框内的内容作为键值匹配数据库
        #读取数据库表名

        pass
    def combobox_3(self,text):
        #选择字段，则，将会以公共键及低端匹配数据库中数据
        dict_columns_type={}#字典格式储存，列名及其对应数据类型
        widgetres = []
        # 获取listwidget中条目数

        #创建一个字典列表储存字段及其数据类型
        #将表格中的数据类型进行转变


    def combobox_4(self,text):
        #选择添加字段数据类型
        pass
    def combobox_5(self,item):
        #连接数据库，并读取数据库中所有表名
        try:
            model = PdTable(pd.DataFrame([]))
            self.tableView_3.setModel(model)

            sqldf=read_config.get_table(item)
            sql_df=PdTable(sqldf)
            self.tableView_3.setModel(sql_df)

        except Exception as reason:
            print("combobox_5出错的原因是%s"%reason)
        '''
        self.comboBox_4.clear()
        self.tablenames = read_config.get_table_names()
        print(self.tablenames)
        for i in self.tablenames:
            self.comboBox_4.addItem(str(i))

        :return:
        '''



    def btn_1(self):
        #实现读取选择的数据表的路径及展现选择表的sheet展现在comboBox_1中
        try:
            self.comboBox_1.clear()
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            self.comboBox_6.clear()
            model = PdTable(pd.DataFrame([]))
            self.tableView_1.setModel(model)
            self.tableView_2.setModel(model)
            fileName, filetype = QFileDialog.getOpenFileName(None,
                                                                    "选取文件",
                                                                    self.cwd,  # 起始路径
                                                                    "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,用双分号间隔

            if fileName == "":
                print("\n取消选择")
            if filetype:
                df = pd.read_excel(str(fileName), sheet_name=None)
                self.label_5.setText(str(fileName))
                for i in df.keys():
                    self.comboBox_1.addItem(str(i))
        except TypeError as reason:
            print('出错原因是%s' % str(reason))


    def btn_2(self):
        #
        try:
            df_len = len(self.column_type_df)
            print(df_len)
            column_text = self.comboBox_3.currentText()
            type_text = self.comboBox_4.currentText()
            if column_text != "" and type_text != "":
                column_list = self.column_type_df['列名'].to_list()
                if column_text not in column_list:
                    self.column_type_df.loc[int(df_len) + 1] = [column_text, type_text]

                else:
                    QMessageBox.information(None, "提示", "已经添加过了")
            else:
                QMessageBox.information(None, "提示", "请确认好列名及数据类型！")
            model = PdTable(self.column_type_df)
            self.tableView_1.setModel(model)
        except Exception as reason:
            print("btn_2错误原因%s" %reason)
        #添加字段及类型


    def btn_3(self):
        try:
            # 表格数据展示
            df1 = self.df
            print("df1")
            print(df1)
            column_list = self.column_type_df['列名'].to_list()
            print(column_list)
            #如果主键不在列表里
            if self.comboBox_2.currentText() not in column_list:
                column_list.insert(0, self.comboBox_2.currentText())
            df_toshow = df1[column_list]
            self.df_toshow = df_toshow
            df = PdTable(df_toshow)
            self.tableView_2.setModel(df)
        except Exception as reason:
            print("btn_3%s"%reason)




    def btn_4(self):
        try:
            self.comboBox_5.clear()
            self.tablenames = read_config.get_table_names()
            print(self.tablenames)
            for i in self.tablenames:
                self.comboBox_5.addItem(str(i))
        except Exception as reason:
            print("btn_4%s" % reason)




    def btn_5(self):
        try:
            df1_columns_list = self.column_type_df['列名'].to_list()
            df1_type_list = self.column_type_df['数据类型'].to_list()
            sql_table_columns_name = read_config.get_columns_names(self.comboBox_5.currentText())
            for i in range(len(df1_columns_list)):
                if df1_columns_list[i] not in sql_table_columns_name:
                    if df1_type_list[i] == "文本型":
                        print("插入")
                        self.add_tablename = self.comboBox_5.currentText()
                        self.add_columnname = df1_columns_list[i]
                        self.type_ = "text"
                        self.question1(text1=self.comboBox_5.currentText(), text2=df1_columns_list[i])

                        print("插入成功")
                    if df1_type_list[i] == "日期型":
                        self.add_tablename = self.comboBox_5.currentText()
                        self.add_columnname = df1_columns_list[i]
                        self.type_ = "date"
                        self.question1(text1=self.comboBox_5.currentText(), text2=df1_columns_list[i])
                    if df1_type_list[i] == "整数型":
                        self.add_tablename = self.comboBox_5.currentText()
                        self.add_columnname = df1_columns_list[i]
                        self.type_ = "int"
                        self.question1(text1=self.comboBox_5.currentText(), text2=df1_columns_list[i])
                    if df1_type_list[i] == "小数型":
                        self.add_tablename = self.comboBox_5.currentText()
                        self.add_columnname = df1_columns_list[i]
                        self.type_ = "float"
                        self.question1(text1=self.comboBox_5.currentText(), text2=df1_columns_list[i])

            print(df1_columns_list)
            print(sql_table_columns_name)
            if self.comboBox_6.currentText() == str("无"):
                print("运行数据更新方法1")
                self.updateway1()
            else:
                print("运行数据更新方法2")
                self.updateway2()
        except Exception as reason:
            print("btn_4%s" % reason)


    def question1(self, text1, text2):
        self.msg = QMessageBox()
        self.msg.setStandardButtons(self.msg.Yes | self.msg.No)
        self.msg.setIcon(self.msg.Question)
        self.msg.setText("请确定将《%s》列表添加到数据库中"% text2)
        self.msg.setWindowTitle(text1)
        self.msg.buttonClicked.connect(self.msgbtn2)
        self.msg.exec_()

    def msgbtn2(self, i):
        a = i.text().strip("&")
        print(a)
        if a == "Yes":
            print("你选择了yes")
            # print(self.msg.text())
            # print(self.msg.windowTitle().title())
            read_config.add_column(self.add_tablename, self.add_columnname, type_=self.type_)

            model = PdTable(pd.DataFrame([]))
            self.tableView_1.setModel(model)
            self.tableView_3.setModel(model)
            sqldf = read_config.get_table(self.comboBox_5.currentText())
            sql_df = PdTable(sqldf)
            self.tableView_3.setModel(sql_df)
        elif a == "No":
            print("你选择了No")
    def updateway1(self):

        #无次级键的更新方法
        ''':var
        1.先获取需要更新的表和数据库中表对应的主键的列
        2.判断需要更新的表中的主键，在数据库中对应表中是否都存在，存在则pass.不存在则添加
        3.根据行列以及
        '''

        ''':var
        '''
        try:
            df1 = self.df_toshow
            df2 = read_config.get_table(self.comboBox_5.currentText())
            print(df1)
            print(df2)
            list_df1_key = df1[self.comboBox_2.currentText()].to_list()
            # list_df1_key除去nan型
            list_df2_key = df2[self.comboBox_2.currentText()].to_list()
            print(list_df1_key)
            print(list_df2_key)
            # 添加主键循环
            for i in list_df1_key:
                print(i)
                if i not in list_df2_key:
                    read_config.add_value(table_name=self.comboBox_5.currentText(),
                                        column_name=self.comboBox_2.currentText(), value=str(i))
                else:
                    print("存在")

            df1_columns_list = self.column_type_df['列名'].to_list()
            print(df1_columns_list)
            df1_type_list = self.column_type_df['数据类型'].to_list()
            print(df1_type_list)

            # 根据收集表中的列进行

            for i in range(len(df1_columns_list)):
                print(i)
                print(df1_columns_list[i])

                value_list = df1[df1_columns_list[i]].to_list()
                print(value_list)
                if df1_type_list[i] == "文本型":
                    for j in range(len(list_df1_key)):
                        print(j)
                        value = value_list[j]
                        print(value)
                        if value == "nan":
                            print("pass")
                        else:
                            value = str(value)
                            read_config.update(table_name=self.comboBox_5.currentText(),
                                            column_name=df1_columns_list[i], key_name=self.comboBox_2.currentText(),
                                            key=list_df1_key[j], value=value)
                elif df1_type_list[i] == "日期型":
                    for j in range(len(list_df1_key)):
                        print(j)
                        value = str(value_list[j])
                        # value =(value_list[j]).strftime('%Y/%m/%d')
                        print(value)
                        if value == "NaT":
                            print("pass")
                        else:
                            print("格式转化")
                            c = (value_list[j]).strftime('%Y/%m/%d')
                            print(c)
                            read_config.update(table_name=self.comboBox_5.currentText(),
                                            column_name=df1_columns_list[i], key_name=self.comboBox_2.currentText(),
                                            key=list_df1_key[j], value=c)
                        pass
                elif df1_type_list[i] == "整数型":
                    for j in range(len(list_df1_key)):
                        print(j)
                        value = str(value_list[j])
                        print(value)
                        if value == "nan":
                            print("pass")
                        else:
                            print("格式转变")
                            c = int(float(value))
                            print(c)
                            read_config.update(table_name=self.comboBox_5.currentText(),
                                            column_name=df1_columns_list[i], key_name=self.comboBox_2.currentText(),
                                            key=list_df1_key[j], value=c)
                        pass
                elif df1_type_list[i] == "小数型":
                    for j in range(len(list_df1_key)):
                        print(j)
                        value = str(value_list[j])
                        print(value)
                        if value == "nan":
                            print("pass")
                        else:
                            print("类型转换")
                            c = float(value)
                            print(c)
                            read_config.update(table_name=self.comboBox_5.currentText(),
                                            column_name=df1_columns_list[i], key_name=self.comboBox_2.currentText(),
                                            key=list_df1_key[j], value=c)

                pv = int((i + 1) / len(df1_columns_list) * 100)
                self.pgb.setValue(pv)
                if pv == 100:
                    QMessageBox.information(None, "提示", "数据更新完成")
                    pv = 0
                    self.pgb.setValue(pv)
        except Exception as reason:
            print("updateway1%s"%reason)






    def updateway2(self):
        try:
            df1 = self.df_toshow
            df2 = read_config.get_table(self.comboBox_5.currentText())
            print(df1)
            print(df2)

            list_df1_key1 = df1[self.comboBox_2.currentText()].to_list()
            list_df1_key2 = df1[self.comboBox_6.currentText()].to_list()
            list_df2_key1 = df2[self.comboBox_2.currentText()].to_list()
            list_df2_key2 = df2[self.comboBox_6.currentText()].to_list()
            print(list_df1_key1)
            print(list_df1_key2)
            print(list_df2_key1)
            print(list_df2_key2)
            list1 = []
            list2 = []
            for i in range(len(list_df1_key1)):
                list1.append([list_df1_key1[i], list_df1_key2[i]])
            for j in range(len(list_df2_key1)):
                list2.append([list_df2_key1[j], list_df2_key2[j]])
            print(list1)
            print(list2)

            df1_columns_list = self.column_type_df['列名'].to_list()
            print(df1_columns_list)
            index_key2 = df1_columns_list.index(self.comboBox_6.currentText())
            print(index_key2)
            print(df1_columns_list[index_key2])
            key2 = df1_columns_list[index_key2]
            df1_columns_list.remove(key2)
            print(df1_columns_list)
            df1_type_list = self.column_type_df['数据类型'].to_list()
            print(df1_type_list)
            key22 = df1_type_list[index_key2]
            print(key22)
            df1_type_list.remove(key22)
            print(df1_type_list)

            for i in list1:
                if i not in list2:
                    read_config.add_values(table_name=self.comboBox_5.currentText(),
                                        column1_name=self.comboBox_2.currentText(), value1=i[0],
                                        column2_name=self.comboBox_6.currentText(), value2=i[1])
                else:
                    print("存在")

            for i in range(len(df1_columns_list)):

                value_list = df1[df1_columns_list[i]].to_list()
                if df1_type_list[i] == "文本型":
                    for j in range(len(list1)):

                        print(j)
                        value = value_list[j]
                        print(value)
                        if value == "nan":
                            print("pass")
                        else:
                            value = str(value)
                            read_config.update2(table_name=self.comboBox_5.currentText(),
                                                column_name=df1_columns_list[i],
                                                key1_name=self.comboBox_2.currentText(), key1=list1[j][0],
                                                key2_name=self.comboBox_6.currentText(), key2=list1[j][1], value=value)
                elif df1_type_list[i] == "日期型":
                    for j in range(len(list1)):
                        print(j)
                        value = str(value_list[j])
                        # value =(value_list[j]).strftime('%Y/%m/%d')
                        print(value)
                        if value == "NaT":
                            print("pass")
                        else:
                            print("格式转化")
                            c = (value_list[j]).strftime('%Y/%m/%d')
                            print(c)
                            read_config.update2(table_name=self.comboBox_5.currentText(),
                                                column_name=df1_columns_list[i],
                                                key1_name=self.comboBox_2.currentText(), key1=list1[j][0],
                                                key2_name=self.comboBox_6.currentText(), key2=list1[j][1], value=c)
                        pass
                elif df1_type_list[i] == "整数型":
                    for j in range(len(list1)):
                        print(j)
                        value = str(value_list[j])
                        print(value)
                        if value == "nan":
                            print("pass")
                        else:
                            print("格式转变")
                            c = int(float(value))
                            print(c)
                            read_config.update2(table_name=self.comboBox_5.currentText(),
                                                column_name=df1_columns_list[i],
                                                key1_name=self.comboBox_2.currentText(), key1=list1[j][0],
                                                key2_name=self.comboBox_6.currentText(), key2=list1[j][1], value=c)
                        pass
                elif df1_type_list[i] == "小数型":
                    for j in range(len(list1)):
                        print(j)
                        value = str(value_list[j])
                        print(value)
                        if value == "nan":
                            print("pass")
                        else:
                            print("类型转换")
                            c = float(value)
                            print(c)
                            read_config.update2(table_name=self.comboBox_5.currentText(),
                                                column_name=df1_columns_list[i],
                                                key1_name=self.comboBox_2.currentText(), key1=list1[j][0],
                                                key2_name=self.comboBox_6.currentText(), key2=list1[j][1], value=c)
                pv = int((i + 1) / len(df1_columns_list) * 100)
                self.pgb.setValue(pv)
                if pv == 100:
                    QMessageBox.information(None, "提示", "数据更新完成")
                    pv = 0
                    self.pgb.setValue(pv)
        except Exception as reason:
            print("updateway2%s"%reason)




    def btn_6(self):
        try:
            self.listWidget_1.clear()
            fileName_choose = QFileDialog.getOpenFileName(None,
                                                                    "选取文件",
                                                                    self.cwd,  # 起始路径
                                                                    "All Files (*)")  # 设置文件扩展名过滤,用双分号间隔
            if fileName_choose[0] != "":
                self.label_5.setText(str(fileName_choose[0]))
                df = pd.read_excel(str(fileName_choose[0]), sheet_name=None)
                print(df.keys())
                for i in df.keys():
                    self.listWidget_1.addItem(str(i))
            if fileName_choose[0] == "":
                QMessageBox.information(None, "提示", "你没有选择数据表。")
                return fileName_choose[0]
        except TypeError as reason:
            print('错误原因是%s' % str(reason))


    def btn_7(self):
        try:
            self.excel_location = None  # excel表位置
            self.pv = 0
            self.df_toshow = None
            self.comboBox_1.clear()
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            self.comboBox_5.clear()
            #self.comboBox_6.clear()
            self.comboBox_8.clear()
            self.comboBox_7.clear()
            model = PdTable(pd.DataFrame([]))
            self.tableView_1.setModel(model)
            self.tableView_2.setModel(model)
            self.tableView_3.setModel(model)

            self.listWidget_1.clear()
            self.label_5.setText("选择表位置：")
        except Exception as reason:
            print("btn_7%s"%reason)

    def question(self,text1,text2):
        self.msg = QMessageBox()
        self.msg.setStandardButtons(self.msg.Yes | self.msg.No)
        self.msg.setIcon(self.msg.Question)
        self.msg.setText(text2)
        self.msg.setWindowTitle(text1)
        self.msg.buttonClicked.connect(self.msgbtn)
        self.msg.exec_()


    def msgbtn(self,i):
        a=i.text().strip("&")
        print(a)
        if a == "Yes":
            print("你选择了yes")
            #print(self.msg.text())
            #print(self.msg.windowTitle().title())
            read_config.add_column(self.msg.windowTitle().title(), self.msg.text())
        elif a== "No":
            print("你选择了No")



    def listwidget_1(self, item):

        try:
            self.msg = QMessageBox()
            self.msg.setStandardButtons(self.msg.Yes | self.msg.No)
            self.msg.setIcon(self.msg.Question)
            self.msg.setText("是否新增数据表：%s" % str(item.text()))
            self.msg.setWindowTitle(str(item.text()))
            self.item = str(item.text())
            self.msg.buttonClicked.connect(self.msgbtn1)
            self.msg.exec_()
        except Exception as reason:
            print("listwidget_1%s"%reason)



    def msgbtn1(self,i):
        a=i.text().strip("&")
        print(a)
        if a == "Yes":
            print("你选择了yes")
            #print(self.msg.text())
            #print(self.msg.windowTitle().title())
            item=self.item
            print(item)

            df = pd.read_excel(str(self.label_5.text()), sheet_name=str(item))
            if str(item)=="教师":
                df=self.teacher_excel_add_id(df)
            if str(item) != "教师":
                df = self.other_excel_add_id(df)
            print(df)
            read_config.create_table(df, str(item))
            QMessageBox.information(None,"提示","导入成功")
        elif a== "No":
            print("你选择了No")


    def teacher_excel_add_id(self,df):
        column_list=df.columns.to_list()
        #判断是否sheet表中是否有教师这列，如果有教师这列，判断是否有教师ID这列
        if "姓名" in column_list:
            if "教师ID" not in column_list:
                df['教师ID']=None
            df['教师ID']=df.index
        return df
        #教师姓名中有重复姓名默认为是不同人，分配ID
        
    def other_excel_add_id(self,df):
        column_list = df.columns.to_list()
        if "姓名" in column_list:
            if "教师ID" not in column_list:
                df['教师ID'] = None

            sql_df = read_config.get_table("教师")
            df_list_name=df['姓名'].to_list()
            sql_list_name=sql_df['姓名'].to_list()

            new_list1,new_list2,name_list=self.remove_repeat(df_list_name)
            sql_list1,sql_list2,sql_name_list=self.remove_repeat(sql_list_name)


            print(name_list)
            print(sql_name_list)

            for i in range(len(df)):
                name = df['姓名'][i]
                print(name)
                if name in name_list:
                    if name in sql_name_list:
                        id = read_config.get_id("教师", name)
                        print(id)
                        df['教师ID'][i] = id
                else:
                    pass
        return df

    def btn_8(self):
        #选择数据表和连接数据库
        fileName, filetype = QFileDialog.getOpenFileName(None,
                                                        "选取文件",
                                                        self.cwd,  # 起始路径
                                                        "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,用双分号间隔

        if fileName == "":
            print("\n取消选择")
        if filetype:
            df = pd.read_excel(str(fileName), sheet_name=None)
            self.label_5.setText(str(fileName))
            self.comboBox_7.clear()
            for i in df.keys():
                self.comboBox_7.addItem(str(i))
        try:
            self.comboBox_8.clear()
            self.tablenames = read_config.get_table_names()

            print(self.tablenames)
            for i in self.tablenames:
                self.comboBox_8.addItem(str(i))
        except Exception as reason:
            print("btn_4%s" % reason)


    def combobox_7(self,item):
        try:
            model = PdTable(pd.DataFrame([]))
            self.tableView_2.setModel(model)

            sqldf = pd.read_excel(str(self.label_5.text()), sheet_name=item)
            sql_df=PdTable(sqldf)
            self.tableView_2.setModel(sql_df)

        except Exception as reason:
            print("combobox_5出错的原因是%s"%reason)

    def combobox_8(self,item):
        try:
            model = PdTable(pd.DataFrame([]))
            self.tableView_3.setModel(model)

            sqldf=read_config.get_table(item)
            sql_df=PdTable(sqldf)
            self.tableView_3.setModel(sql_df)

        except Exception as reason:
            print("combobox_5出错的原因是%s"%reason)


    def btn_9(self):
        #进行表格及数据库id匹配
        try:
            df = pd.read_excel(str(self.label_5.text()), sheet_name=self.comboBox_7.currentText())      #读取选取的数据表
            df_columns_list=df.columns.to_list()                        #存储列名
            teacher_name_list=df['姓名'].to_list()                       #将姓名列都列举出来

            new_list1=[] #用于存储无重复的所有姓名
            new_list2=[]   #用于存储有重复的所有姓名
            name_list=[]    #储存去除重复姓名后余下的姓名

            for i in teacher_name_list:
                if i not in new_list1:
                    new_list1.append(i)
                    name_list.append(i)
                else:
                    if i not in new_list2:
                        new_list2.append(i)
                    else:
                        pass


            for i in new_list2:
                name_list.remove(i)



            #如果表格列中没有教师ID列，则插入教师ID列
            if "教师ID" not in df_columns_list:
                df['教师ID']=None

            #读取数据库表
            sql_df=read_config.get_table(self.comboBox_8.currentText())
            sql_name_list=sql_df['姓名'].to_list()            #将数据库内姓名列举出来


            sql_list1, sql_list2, sql_name_list=self.remove_repeat(sql_name_list)
            #sql_list1是全部姓名
            #sql_list2是发生重名的全部姓名
            #sql_name_list是去除重名后余下的姓名列表

            #调用remove_repeat方法去除重复

            #依次读取姓名列，如果姓名在去除重复后的姓名列表中，且选择的数据库中有该姓名则会进行ID匹配然后添加

            '''
            姓名匹配逻辑：
            1.对于教师的新增默认是不需要进行数据匹配的，因为教师不重复的，故教师ID列为自增函数，只要有新增的都会进行自动匹配教师ID
            2.对于包含动作类表格的数据匹配逻辑，只要是包含姓名的，都可以与数据库内教师表进行数据匹配，会自动将教师ID匹配上，其余教师ID需要自行进行填充
            3.不包含教师姓名的表，请直接进行数据表的更新或者新增
            '''

            for i in range(len(df)):
                name=df['姓名'][i]
                if name in sql_name_list:
                        id=read_config.get_id(self.comboBox_8.currentText(),name)
                        print(name)
                        print(id)
                        df['教师ID'][i]=id
            #在原始表中新填加一张表，包含了教师ID，存储在原来的表格里
            self.write(file_path=str(self.label_5.text()), sheet_name=str(self.comboBox_7.currentText()+"new"), df_name=df)
            QMessageBox.information(None,"提示","教师ID匹配已经完成")

        except Exception as reason:
            QMessageBox.information(None, "错误提示", "进行id匹配出错的原因%s"%reason)



        pass

    def write(cls, file_path, sheet_name, df_name):
            writer = pd.ExcelWriter(file_path, mode='r+')
            df_name.to_excel(writer, sheet_name=sheet_name, index_label=False, index=False)
            writer.save()


    def remove_repeat(self,sample_list):
        new_list1 = []  # 用于存储无重复的所有姓名
        new_list2 = []  # 用于存储有重复的所有姓名
        name_list = []
        for i in sample_list:
            if i not in new_list1:
                new_list1.append(i)
                name_list.append(i)
            else:
                if i not in new_list2:
                    new_list2.append(i)
                else:
                    pass
        for i in new_list2:
            name_list.remove(i)
        return new_list1,new_list2,name_list

#显示df的table_view，主界面下方表格
class PdTable(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    # 显示数据
    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def rowCount(self, parent=None):
        #获取行
        return self._data.shape[0]

    def columnCount(self, parent=None):
        #获取列
        return self._data.shape[1]
    # 显示行和列头
    def headerData(self,col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.axes[0][col]
        return None




