# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\VSCode_Project\python_project\fuzzProject\window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread,pyqtSignal
import sys
import re

import fuzz


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setIconSize(QtCore.QSize(20, 20))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.instrBtn = QtWidgets.QPushButton(self.centralwidget)
        self.instrBtn.setGeometry(QtCore.QRect(510, 190, 93, 30))
        self.instrBtn.setObjectName("instrBtn")

        self.staticAnalyzeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.staticAnalyzeBtn.setGeometry(QtCore.QRect(510, 130, 93, 30))
        self.staticAnalyzeBtn.setObjectName("staticAnalyzeBtn")

        self.startFuzzBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startFuzzBtn.setGeometry(QtCore.QRect(510, 250, 93, 30))
        self.startFuzzBtn.setIconSize(QtCore.QSize(40, 40))
        self.startFuzzBtn.setObjectName("startFuzzBtn")

        self.chooseFileTBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.chooseFileTBrowser.setGeometry(QtCore.QRect(80, 80, 371, 30))
        self.chooseFileTBrowser.setObjectName("chooseFileTBrowser")

        self.fuzzInfoTBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.fuzzInfoTBrowser.setGeometry(QtCore.QRect(80, 130, 371, 300))
        self.fuzzInfoTBrowser.setObjectName("fuzzInfoTBrowser")

        self.chooseCBtn = QtWidgets.QPushButton(self.centralwidget)
        self.chooseCBtn.setGeometry(QtCore.QRect(510, 80, 93, 30))
        self.chooseCBtn.setObjectName("chooseCBtn")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.chooseCBtn.clicked.connect(self.chooseFile)
        self.startFuzzBtn.clicked.connect(self.startFuzz)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chooseCBtn.setText(_translate("MainWindow", "选择C文件"))
        self.instrBtn.setText(_translate("MainWindow", "插桩"))
        self.staticAnalyzeBtn.setText(_translate("MainWindow", "静态分析"))
        self.startFuzzBtn.setText(_translate("MainWindow", "开始测试"))
        self.chooseFileTBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">C文件位置</p></body></html>"))
        self.fuzzInfoTBrowser.setHtml(_translate("MainWindow", "模糊测试信息"))

    def chooseFile(self, Filepath):
        m = QtWidgets.QFileDialog.getOpenFileName(None,"choose file","C:/Users/Radon/Desktop/","c files (*.c)")
        path = re.sub("/",r"\\",m[0])
        self.chooseFileTBrowser.setText(path)
    
    def startFuzz(self):
        source_loc = self.chooseFileTBrowser.toPlainText()
        self.startFuzzBtn.setEnabled(False)
        self.chooseCBtn.setEnabled(False)
        print(source_loc)
        self.fuzzInfoTBrowser.setText("开始测试...")
        # self.fuzzThread = FuzzThread()
        # self.fuzzThread.over.connect(self.overFuzz)
        # self.fuzzThread.setSourceLoc(source_loc)
        fuzz.fuzz(source_loc,ui)
        self.fuzzInfoTBrowser.append("\n测试结束.")
        self.startFuzzBtn.setEnabled(True)
        self.chooseCBtn.setEnabled(True)
    
    def overFuzz(self):
        self.fuzzInfoTBrowser.append("测试结束.")
        self.startFuzzBtn.setEnabled(True)
        self.chooseCBtn.setEnabled(True)
    
    def fuzzInfoPrint(self,fuzzInfo):
        # self.fuzzInfoTBrowser.setText(fuzzInfo)
        self.fuzzInfoTBrowser.setText(fuzzInfo)
        QtWidgets.QApplication.processEvents()
        print(fuzzInfo)

class FuzzThread(QThread):
    # 模糊测试用一个新线程，不然会暂时卡死
    over = pyqtSignal(bool)
    def __init__(self):
        super().__init__()
    def setSourceLoc(self,source_loc):
        self.source_loc = source_loc
        self.start()
    def run(self):
        print("FuzzThread has started.")
        fuzz.fuzz(self.source_loc,ui)
        self.over.emit(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())