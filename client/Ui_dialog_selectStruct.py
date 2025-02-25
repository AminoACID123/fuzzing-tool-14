# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\VSCode_Project\python_project\fuzzProject\dialog_selectStruct.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys
import os
import traceback
import cppProj

import Ui_dialog_seed as seedDialogPY
import staticAnalysis


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(415, 414)
        Dialog.setModal(False)
        self.structTableWidget = QtWidgets.QTableWidget(Dialog)
        self.structTableWidget.setGeometry(QtCore.QRect(30, 30, 361, 291))
        self.structTableWidget.setObjectName("structTableWidget")
        self.structTableWidget.setColumnCount(2)
        self.structTableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.structTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.structTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.structTableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.structTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.structTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        # self.structTableWidget.setItem(0, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        # item.setCheckState(QtCore.Qt.Unchecked)
        # self.structTableWidget.setItem(0, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        # self.structTableWidget.setItem(1, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setCheckState(QtCore.Qt.Unchecked)
        # self.structTableWidget.setItem(1, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        # self.structTableWidget.setItem(2, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setCheckState(QtCore.Qt.Unchecked)
        self.structTableWidget.setItem(2, 1, item)
        self.structTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.structTableWidget.horizontalHeader().setDefaultSectionSize(175)
        self.yesBtn = QtWidgets.QPushButton(Dialog)
        self.yesBtn.setGeometry(QtCore.QRect(90, 340, 221, 51))
        self.yesBtn.setObjectName("yesBtn")

        # =================================connect=======================================
        self.seedBinaryPath = ""

        self.yesBtn.clicked.connect(self.popSeedDialog)
        self.yesBtn.clicked.connect(Dialog.accept)
        # =============================================================================

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "选择结构体"))
        item = self.structTableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.structTableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.structTableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.structTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "结构体"))
        item = self.structTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "用于输入"))
        __sortingEnabled = self.structTableWidget.isSortingEnabled()
        self.structTableWidget.setSortingEnabled(False)
        # item = self.structTableWidget.item(0, 0)
        # item.setText(_translate("Dialog", "struct1"))
        # item = self.structTableWidget.item(1, 0)
        # item.setText(_translate("Dialog", "struct2"))
        # item = self.structTableWidget.item(2, 0)
        # item.setText(_translate("Dialog", "struct3"))
        self.structTableWidget.setSortingEnabled(__sortingEnabled)
        self.yesBtn.setText(_translate("Dialog", "确定"))
        # ================================================================
        self.selectedStruct = ""
        # ================================================================

    # =======================================================================================

    def setValues(self, header_loc_list, typeJSONPath, uiClient):
        """设置界面的初始值

        Parameters
        ----------
        header_loc_list : list
            列表中存储了所有头文件的路径
        typeJSONPath : str
            数据类型字典JSON文件位置
        uiClient : [type]
            主界面ui

        Notes
        -----
        [description]
        """
        self.header_loc_list = header_loc_list

        # ========== Support for cpp ==========
        cppProj.init(header_loc_list)
        self.structList = cppProj.getAllStruct(header_loc_list)

        structSet = set()
        for struct in self.structList:
            structSet.add(struct[-1])
        self.structList = sorted(list(structSet))
        # =====================================

        self.structTableWidget.setRowCount(len(self.structList))
        self.typeJSONPath = typeJSONPath
        self.uiClient = uiClient

        s_cbx = "{"
        s_lab = "{"
        for i in range(len(self.structList)):
            s_cbx += str(i) + ":QtWidgets.QCheckBox(),"
            s_lab += str(i) + ":QtWidgets.QLabel(),"
        s_cbx += "}"
        s_lab += "}"
        self.checkboxs = eval(s_cbx)
        self.labels = eval(s_lab)
        print(self.structList)
        for i in range(len(self.structList)):
            hLayout = QtWidgets.QHBoxLayout()
            hLayout.addWidget(self.checkboxs[i])
            hLayout.setAlignment(self.checkboxs[i], QtCore.Qt.AlignCenter)
            widget = QtWidgets.QWidget()
            widget.setLayout(hLayout)
            self.structTableWidget.setCellWidget(i, 1, widget)
            self.structTableWidget.setRowHeight(i, 40)
            self.labels[i].setText(self.structList[i])
            hLayout2 = QtWidgets.QHBoxLayout()
            hLayout2.addWidget(self.labels[i])
            hLayout2.setAlignment(self.labels[i], QtCore.Qt.AlignCenter)
            widget2 = QtWidgets.QWidget()
            widget2.setLayout(hLayout2)
            self.structTableWidget.setCellWidget(i, 0, widget2)
            self.checkboxs[i].clicked.connect(lambda x, i=i: self.selectStruct(self.checkboxs[i], self.structList[i]))

        # 默认高度较矮，需要设置一下
        for i in range(len(self.structList)):
            self.structTableWidget.setRowHeight(i, 50)

    def setSeedBinaryPath(self, seedBinaryPath):
        self.seedBinaryPath = seedBinaryPath

    def selectStruct(self, checkbox, label):
        """选择了某个结构体，将其对应的checkbox打勾

        Parameters
        ----------
        checkbox : [type]
            [description]
        label : [type]
            [description]

        Notes
        -----
        [description]
        """
        self.unselectAll()
        checkbox.setChecked(True)
        self.selectedStruct = label

    def unselectAll(self):
        """因为结构体是单选，所以写一个取消全部选择的函数，在选择某个结构体前先取消全部选择

        Notes
        -----
        [description]
        """
        for i in range(len(self.structList)):
            self.checkboxs[i].setChecked(False)
        self.selectedStruct = ""

    def popSeedDialog(self):
        """弹出种子输入界面

        Raises
        ------
        ValueError
            如果没有选择结构体就弹出提示信息

        Notes
        -----
        [description]
        """
        analyzeTipBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "消息", "如果结构体内容较为复杂，分析内容会较长，请耐心等待")
        analyzeTipBox.exec_()
        try:
            if self.selectedStruct == "":
                raise ValueError("没有选择结构体")
            self.seedDialog = QtWidgets.QDialog()
            self.uiSeed = seedDialogPY.Ui_Dialog()
            self.uiSeed.setupUi(self.seedDialog)
            # 如果读取JSON的话，JSONPath和readJSON就用不上了，占个位置
            self.uiSeed.setDataTypeDict(self.typeJSONPath)
            if os.path.exists(self.seedBinaryPath):
                self.uiSeed.initStructDictBySeedBinary(self.header_loc_list, self.seedBinaryPath, self.uiClient, self.selectedStruct, self.structList)
            else:
                self.uiSeed.initStructDict(self.header_loc_list, "JSONPath", False, self.uiClient, self.selectedStruct, self.structList)
            self.seedDialog.show()
        except ValueError as e:
            exceptionBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "还没有选择结构体")
            exceptionBox.exec_()
            print("\033[1;31m")
            traceback.print_exc()
            print("\033[0m")
        except BaseException as e:
            print("\033[1;31m")
            traceback.print_exc()
            print("\033[0m")
            exceptionBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", repr(e))
            exceptionBox.exec_()

    # ====================================================================================================


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    headerNotExistBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "消息", "请运行Ui_window.py :)")
    headerNotExistBox.exec_()
