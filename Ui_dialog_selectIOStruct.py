'''
Author: Radon
Date: 2021-07-19 19:27:59
LastEditors: Radon
LastEditTime: 2021-07-19 21:49:27
Description: 选择输入与输出格式的界面
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Project_VSCode\python_project\fuzzProject\dialog_selectInputAndOutputStruct.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import functools

import Ui_dialog_selectStruct as selectStructDialogPY


class Ui_Dialog(object):
    def setupUi(self, Dialog, header_loc_list):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 227)
        self.inputBtn = QtWidgets.QPushButton(Dialog)
        self.inputBtn.setGeometry(QtCore.QRect(70, 70, 111, 61))
        self.inputBtn.setObjectName("inputBtn")
        self.outputBtn = QtWidgets.QPushButton(Dialog)
        self.outputBtn.setGeometry(QtCore.QRect(230, 70, 111, 61))
        self.outputBtn.setObjectName("outputBtn")
        self.tipLabel = QtWidgets.QLabel(Dialog)
        self.tipLabel.setGeometry(QtCore.QRect(130, 30, 161, 16))
        self.tipLabel.setObjectName("tipLabel")
        self.inputTipLabel = QtWidgets.QLabel(Dialog)
        self.inputTipLabel.setGeometry(QtCore.QRect(140, 150, 72, 15))
        self.inputTipLabel.setObjectName("inputTipLabel")
        self.outputTipLabel = QtWidgets.QLabel(Dialog)
        self.outputTipLabel.setGeometry(QtCore.QRect(140, 190, 72, 15))
        self.outputTipLabel.setObjectName("outputTipLabel")
        self.inputStructLabel = QtWidgets.QLabel(Dialog)
        self.inputStructLabel.setGeometry(QtCore.QRect(220, 150, 161, 16))
        self.inputStructLabel.setObjectName("inputStructLabel")
        self.outputStructLabel = QtWidgets.QLabel(Dialog)
        self.outputStructLabel.setGeometry(QtCore.QRect(220, 190, 161, 16))
        self.outputStructLabel.setObjectName("outputStructLabel")

        # =========================================================================
        self.inputBtn.clicked.connect(functools.partial(self.popStructDialog, "input", header_loc_list))
        # =========================================================================

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "选择格式"))
        self.inputBtn.setText(_translate("Dialog", "输入"))
        self.outputBtn.setText(_translate("Dialog", "输出"))
        self.tipLabel.setText(_translate("Dialog", "请选择输入与输出格式"))
        self.inputTipLabel.setText(_translate("Dialog", "输入格式:"))
        self.outputTipLabel.setText(_translate("Dialog", "输出格式:"))
        self.inputStructLabel.setText(_translate("Dialog", "暂无"))
        self.outputStructLabel.setText(_translate("Dialog", "暂无"))

    def popStructDialog(self, choice, header_loc_list):
        """弹出选择结构体的界面

        Parameters
        ----------
        choice : str
            表示按下了哪个按钮，如果按下了输入按钮choice的值就是input，输出是output
        header_loc_list : list
            列表内存储了所有头文件的路径信息

        Notes
        -----
        [description]
        """
        # 询问用户是否读取JSON
        readJSON = False
        whetherReadJSONBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, "读取文件", "是否读取现有JSON文件?")
        yes = whetherReadJSONBox.addButton("是", QtWidgets.QMessageBox.YesRole)
        no = whetherReadJSONBox.addButton("否", QtWidgets.QMessageBox.NoRole)
        whetherReadJSONBox.exec_()
        if whetherReadJSONBox.clickedButton() == yes:
            readJSON = True

        # 如果读取现有文件，就读取JSON
        if readJSON:
            selectedFile = QtWidgets.QFileDialog.getOpenFileName(None, "choose file", "C:/Users/Radon/Desktop/", filter="json file (*.json)")
            path = selectedFile[0]
            print("选完了json，该打开种子设置界面了")
        else:
            if choice == "input":
                self.selectStructDialog = QtWidgets.QDialog()
                self.uiSelectStruct = selectStructDialogPY.Ui_Dialog()
                self.uiSelectStruct.setupUi(self.selectStructDialog)
                self.selectStructDialog.show()