
from PyQt5.QtCore import *
import pymysql
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import os
import pandas as pd
from PyQt5.QtWidgets import QMessageBox
import read_config




class PdTable(QAbstractTableModel):
    def __init__(self,data):
        QAbstractTableModel.__init__(self)
        self._data = data
        self.columnCount=self._data.shape[1]
        self.rowCount=self._data.shape[0]



#显示df的table_view，主界面下方表格
class PdTable(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        #获取行
        return self._data.shape[0]

    def columnCount(self, parent=None):
        #获取列
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