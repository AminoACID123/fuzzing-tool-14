'''
Author: Radon
Date: 2021-06-29 13:23:34
LastEditors: Radon
LastEditTime: 2021-07-01 14:41:04
Description: 模糊测试工具
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\VSCode_Project\python_project\fuzzProject\window_v5.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import re
import os

import Ui_dialog_fuzz_v2 as fuzzDialogPY
import Ui_dialog_seed_v5 as seedDialogPY
import Ui_dialog_selectTarget as targetDialogPY
import Ui_dialog_selectStruct as structDialogPY
import staticAnalysis as sa

import instrument as ins


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 614)
        MainWindow.setIconSize(QtCore.QSize(20, 20))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startFuzzBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startFuzzBtn.setGeometry(QtCore.QRect(439, 500, 271, 61))
        self.startFuzzBtn.setIconSize(QtCore.QSize(40, 40))
        self.startFuzzBtn.setObjectName("startFuzzBtn")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(300, 20, 201, 31))
        self.title.setLineWidth(1)
        self.title.setIndent(-1)
        self.title.setObjectName("title")
        self.chooseFileGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.chooseFileGroup.setGeometry(QtCore.QRect(80, 50, 631, 101))
        self.chooseFileGroup.setObjectName("chooseFileGroup")
        self.CFileLoc = QtWidgets.QTextBrowser(self.chooseFileGroup)
        self.CFileLoc.setEnabled(True)
        self.CFileLoc.setGeometry(QtCore.QRect(20, 20, 481, 31))
        self.CFileLoc.setObjectName("CFileLoc")
        self.chooseCBtn = QtWidgets.QPushButton(self.chooseFileGroup)
        self.chooseCBtn.setGeometry(QtCore.QRect(520, 20, 93, 31))
        self.chooseCBtn.setAutoDefault(False)
        self.chooseCBtn.setDefault(False)
        self.chooseCBtn.setFlat(False)
        self.chooseCBtn.setObjectName("chooseCBtn")
        self.HFileLoc = QtWidgets.QTextBrowser(self.chooseFileGroup)
        self.HFileLoc.setEnabled(True)
        self.HFileLoc.setGeometry(QtCore.QRect(20, 60, 481, 31))
        self.HFileLoc.setObjectName("HFileLoc")
        self.chooseHBtn = QtWidgets.QPushButton(self.chooseFileGroup)
        self.chooseHBtn.setGeometry(QtCore.QRect(520, 60, 93, 31))
        self.chooseHBtn.setAutoDefault(False)
        self.chooseHBtn.setDefault(False)
        self.chooseHBtn.setFlat(False)
        self.chooseHBtn.setObjectName("chooseHBtn")
        self.seedInputGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.seedInputGroup.setGeometry(QtCore.QRect(440, 160, 271, 121))
        self.seedInputGroup.setObjectName("seedInputGroup")
        self.popSeedDialogBtn = QtWidgets.QPushButton(self.seedInputGroup)
        self.popSeedDialogBtn.setGeometry(QtCore.QRect(90, 35, 93, 31))
        self.popSeedDialogBtn.setObjectName("popSeedDialogBtn")
        self.label_3 = QtWidgets.QLabel(self.seedInputGroup)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 231, 16))
        self.label_3.setObjectName("label_3")
        self.stopOptionGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.stopOptionGroup.setGeometry(QtCore.QRect(80, 290, 341, 181))
        self.stopOptionGroup.setObjectName("stopOptionGroup")
        self.stopByTime = QtWidgets.QRadioButton(self.stopOptionGroup)
        self.stopByTime.setGeometry(QtCore.QRect(20, 80, 115, 19))
        self.stopByTime.setObjectName("stopByTime")
        self.stopByTC = QtWidgets.QRadioButton(self.stopOptionGroup)
        self.stopByTC.setGeometry(QtCore.QRect(20, 130, 115, 19))
        self.stopByTC.setObjectName("stopByTC")
        self.stopByCrash = QtWidgets.QRadioButton(self.stopOptionGroup)
        self.stopByCrash.setGeometry(QtCore.QRect(20, 30, 161, 19))
        self.stopByCrash.setChecked(True)
        self.stopByCrash.setObjectName("stopByCrash")
        self.fuzzTime = QtWidgets.QSpinBox(self.stopOptionGroup)
        self.fuzzTime.setGeometry(QtCore.QRect(150, 70, 81, 31))
        self.fuzzTime.setObjectName("fuzzTime")
        self.timeUnit = QtWidgets.QComboBox(self.stopOptionGroup)
        self.timeUnit.setGeometry(QtCore.QRect(240, 70, 91, 31))
        self.timeUnit.setObjectName("timeUnit")
        self.timeUnit.addItem("")
        self.timeUnit.addItem("")
        self.TCUnitLabel = QtWidgets.QLabel(self.stopOptionGroup)
        self.TCUnitLabel.setGeometry(QtCore.QRect(240, 124, 72, 21))
        self.TCUnitLabel.setObjectName("TCUnitLabel")
        self.stopByTCNum = QtWidgets.QLineEdit(self.stopOptionGroup)
        self.stopByTCNum.setGeometry(QtCore.QRect(150, 120, 81, 31))
        self.stopByTCNum.setObjectName("stopByTCNum")
        self.instrOptionGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.instrOptionGroup.setGeometry(QtCore.QRect(440, 290, 271, 181))
        self.instrOptionGroup.setObjectName("instrOptionGroup")
        self.funcLevel = QtWidgets.QRadioButton(self.instrOptionGroup)
        self.funcLevel.setGeometry(QtCore.QRect(30, 50, 115, 19))
        self.funcLevel.setChecked(True)
        self.funcLevel.setObjectName("funcLevel")
        self.branchLevel = QtWidgets.QRadioButton(self.instrOptionGroup)
        self.branchLevel.setGeometry(QtCore.QRect(30, 110, 115, 19))
        self.branchLevel.setObjectName("branchLevel")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(80, 480, 341, 101))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 31))
        self.label.setObjectName("label")
        self.TCNumPerCyc = QtWidgets.QLineEdit(self.groupBox)
        self.TCNumPerCyc.setGeometry(QtCore.QRect(150, 20, 81, 31))
        self.TCNumPerCyc.setObjectName("TCNumPerCyc")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 31, 31))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 131, 31))
        self.label_4.setObjectName("label_4")
        self.timeoutLEdit = QtWidgets.QLineEdit(self.groupBox)
        self.timeoutLEdit.setGeometry(QtCore.QRect(150, 60, 81, 31))
        self.timeoutLEdit.setObjectName("timeoutLEdit")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(240, 60, 31, 31))
        self.label_5.setObjectName("label_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(80, 160, 341, 121))
        self.tabWidget.setStyleSheet("background-color:rgb(235, 235, 235)")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.codeStructTab = QtWidgets.QWidget()
        self.codeStructTab.setObjectName("codeStructTab")
        self.targetSetInfo = QtWidgets.QTextBrowser(self.codeStructTab)
        self.targetSetInfo.setGeometry(QtCore.QRect(20, 10, 201, 71))
        self.targetSetInfo.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.targetSetInfo.setObjectName("targetSetInfo")
        self.SAByCppcheckBtn = QtWidgets.QPushButton(self.codeStructTab)
        self.SAByCppcheckBtn.setGeometry(QtCore.QRect(230, 10, 93, 31))
        self.SAByCppcheckBtn.setStyleSheet("")
        self.SAByCppcheckBtn.setObjectName("SAByCppcheckBtn")
        self.SAByManBtn = QtWidgets.QPushButton(self.codeStructTab)
        self.SAByManBtn.setGeometry(QtCore.QRect(230, 50, 93, 31))
        self.SAByManBtn.setObjectName("SAByManBtn")
        self.tabWidget.addTab(self.codeStructTab, "")
        self.AITab = QtWidgets.QWidget()
        self.AITab.setObjectName("AITab")
        self.label_6 = QtWidgets.QLabel(self.AITab)
        self.label_6.setGeometry(QtCore.QRect(120, 30, 141, 16))
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.AITab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 以下为手写内容
        self.startFuzzBtn.clicked.connect(self.popFuzzDialog)
        # self.popSeedDialogBtn.clicked.connect(self.popSeedDialog)
        self.popSeedDialogBtn.clicked.connect(self.popStructDialog)
        self.chooseCBtn.clicked.connect(self.chooseCFile)
        self.chooseHBtn.clicked.connect(self.chooseHFile)
        self.SAByCppcheckBtn.clicked.connect(self.SAByCppcheck)
        self.SAByManBtn.clicked.connect(self.popTargetDialog)

        regExp1 = QtCore.QRegExp("^([1-9]\d{0,2}|1000)$")
        self.TCNumPerCyc.setValidator(QtGui.QRegExpValidator(regExp1))
        self.timeoutLEdit.setValidator(QtGui.QRegExpValidator(regExp1))
        regExp2 = QtCore.QRegExp("^\\d+$")
        self.stopByTCNum.setValidator(QtGui.QRegExpValidator(regExp2))
        # 手写内容结束

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于代码结构的模糊测试工具"))
        self.startFuzzBtn.setText(_translate("MainWindow", "开始测试"))
        self.title.setText(_translate("MainWindow", "基于代码结构的模糊测试工具"))
        self.chooseFileGroup.setTitle(_translate("MainWindow", "选择文件"))
        self.CFileLoc.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.CFileLoc.setPlaceholderText(_translate("MainWindow", "C文件位置"))
        self.chooseCBtn.setText(_translate("MainWindow", "选择C文件"))
        self.HFileLoc.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.HFileLoc.setPlaceholderText(_translate("MainWindow", "头文件位置"))
        self.chooseHBtn.setText(_translate("MainWindow", "选择头文件"))
        self.seedInputGroup.setTitle(_translate("MainWindow", "种子输入"))
        self.popSeedDialogBtn.setText(_translate("MainWindow", "手动输入"))
        self.label_3.setText(_translate("MainWindow", "如果不手动输入，系统会自动生成"))
        self.stopOptionGroup.setTitle(_translate("MainWindow", "终止条件"))
        self.stopByTime.setText(_translate("MainWindow", "按时间"))
        self.stopByTC.setText(_translate("MainWindow", "按测试用例数量"))
        self.stopByCrash.setText(_translate("MainWindow", "检测到错误就停止"))
        self.timeUnit.setItemText(0, _translate("MainWindow", "分钟"))
        self.timeUnit.setItemText(1, _translate("MainWindow", "小时"))
        self.TCUnitLabel.setText(_translate("MainWindow", "个"))
        self.stopByTCNum.setText(_translate("MainWindow", "2000"))
        self.instrOptionGroup.setTitle(_translate("MainWindow", "插桩粒度"))
        self.funcLevel.setText(_translate("MainWindow", "函数级"))
        self.branchLevel.setText(_translate("MainWindow", "分支级"))
        self.groupBox.setTitle(_translate("MainWindow", "其他设置"))
        self.label.setText(_translate("MainWindow", "每轮测试用例生成"))
        self.TCNumPerCyc.setText(_translate("MainWindow","5"))
        self.label_2.setText(_translate("MainWindow", "个"))
        self.label_4.setText(_translate("MainWindow", "测试用例超时时间："))
        self.timeoutLEdit.setText(_translate("MainWindow", "10"))
        self.label_5.setText(_translate("MainWindow", "秒"))
        self.targetSetInfo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.targetSetInfo.setPlaceholderText(_translate("MainWindow", "目标集信息"))
        self.SAByCppcheckBtn.setText(_translate("MainWindow", "cppcheck"))
        self.SAByManBtn.setText(_translate("MainWindow", "手动选择"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.codeStructTab), _translate("MainWindow", "基于代码结构"))
        self.label_6.setText(_translate("MainWindow", "基于交互接口规约"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AITab), _translate("MainWindow", "基于交互接口规约"))

        # 以下为手写内容
        self.TCNumPerCyc.setPlaceholderText("1-1000")
        self.timeoutLEdit.setPlaceholderText("1-1000")
        self.fuzzTime.setMaximum(9999)
        # 手写内容结束

    # 以下为手写内容
    '''
    @description: 选择C文件
    @param {*} self
    @param {*} Filepath
    @return {*}
    '''
    def chooseCFile(self, Filepath):
        # 注意！getOpenFileNames()中的filter如果想选择多个文件的话，需要用两个分号隔开！
        # temp = QtWidgets.QFileDialog.getOpenFileNames(None,"choose file","C:/Users/Radon/Desktop/",filter="c files (*.c);;cpp Files (*.cpp)")
        temp = QtWidgets.QFileDialog.getOpenFileNames(None,"choose file","C:/Users/Radon/Desktop/",filter="source file (*.c *.cpp)")
        path = ""
        if len(temp[0]) == 1:
            path = re.sub("/",r"\\",temp[0][0])
        else:
            for i in range(len(temp[0])):
                path += re.sub("/",r"\\",temp[0][i]) + "\n"
        path = path.rstrip("\n")
        self.CFileLoc.setText(path)

    '''
    @description: 选择头文件
    @param {*} self
    @param {*} Filepath
    @return {*}
    '''
    def chooseHFile(self, Filepath):
        temp = QtWidgets.QFileDialog.getOpenFileNames(None,"choose file","C:/Users/Radon/Desktop/","h files (*.h)")
        path = ""
        if len(temp[0]) == 1:
            path = re.sub("/",r"\\",temp[0][0])
        else:
            for i in range(len(temp[0])):
                path += re.sub("/",r"\\",temp[0][i]) + "\n"
        path = path.rstrip("\n")
        self.HFileLoc.setText(path)

    '''
    @description: 弹出模糊测试的窗口, 在测试前，会询问用户是否已将数据维持在了最新状态
                  注意, 需要把C文件与H文件放在同一目录下
    @param {*} self
    @return {*}
    '''
    def popFuzzDialog(self):
        print(self.targetSetInfo.toPlainText())
        source_loc = self.CFileLoc.toPlainText().split("\n")
        for source in source_loc:
            if not os.path.exists(source):
                sourceNotExistBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "C文件不存在！")
                sourceNotExistBox.exec_()
                return
        if not os.path.exists(re.sub(source_loc[0].split("\\")[-1],"",source_loc[0]) + "\\in\\"):
            seedNotExistBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "种子文件不存在！")
            seedNotExistBox.exec_()
            return
        seedLatestBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, '警告', '模糊测试即将开始, 请确认种子文件为最新状态')
        yes = seedLatestBox.addButton('确定', QtWidgets.QMessageBox.YesRole)
        no = seedLatestBox.addButton('修改种子', QtWidgets.QMessageBox.NoRole)
        seedLatestBox.exec_()
        if seedLatestBox.clickedButton() == no:
            seedSetBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "消息", "您可以点击主页面中的手动输入按钮以更新种子")
            seedSetBox.exec_()
            return
        self.fuzzDialog = QtWidgets.QDialog()
        self.uiFuzz = fuzzDialogPY.Ui_Dialog()
        self.uiFuzz.setupUi(self.fuzzDialog)
        self.fuzzDialog.show()
        self.uiFuzz.startFuzz(source_loc,ui,self.uiFuzz)

    def popSeedDialog(self):
        header_loc = self.HFileLoc.toPlainText()
        readJSON = False
        header_loc = header_loc.split("\n")
        for header in header_loc:
            if not os.path.exists(header):
                self.HFileLoc.setText("头文件不存在!")
                headerNotExistBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "头文件不存在！")
                headerNotExistBox.exec_()
                return
        headerMsgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, '发现JSON文件', '发现structDict.json，是否读取？')
        yes = headerMsgBox.addButton('是', QtWidgets.QMessageBox.YesRole)
        no = headerMsgBox.addButton('否', QtWidgets.QMessageBox.NoRole)
        if os.path.exists(re.sub(header_loc[0].split("\\")[-1],"",header_loc[0]) + "\\structDict.json"):
            headerMsgBox.exec_()
            if headerMsgBox.clickedButton() == yes:
                readJSON = True
        self.seedDialog.show()
        self.uiSeed.initStructDict(header_loc,readJSON)

    '''
    @description: 弹出一个dialog, 其中显示了c中所有的函数, 以让用户选择目标
    @param {*} self
    @return {*}
    '''
    def popTargetDialog(self):
        self.targetSetInfo.clear()
        source_loc = self.CFileLoc.toPlainText()
        sourceList = source_loc.split("\n")
        for source in sourceList:
            if not os.path.exists(source):
                self.targetSetInfo.append("被测文件不存在!")
                return
        self.targetDialog = QtWidgets.QDialog()
        self.uiTarget = targetDialogPY.Ui_Dialog()
        self.uiTarget.setupUi(self.targetDialog)
        self.targetDialog.show()
        self.uiTarget.setValues(ui,source_loc,[])
        # self.uiFuzz.startFuzz(source_loc,ui,self.uiFuzz,self.uiSeed)

    '''
    @description: 弹出选择输入结构体的界面，通过选择结构体来得知初始输入的格式
    @param {*} self 需要将header_loc发送给选择结构体的界面。header_loc是列表
    @return {*}
    '''
    def popStructDialog(self):
        header_loc = self.HFileLoc.toPlainText()
        header_loc = header_loc.split("\n")
        # 查看是否已存在structDict.json
        headerMsgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, '发现JSON文件', '发现structDict.json，是否读取？')
        yes = headerMsgBox.addButton('确定', QtWidgets.QMessageBox.YesRole)
        no = headerMsgBox.addButton('取消', QtWidgets.QMessageBox.NoRole)
        readJSON = False
        # 查看header路径是否正确
        for header in header_loc:
            if not os.path.exists(header):
                self.HFileLoc.setText("头文件不存在!")
                headerNotExistBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "头文件不存在！")
                headerNotExistBox.exec_()
                return
        if os.path.exists(re.sub(header_loc[0].split("\\")[-1],"",header_loc[0]) + "in\\structDict.json"):
            headerMsgBox.exec_()
            if headerMsgBox.clickedButton() == yes:
                readJSON = True
        # 如果读取现有的struct.json
        if readJSON:
            self.seedDialog = QtWidgets.QDialog()
            self.uiSeed = seedDialogPY.Ui_Dialog()
            self.uiSeed.setupUi(self.seedDialog)
            self.seedDialog.show()
            # param_struct和["param","allStruct"]只是用来占位置的，因为如果读取json的话并不需要这两个变量
            self.uiSeed.initStructDict(header_loc, readJSON, "param_struct", ["param","allStruct"])
        # 如果不读取现有的struct.json, 或者没有struct.json的话
        else:
            self.structDialog = QtWidgets.QDialog()
            self.uiStruct = structDialogPY.Ui_Dialog()
            self.uiStruct.setupUi(self.structDialog)
            self.structDialog.show()
            self.uiStruct.setValues(header_loc)

    '''
    @description: 通过CPPCHECK进行静态分析获取可能有缺陷的地方
    @param {*} self
    @return {*}
    '''
    def SAByCppcheck(self):
        self.targetSetInfo.clear()
        source_loc = self.CFileLoc.toPlainText()
        self.SAResult = sa.analyze(source_loc)
        if len(self.SAResult) == 0:
            self.targetSetInfo.setText("暂无目标!")
            return
        if isinstance(self.SAResult,str):
            self.targetSetInfo.setText(self.SAResult)
            return
        self.targetDialog = QtWidgets.QDialog()
        self.uiTarget =targetDialogPY.Ui_Dialog()
        self.uiTarget.setupUi(self.targetDialog)
        self.targetDialog.show()
        self.uiTarget.setValues(ui,source_loc,self.SAResult)
    # 手写内容结束

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())