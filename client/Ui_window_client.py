# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Project_VSCode\python\fuzzProject\client\window_client.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

from loguru import logger

import sys
import traceback
import os
import re
import time

import Ui_dialog_dataType as dataTypeDialogPY
import Ui_dialog_seed as seedDialogPY
import Ui_dialog_selectStruct as selectStructDialogPY
import Ui_dialog_validation as validateDialogPY
import Ui_dialog_prepareFuzz as prepareFuzzDialogPY

import Ui_dialog_AICfg as aicfgDialogPY

# 初始化logger
logDir = os.path.join(os.path.dirname(__file__), "logs")
if not os.path.exists(logDir):
    os.mkdir(logDir)
logger.add(os.path.join(logDir, "runtime_{time}.log"))
logger.info("Start running...\n")
# ============


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 764)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 30, 161, 16))
        self.label.setObjectName("label")
        self.fileSelectGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.fileSelectGroupBox.setGeometry(QtCore.QRect(79, 70, 561, 231))
        self.fileSelectGroupBox.setObjectName("fileSelectGroupBox")
        self.HFileLoc = QtWidgets.QTextBrowser(self.fileSelectGroupBox)
        self.HFileLoc.setGeometry(QtCore.QRect(20, 20, 521, 71))
        self.HFileLoc.setObjectName("HFileLoc")
        self.chooseHFileBtn = QtWidgets.QPushButton(self.fileSelectGroupBox)
        self.chooseHFileBtn.setGeometry(QtCore.QRect(430, 100, 111, 28))
        self.chooseHFileBtn.setObjectName("chooseHFileBtn")
        self.dataTypeDictLoc = QtWidgets.QTextBrowser(self.fileSelectGroupBox)
        self.dataTypeDictLoc.setGeometry(QtCore.QRect(20, 135, 521, 51))
        self.dataTypeDictLoc.setObjectName("dataTypeDictLoc")
        self.chooseJSONFileBtn = QtWidgets.QPushButton(self.fileSelectGroupBox)
        self.chooseJSONFileBtn.setGeometry(QtCore.QRect(270, 193, 111, 28))
        self.chooseJSONFileBtn.setObjectName("chooseJSONFileBtn")
        self.dataTypeInputBtn = QtWidgets.QPushButton(self.fileSelectGroupBox)
        self.dataTypeInputBtn.setGeometry(QtCore.QRect(390, 193, 151, 28))
        self.dataTypeInputBtn.setObjectName("dataTypeInputBtn")
        self.seedInputGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.seedInputGroupBox.setGeometry(QtCore.QRect(390, 310, 251, 111))
        self.seedInputGroupBox.setObjectName("seedInputGroupBox")
        self.seedInputBtn = QtWidgets.QPushButton(self.seedInputGroupBox)
        self.seedInputBtn.setGeometry(QtCore.QRect(50, 35, 151, 28))
        self.seedInputBtn.setObjectName("seedInputBtn")
        self.isMutateInRangeCheckBox = QtWidgets.QCheckBox(self.seedInputGroupBox)
        self.isMutateInRangeCheckBox.setGeometry(QtCore.QRect(60, 80, 131, 19))
        self.isMutateInRangeCheckBox.setChecked(True)
        self.isMutateInRangeCheckBox.setObjectName("isMutateInRangeCheckBox")
        self.validationGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.validationGroupBox.setGeometry(QtCore.QRect(80, 580, 291, 121))
        self.validationGroupBox.setObjectName("validationGroupBox")
        self.startValidateBtn = QtWidgets.QPushButton(self.validationGroupBox)
        self.startValidateBtn.setGeometry(QtCore.QRect(100, 30, 93, 28))
        self.startValidateBtn.setObjectName("startValidateBtn")
        self.validateTipLabel = QtWidgets.QLabel(self.validationGroupBox)
        self.validateTipLabel.setGeometry(QtCore.QRect(70, 70, 161, 41))
        self.validateTipLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.validateTipLabel.setObjectName("validateTipLabel")
        self.addressSetGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.addressSetGroupBox.setGeometry(QtCore.QRect(80, 310, 291, 111))
        self.addressSetGroupBox.setObjectName("addressSetGroupBox")
        self.senderIPLineEdit = QtWidgets.QLineEdit(self.addressSetGroupBox)
        self.senderIPLineEdit.setGeometry(QtCore.QRect(20, 30, 141, 21))
        self.senderIPLineEdit.setText("")
        self.senderIPLineEdit.setObjectName("senderIPLineEdit")
        self.receiverIPLineEdit = QtWidgets.QLineEdit(self.addressSetGroupBox)
        self.receiverIPLineEdit.setGeometry(QtCore.QRect(20, 70, 141, 21))
        self.receiverIPLineEdit.setObjectName("receiverIPLineEdit")
        self.senderPortLineEdit = QtWidgets.QLineEdit(self.addressSetGroupBox)
        self.senderPortLineEdit.setGeometry(QtCore.QRect(180, 30, 91, 21))
        self.senderPortLineEdit.setText("")
        self.senderPortLineEdit.setObjectName("senderPortLineEdit")
        self.receiverPortLineEdit = QtWidgets.QLineEdit(self.addressSetGroupBox)
        self.receiverPortLineEdit.setGeometry(QtCore.QRect(180, 70, 91, 21))
        self.receiverPortLineEdit.setText("")
        self.receiverPortLineEdit.setObjectName("receiverPortLineEdit")
        self.senderColonLabel = QtWidgets.QLabel(self.addressSetGroupBox)
        self.senderColonLabel.setGeometry(QtCore.QRect(165, 30, 16, 16))
        self.senderColonLabel.setObjectName("senderColonLabel")
        self.receiverColonLabel = QtWidgets.QLabel(self.addressSetGroupBox)
        self.receiverColonLabel.setGeometry(QtCore.QRect(165, 70, 16, 16))
        self.receiverColonLabel.setObjectName("receiverColonLabel")
        self.startFuzzBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startFuzzBtn.setGeometry(QtCore.QRect(390, 640, 251, 61))
        self.startFuzzBtn.setObjectName("startFuzzBtn")
        self.stopOptionGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.stopOptionGroupBox.setGeometry(QtCore.QRect(79, 430, 291, 141))
        self.stopOptionGroupBox.setObjectName("stopOptionGroupBox")
        self.stopByCrash = QtWidgets.QRadioButton(self.stopOptionGroupBox)
        self.stopByCrash.setGeometry(QtCore.QRect(20, 30, 161, 19))
        self.stopByCrash.setChecked(True)
        self.stopByCrash.setObjectName("stopByCrash")
        self.stopByTime = QtWidgets.QRadioButton(self.stopOptionGroupBox)
        self.stopByTime.setGeometry(QtCore.QRect(20, 70, 81, 19))
        self.stopByTime.setObjectName("stopByTime")
        self.stopByTC = QtWidgets.QRadioButton(self.stopOptionGroupBox)
        self.stopByTC.setGeometry(QtCore.QRect(20, 110, 121, 19))
        self.stopByTC.setObjectName("stopByTC")
        self.fuzzTime = QtWidgets.QSpinBox(self.stopOptionGroupBox)
        self.fuzzTime.setGeometry(QtCore.QRect(110, 67, 71, 25))
        self.fuzzTime.setMaximum(9999)
        self.fuzzTime.setObjectName("fuzzTime")
        self.timeUnit = QtWidgets.QComboBox(self.stopOptionGroupBox)
        self.timeUnit.setGeometry(QtCore.QRect(190, 67, 81, 25))
        self.timeUnit.setObjectName("timeUnit")
        self.timeUnit.addItem("")
        self.timeUnit.addItem("")
        self.TCNumsLineEdit = QtWidgets.QLineEdit(self.stopOptionGroupBox)
        self.TCNumsLineEdit.setGeometry(QtCore.QRect(150, 105, 101, 25))
        self.TCNumsLineEdit.setObjectName("TCNumsLineEdit")
        self.amountLabel = QtWidgets.QLabel(self.stopOptionGroupBox)
        self.amountLabel.setGeometry(QtCore.QRect(255, 110, 21, 16))
        self.amountLabel.setObjectName("amountLabel")
        self.optionTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.optionTabWidget.setGeometry(QtCore.QRect(390, 430, 251, 141))
        self.optionTabWidget.setStyleSheet("background-color:rgb(235, 235, 235)")
        self.optionTabWidget.setObjectName("optionTabWidget")
        self.codeStructTab = QtWidgets.QWidget()
        self.codeStructTab.setObjectName("codeStructTab")
        self.TCNumPerCycLabel = QtWidgets.QLabel(self.codeStructTab)
        self.TCNumPerCycLabel.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.TCNumPerCycLabel.setObjectName("TCNumPerCycLabel")
        self.TCNumPerCyc = QtWidgets.QLineEdit(self.codeStructTab)
        self.TCNumPerCyc.setGeometry(QtCore.QRect(137, 15, 71, 30))
        self.TCNumPerCyc.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.TCNumPerCyc.setObjectName("TCNumPerCyc")
        self.pieceLabel = QtWidgets.QLabel(self.codeStructTab)
        self.pieceLabel.setGeometry(QtCore.QRect(210, 20, 21, 16))
        self.pieceLabel.setObjectName("pieceLabel")
        self.timeoutLEdit = QtWidgets.QLineEdit(self.codeStructTab)
        self.timeoutLEdit.setGeometry(QtCore.QRect(137, 55, 71, 30))
        self.timeoutLEdit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.timeoutLEdit.setObjectName("timeoutLEdit")
        self.TCTimeoutLabel = QtWidgets.QLabel(self.codeStructTab)
        self.TCTimeoutLabel.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.TCTimeoutLabel.setObjectName("TCTimeoutLabel")
        self.secondLabel = QtWidgets.QLabel(self.codeStructTab)
        self.secondLabel.setGeometry(QtCore.QRect(210, 60, 21, 16))
        self.secondLabel.setObjectName("secondLabel")
        self.optionTabWidget.addTab(self.codeStructTab, "")
        self.AITab = QtWidgets.QWidget()
        self.AITab.setObjectName("AITab")
        self.AICfgInfo = QtWidgets.QTextBrowser(self.AITab)
        self.AICfgInfo.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.AICfgInfo.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.AICfgInfo.setObjectName("AICfgInfo")
        self.AICfgBtn = QtWidgets.QPushButton(self.AITab)
        self.AICfgBtn.setGeometry(QtCore.QRect(80, 77, 93, 28))
        self.AICfgBtn.setCheckable(False)
        self.AICfgBtn.setObjectName("AICfgBtn")
        self.optionTabWidget.addTab(self.AITab, "")
        self.switchInstrValueEndianLabel = QtWidgets.QLabel(self.centralwidget)
        self.switchInstrValueEndianLabel.setGeometry(QtCore.QRect(400, 580, 81, 20))
        self.switchInstrValueEndianLabel.setObjectName("switchInstrValueEndianLabel")
        self.instrValueEndianComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.instrValueEndianComboBox.setGeometry(QtCore.QRect(480, 580, 91, 21))
        self.instrValueEndianComboBox.setObjectName("instrValueEndianComboBox")
        self.instrValueEndianComboBox.addItem("")
        self.instrValueEndianComboBox.addItem("")
        self.instrValueBitsizeTipLabel = QtWidgets.QLabel(self.centralwidget)
        self.instrValueBitsizeTipLabel.setGeometry(QtCore.QRect(400, 610, 131, 20))
        self.instrValueBitsizeTipLabel.setObjectName("instrValueBitsizeTipLabel")
        self.instrValueBitsizeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.instrValueBitsizeComboBox.setGeometry(QtCore.QRect(480, 610, 91, 21))
        self.instrValueBitsizeComboBox.setObjectName("instrValueBitsizeComboBox")
        self.instrValueBitsizeComboBox.addItem("")
        self.instrValueBitsizeComboBox.addItem("")
        self.instrValueBitsizeComboBox.addItem("")
        self.instrValueBitsizeComboBox.addItem("")
        self.instrValueBitsizeComboBox.addItem("")
        self.instrValueBitsizeComboBox.addItem("")
        self.instrValueBitsizeComboBox.addItem("")
        self.instrValueBitsizeComboBox.addItem("")
        self.localVarEndianLabel = QtWidgets.QLabel(self.centralwidget)
        self.localVarEndianLabel.setGeometry(QtCore.QRect(580, 580, 81, 20))
        self.localVarEndianLabel.setObjectName("localVarEndianLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # ==========connect========================================================
        self.chooseHFileBtn.clicked.connect(self.chooseHFile)
        self.seedInputBtn.clicked.connect(self.popStructDialog)
        self.startValidateBtn.clicked.connect(self.popValidateDialog)
        self.startFuzzBtn.clicked.connect(self.popPrepareFuzzDialog)
        self.chooseJSONFileBtn.clicked.connect(self.chooseJSONFile)
        self.dataTypeInputBtn.clicked.connect(self.popDataTypeDialog)
        self.mainWindow = MainWindow

        self.AICfgBtn.clicked.connect(self.popAICfgDialog)

        # 每轮测试用例数量、超时时间上线为1000，测试用例总数量上线为1亿
        regExp1 = QtCore.QRegExp("^([1-9]\d{0,2}|1000)$")
        self.TCNumPerCyc.setValidator(QtGui.QRegExpValidator(regExp1))
        self.timeoutLEdit.setValidator(QtGui.QRegExpValidator(regExp1))
        regExp2 = QtCore.QRegExp("^([1-9]\d{0,6}|10000000)$")
        self.TCNumsLineEdit.setValidator(QtGui.QRegExpValidator(regExp2))
        self.AICfgDialog = None

        if sys.byteorder == "little":  # 根据电脑的字节序设置插装值下拉框默认值
            self.instrValueEndianComboBox.setCurrentIndex(0)
        else:
            self.instrValueEndianComboBox.setCurrentIndex(1)
        # self.senderIPLineEdit.setText("")
        # self.senderPortLineEdit.setText("9999")
        # self.receiverIPLineEdit.setText("192.168.50.176")
        # self.receiverPortLineEdit.setText("8888")
        # =========================================================================

        self.retranslateUi(MainWindow)
        self.optionTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ================================刷新组件内容==============================
        if sys.byteorder == "little":
            self.localVarEndianLabel.setText("转为小端")
        else:
            self.localVarEndianLabel.setText("转为大端")
        # =========================================================================

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "模糊测试工具 - 客户端"))
        self.label.setText(_translate("MainWindow", "模糊测试工具 - 客户端"))
        self.fileSelectGroupBox.setTitle(_translate("MainWindow", "文件选择"))
        self.HFileLoc.setPlaceholderText(_translate("MainWindow", "头文件位置"))
        self.chooseHFileBtn.setText(_translate("MainWindow", "选择头文件"))
        self.dataTypeDictLoc.setPlaceholderText(_translate("MainWindow", "数据类型文件位置(JSON)"))
        self.chooseJSONFileBtn.setText(_translate("MainWindow", "选择JSON文件"))
        self.dataTypeInputBtn.setText(_translate("MainWindow", "设置数据类型信息"))
        self.seedInputGroupBox.setTitle(_translate("MainWindow", "种子设置"))
        self.seedInputBtn.setText(_translate("MainWindow", "设置种子测试用例"))
        self.isMutateInRangeCheckBox.setText(_translate("MainWindow", "变异体在范围内"))
        self.validationGroupBox.setTitle(_translate("MainWindow", "完整性验证"))
        self.startValidateBtn.setText(_translate("MainWindow", "开始验证"))
        self.validateTipLabel.setText(_translate("MainWindow", "验证目前是否已持有进行\n" "模糊测试的必要文件"))
        self.addressSetGroupBox.setTitle(_translate("MainWindow", "地址设置"))
        self.senderIPLineEdit.setToolTip(_translate("MainWindow", "通常为本机IP地址"))
        self.senderIPLineEdit.setPlaceholderText(_translate("MainWindow", "发送方IP地址"))
        self.receiverIPLineEdit.setPlaceholderText(_translate("MainWindow", "接收方IP地址"))
        self.senderPortLineEdit.setPlaceholderText(_translate("MainWindow", "端口"))
        self.receiverPortLineEdit.setPlaceholderText(_translate("MainWindow", "端口"))
        self.senderColonLabel.setText(_translate("MainWindow", ":"))
        self.receiverColonLabel.setText(_translate("MainWindow", ":"))
        self.startFuzzBtn.setText(_translate("MainWindow", "开始测试"))
        self.stopOptionGroupBox.setTitle(_translate("MainWindow", "终止条件"))
        self.stopByCrash.setText(_translate("MainWindow", "检测到错误就停止"))
        self.stopByTime.setText(_translate("MainWindow", "按时间"))
        self.stopByTC.setText(_translate("MainWindow", "按测试用例数"))
        self.timeUnit.setItemText(0, _translate("MainWindow", "分钟"))
        self.timeUnit.setItemText(1, _translate("MainWindow", "小时"))
        self.TCNumsLineEdit.setText(_translate("MainWindow", "2000"))
        self.amountLabel.setText(_translate("MainWindow", "个"))
        self.TCNumPerCycLabel.setText(_translate("MainWindow", "每轮测试用例生成"))
        self.TCNumPerCyc.setText(_translate("MainWindow", "5"))
        self.pieceLabel.setText(_translate("MainWindow", "个"))
        self.timeoutLEdit.setText(_translate("MainWindow", "10"))
        self.TCTimeoutLabel.setText(_translate("MainWindow", "测试用例超时时间"))
        self.secondLabel.setText(_translate("MainWindow", "秒"))
        self.optionTabWidget.setTabText(self.optionTabWidget.indexOf(self.codeStructTab), _translate("MainWindow", "代码结构"))
        self.AICfgBtn.setText(_translate("MainWindow", "设置"))
        self.optionTabWidget.setTabText(self.optionTabWidget.indexOf(self.AITab), _translate("MainWindow", "交互接口规约"))
        self.switchInstrValueEndianLabel.setText(_translate("MainWindow", "将插装值从"))
        self.instrValueEndianComboBox.setCurrentText(_translate("MainWindow", "小端"))
        self.instrValueEndianComboBox.setItemText(0, _translate("MainWindow", "小端"))
        self.instrValueEndianComboBox.setItemText(1, _translate("MainWindow", "大端"))
        self.instrValueBitsizeTipLabel.setText(_translate("MainWindow", "插装变量为"))
        self.instrValueBitsizeComboBox.setCurrentText(_translate("MainWindow", "8位"))
        self.instrValueBitsizeComboBox.setItemText(0, _translate("MainWindow", "8位"))
        self.instrValueBitsizeComboBox.setItemText(1, _translate("MainWindow", "无符号8位"))
        self.instrValueBitsizeComboBox.setItemText(2, _translate("MainWindow", "16位"))
        self.instrValueBitsizeComboBox.setItemText(3, _translate("MainWindow", "无符号16位"))
        self.instrValueBitsizeComboBox.setItemText(4, _translate("MainWindow", "32位"))
        self.instrValueBitsizeComboBox.setItemText(5, _translate("MainWindow", "无符号32位"))
        self.instrValueBitsizeComboBox.setItemText(6, _translate("MainWindow", "64位"))
        self.instrValueBitsizeComboBox.setItemText(7, _translate("MainWindow", "无符号64位"))
        self.localVarEndianLabel.setText(_translate("MainWindow", "转为X端"))

    # ==========定义功能================================================================

    def chooseHFile(self):
        """选择头文件

        Notes
        -----
        [description]
        """
        temp = QtWidgets.QFileDialog.getOpenFileNames(None, "choose file", "C:/Users/Radon/Desktop/", "h files (*.h)")
        path = ""
        if len(temp[0]) == 0:
            return
        for i in range(len(temp[0])):
            path += temp[0][i] + "\n"
        path = path.rstrip("\n")
        self.HFileLoc.setText(path)

    def chooseJSONFile(self):
        """选择数据类型JSON文件

        Notes
        -----
        [description]
        """
        path = QtWidgets.QFileDialog.getOpenFileName(None, "choose file", "C:/Users/Radon/Desktop/", "json files (*.json)")
        self.dataTypeDictLoc.setText(path[0])

    def popAICfgDialog(self):
        self.AICfgDialog = aicfgDialogPY.Ui_Dialog(self.AICfgInfo)
        self.AICfgDialog.show()

    def popDataTypeDialog(self):
        typeJSONPath = self.dataTypeDictLoc.toPlainText()

        # 如果JSON文件不存在
        if not os.path.exists(typeJSONPath):
            JSONNotExistBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, "消息", "JSON文件不存在，是否使用默认值?")
            yes = JSONNotExistBox.addButton("是", QtWidgets.QMessageBox.YesRole)
            no = JSONNotExistBox.addButton("否", QtWidgets.QMessageBox.NoRole)
            JSONNotExistBox.exec_()
            if JSONNotExistBox.clickedButton() == no:
                return  # 如果使用默认值则继续，否则就结束

        try:
            dataTypeDialog = QtWidgets.QDialog()
            uiDataType = dataTypeDialogPY.Ui_Dialog()
            uiDataType.setupUi(dataTypeDialog)
            uiDataType.initDataTypeDict(typeJSONPath)
            dataTypeDialog.show()
        except BaseException as e:
            print("\033[1;31m")
            traceback.print_exc()
            print("\033[0m")
            logger.exception("Exception in " + os.path.basename(__file__) + ", popDataType func")
            errBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "出错:" + str(e))
            errBox.exec_()

    def popStructDialog(self):
        """弹出选择结构体的界面

        Parameters
        ----------
        choice : str
            表示按下了哪个按钮，如果按下了输入按钮choice的值就是input，输出是output

        Notes
        -----
        [description]
        """

        methods = ("读取测试用例JSON文件", "读取测试用例二进制文件并使用默认数据类型字典", "读取测试用例二进制文件并使用数据类型字典JSON文件", "手动设置测试用例并使用默认数据类型字典", "手动设置测试用例并使用数据类型字典JSON文件")
        item, okPressed = QtWidgets.QInputDialog.getItem(self.mainWindow, "选择输入方式", "选择输入方式", methods, 0, False)
        if not okPressed:
            return

        self.header_loc_list = self.HFileLoc.toPlainText().split("\n")
        typeJSONPath = self.dataTypeDictLoc.toPlainText()
        for header in self.header_loc_list:  # 检测头文件是否存在
            if not os.path.exists(header):
                headerNotExistBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "头文件不存在!")
                headerNotExistBox.exec_()
                return

        if item == "读取测试用例JSON文件":
            selectedFile = QtWidgets.QFileDialog.getOpenFileName(None, "choose file", "C:/Users/Radon/Desktop/", filter="json file (*.json)")
            seedJSONPath = selectedFile[0]
            try:
                # 如果seedJSONPath是空字符串，表示用户点击了右上角的X
                if seedJSONPath == "":
                    return
                self.seedDialog = QtWidgets.QDialog()
                self.uiSeed = seedDialogPY.Ui_Dialog()
                self.uiSeed.setupUi(self.seedDialog)
                # 如果读取JSON的话，后两个参数其实是用不上的
                self.uiSeed.initStructDict(self.header_loc_list, seedJSONPath, True, self, struct="struct", allStruct=["all", "struct"])
                self.seedDialog.show()
            except BaseException as e:
                traceback.print_exc()
                loadJSONFailedBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "读取失败", "JSON文件读取失败: " + str(e))
                loadJSONFailedBox.exec_()
        elif item == "手动设置测试用例并使用默认数据类型字典":
            # 检查clang是否安装正确
            if os.system("clang -v") != 0:
                clangInstallErrBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "未检测到clang")
                clangInstallErrBox.exec_()
                return
            try:
                self.selectStructDialog = QtWidgets.QDialog()
                self.uiSelectStruct = selectStructDialogPY.Ui_Dialog()
                self.uiSelectStruct.setupUi(self.selectStructDialog)
                self.uiSelectStruct.setValues(self.header_loc_list, "", self)
                self.selectStructDialog.show()
            except BaseException as e:
                analyzeStructErrBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "分析结构体时出错:" + str(e))
                analyzeStructErrBox.exec_()
                # 提示用户解决方案
                analyzeStructTipBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "提示",
                                                            "推荐解决方案:\n" + "1.请确认代码无误\n" + "2.请给结构体定义别名，否则可能会导致显示不全\n" + "3.目前仅支持C语言, 请确认代码中仅有C语言的关键字")
                analyzeStructTipBox.exec_()
                print("\033[1;31m")
                traceback.print_exc()
                print("\033[0m")
        elif item == "手动设置测试用例并使用数据类型字典JSON文件":
            # 检查clang是否安装正确
            if os.system("clang -v") != 0:
                clangInstallErrBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "未检测到clang")
                clangInstallErrBox.exec_()
                return
            # 检查数据类型JSON文件是否存在
            if not os.path.exists(typeJSONPath):
                whetherUseDefaultTypeDictBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, "提示", "未检测到数据类型JSON文件，是否使用默认数据类型字典?")
                yes = whetherUseDefaultTypeDictBox.addButton("是", QtWidgets.QMessageBox.YesRole)
                no = whetherUseDefaultTypeDictBox.addButton("否", QtWidgets.QMessageBox.NoRole)
                whetherUseDefaultTypeDictBox.exec_()
                if whetherUseDefaultTypeDictBox.clickedButton() == no:
                    return
            try:
                self.selectStructDialog = QtWidgets.QDialog()
                self.uiSelectStruct = selectStructDialogPY.Ui_Dialog()
                self.uiSelectStruct.setupUi(self.selectStructDialog)
                self.uiSelectStruct.setValues(self.header_loc_list, typeJSONPath, self)
                self.selectStructDialog.show()
            except BaseException as e:
                analyzeStructErrBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "分析结构体时出错:" + str(e))
                analyzeStructErrBox.exec_()
                # 提示用户解决方案
                analyzeStructTipBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "提示",
                                                            "推荐解决方案:\n" + "1.请确认代码无误\n" + "2.请给结构体定义别名，否则可能会导致显示不全\n" + "3.目前仅支持C语言, 请确认代码中仅有C语言的关键字")
                analyzeStructTipBox.exec_()
                print("\033[1;31m")
                traceback.print_exc()
                print("\033[0m")
        elif item == "读取测试用例二进制文件并使用默认数据类型字典":
            # 获得测试用例二进制文件路径
            # 弹出结构体选择界面，选择测试用例对应的结构体
            # 显示测试用例中每个变量的内容
            helpBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "消息",
                                            "读取测试用例二进制文件并使用默认数据类型字典, 流程如下:\n" + "1.选择无扩展名的二进制文件作为读取对象\n" + "2.选择测试用例对应的结构体\n" + "3.等待读取结果")
            helpBox.exec_()
            selectedFile = QtWidgets.QFileDialog.getOpenFileName(None, "选择种子文件", "C:/Users/Radon/Desktop/", filter="All file (*)")
            seedBinaryPath = selectedFile[0]
            if len(seedBinaryPath) == 0:
                return
            elif len(os.path.splitext(seedBinaryPath)[-1]) > 0:
                notBinFileBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "消息", "请选择无扩展名的二进制文件")
                notBinFileBox.exec_()
            else:
                try:
                    self.selectStructDialog = QtWidgets.QDialog()
                    self.uiSelectStruct = selectStructDialogPY.Ui_Dialog()
                    self.uiSelectStruct.setupUi(self.selectStructDialog)
                    self.uiSelectStruct.setSeedBinaryPath(seedBinaryPath)
                    self.uiSelectStruct.setValues(self.header_loc_list, "", self)
                    self.selectStructDialog.show()
                except BaseException as e:
                    analyzeStructErrBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "分析结构体时出错:" + str(e))
                    analyzeStructErrBox.exec_()
                    # 提示用户解决方案
                    analyzeStructTipBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "提示",
                                                                "推荐解决方案:\n" + "1.请确认代码无误\n" + "2.请给结构体定义别名，否则可能会导致显示不全\n" + "3.目前仅支持C语言, 请确认代码中仅有C语言的关键字")
                    analyzeStructTipBox.exec_()
                    print("\033[1;31m")
                    traceback.print_exc()
                    print("\033[0m")
        elif item == "读取测试用例二进制文件并使用数据类型字典JSON文件":
            # 获得测试用例二进制文件路径，数据类型字典JSON文件路径
            # 弹出结构体选择界面，选择测试用例对应的结构体
            # 显示测试用例中每个变量的内容
            helpBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "消息",
                                            "读取测试用例二进制文件并使用数据类型字典JSON文件, 流程如下:\n" + "1.选择无扩展名的二进制文件作为读取对象\n" + "2.选择测试用例对应的结构体\n" + "3.等待读取结果")
            helpBox.exec_()
            if not os.path.exists(typeJSONPath):
                typeJSONNotExistBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, "消息", "未检测到数据类型JSON文件，是否使用默认设置?")
                yes = typeJSONNotExistBox.addButton("是", QtWidgets.QMessageBox.YesRole)
                no = typeJSONNotExistBox.addButton("否", QtWidgets.QMessageBox.NoRole)
                typeJSONNotExistBox.exec_()
                if typeJSONNotExistBox.clickedButton() == no:
                    return
            selectedFile = QtWidgets.QFileDialog.getOpenFileName(None, "选择种子二进制文件", "C:/Users/Radon/Desktop/", filter="All file (*)")
            seedBinaryPath = selectedFile[0]
            if len(seedBinaryPath) == 0:
                return
            elif len(os.path.splitext(seedBinaryPath)[-1]) > 0:
                notBinFileBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "消息", "请选择无扩展名的二进制文件")
                notBinFileBox.exec_()
            else:
                try:
                    self.selectStructDialog = QtWidgets.QDialog()
                    self.uiSelectStruct = selectStructDialogPY.Ui_Dialog()
                    self.uiSelectStruct.setupUi(self.selectStructDialog)
                    self.uiSelectStruct.setSeedBinaryPath(seedBinaryPath)
                    self.uiSelectStruct.setValues(self.header_loc_list, typeJSONPath, self)
                    self.selectStructDialog.show()
                except BaseException as e:
                    analyzeStructErrBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "分析结构体时出错:" + str(e))
                    analyzeStructErrBox.exec_()
                    # 提示用户解决方案
                    analyzeStructTipBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "提示",
                                                                "推荐解决方案:\n" + "1.请确认代码无误\n" + "2.请给结构体定义别名，否则可能会导致显示不全\n" + "3.目前仅支持C语言, 请确认代码中仅有C语言的关键字")
                    analyzeStructTipBox.exec_()
                    print("\033[1;31m")
                    traceback.print_exc()
                    print("\033[0m")
        else:
            workingBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "警告", "选择了列表中没有的内容")
            workingBox.exec_()

    def popValidateDialog(self):
        """弹出验证完整性的对话框

        Notes
        -----
        [description]
        """
        try:
            header_loc_list = self.HFileLoc.toPlainText().split("\n")
            for header in header_loc_list:
                if not os.path.exists(header):
                    headerNotExistBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "头文件不存在")
                    headerNotExistBox.exec_()
                    return
            self.validateDialog = QtWidgets.QDialog()
            self.uiValidate = validateDialogPY.Ui_Dialog()
            self.uiValidate.setupUi(self.validateDialog)
            self.validateDialog.show()
            self.uiValidate.startValidate(header_loc_list)
        except BaseException as e:
            validateErrBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "验证失败: " + str(e))
            validateErrBox.exec_()
            print("\033[1;31m")
            traceback.print_exc()
            print("\033[0m]")

    def popPrepareFuzzDialog(self):
        header_loc_list = self.HFileLoc.toPlainText().split("\n")
        for header in header_loc_list:
            if not os.path.exists(header):
                headerNotExistBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "头文件不存在")
                headerNotExistBox.exec_()
                return

        # IPAddress列表中存储了发送方与接收方的IP，0是发送方，1是接收方
        IPAddressList = list()
        IPAddressList.append(self.senderIPLineEdit.text() + ":" + self.senderPortLineEdit.text())
        IPAddressList.append(self.receiverIPLineEdit.text() + ":" + self.receiverPortLineEdit.text())

        self.prepareFuzzDialog = QtWidgets.QDialog()
        self.uiPrepareFuzz = prepareFuzzDialogPY.Ui_Dialog()
        self.uiPrepareFuzz.setupUi(self.prepareFuzzDialog)
        self.prepareFuzzDialog.show()
        self.uiPrepareFuzz.setValues(self, header_loc_list, IPAddressList)

    # ==================================================================================


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())