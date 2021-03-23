# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 14, 401, 401))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.B_make = QtWidgets.QPushButton(self.centralwidget)
        self.B_make.setGeometry(QtCore.QRect(630, 370, 151, 41))
        self.B_make.setObjectName("B_make")
        self.B_clip = QtWidgets.QPushButton(self.centralwidget)
        self.B_clip.setGeometry(QtCore.QRect(450, 70, 151, 41))
        self.B_clip.setObjectName("B_clip")
        self.B_file = QtWidgets.QPushButton(self.centralwidget)
        self.B_file.setGeometry(QtCore.QRect(630, 70, 151, 41))
        self.B_file.setObjectName("B_file")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(13, 436, 771, 151))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(452, 20, 281, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.B_browse = QtWidgets.QPushButton(self.centralwidget)
        self.B_browse.setGeometry(QtCore.QRect(740, 20, 41, 31))
        self.B_browse.setObjectName("B_browse")
        self.B_save = QtWidgets.QPushButton(self.centralwidget)
        self.B_save.setGeometry(QtCore.QRect(450, 370, 151, 41))
        self.B_save.setObjectName("B_save")
        self.B_grab = QtWidgets.QPushButton(self.centralwidget)
        self.B_grab.setGeometry(QtCore.QRect(450, 130, 151, 41))
        self.B_grab.setObjectName("B_grab")
        self.B_save_img = QtWidgets.QPushButton(self.centralwidget)
        self.B_save_img.setGeometry(QtCore.QRect(450, 310, 151, 41))
        self.B_save_img.setObjectName("B_save_img")
        self.B_save_text = QtWidgets.QPushButton(self.centralwidget)
        self.B_save_text.setGeometry(QtCore.QRect(630, 130, 151, 41))
        self.B_save_text.setObjectName("B_save_text")
        self.B_make_clip = QtWidgets.QPushButton(self.centralwidget)
        self.B_make_clip.setGeometry(QtCore.QRect(630, 310, 151, 41))
        self.B_make_clip.setObjectName("B_make_clip")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(640, 189, 141, 41))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "二维码"))
        self.B_make.setText(_translate("MainWindow", "生成"))
        self.B_clip.setText(_translate("MainWindow", "识别剪贴板"))
        self.B_file.setText(_translate("MainWindow", "从文件识别"))
        self.B_browse.setText(_translate("MainWindow", "浏览"))
        self.B_save.setText(_translate("MainWindow", "保存"))
        self.B_grab.setText(_translate("MainWindow", "截图识别"))
        self.B_save_img.setText(_translate("MainWindow", "保存图片到剪贴板"))
        self.B_save_text.setText(_translate("MainWindow", "保存结果到剪贴板"))
        self.B_make_clip.setText(_translate("MainWindow", "从剪贴板生成"))
        self.checkBox.setText(_translate("MainWindow", "网址自动打开"))
