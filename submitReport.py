# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proje3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtWidgets import QFileDialog
import PyQt5.QtWidgets
import doctor
import basicReport


class Ui_Dialog(object):
    def pushButtonHandler(self):
        print("button clicked")
        self.dialogBox()
    def dialogBox(self):
        filePath = QFileDialog.getOpenFileName()
        path = filePath[0]
        print(path)
        with open (path,"r") as f:
            print(f.readlines())
    def browse(self):
        filePath = QFileDialog.getOpenFileName(self,'Single File',"C:/Users/ASUS/PycharmProjects/BrightBorn/myPackage/documents",'*.text')
        print('filePath ',filePath)
        fileHandle = open(filePath,'r')
        lines = fileHandle.readlines()
        for line in lines:
            print(line)
    def openSayfa5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = basicReport.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(710, 532)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(180, 150, 581, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(170, 0, 20, 521))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 230, 161, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 300, 161, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 370, 161, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(530, 200, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(280, 250, 104, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 380, 75, 61))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/ASUS/PycharmProjects/BrightBorn/myPackage/images/submit.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pushButtonHandler)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 380, 75, 61))
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.pushButtonHandler)

        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(300, 200, 61, 20))
        self.radioButton.setObjectName("radioButton")
        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(280, 310, 104, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_6.setGeometry(QtCore.QRect(510, 250, 104, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_7.setGeometry(QtCore.QRect(510, 310, 104, 31))
        self.textEdit_7.setObjectName("textEdit_7")

        self.textEdit_8 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_8.setGeometry(QtCore.QRect(370, 20, 201, 61))
        self.textEdit_8.setObjectName("textEdit_8")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openSayfa5)

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 470, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 111, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/ASUS/PycharmProjects/BrightBorn/myPackage/images/doctor.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.radioButton.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.textEdit.raise_()
        self.textEdit_2.raise_()
        self.textEdit_3.raise_()
        self.radioButton_2.raise_()
        self.textEdit_4.raise_()
        self.pushButton_2.raise_()
        self.textEdit_5.raise_()
        self.textEdit_6.raise_()
        self.textEdit_7.raise_()
        self.pushButton_3.raise_()
        self.textEdit_8.raise_()
        self.pushButton.raise_()
        self.pushButton_4.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Doctor ID:</p></body></html>"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Name :</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Surname :</span></p></body></html>"))
        self.radioButton_2.setText(_translate("Dialog", "Female"))
        self.textEdit_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Full Name</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>"))
        self.radioButton.setText(_translate("Dialog", "Male"))
        self.textEdit_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Patient ID</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>"))
        self.textEdit_6.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Full Name</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>"))
        self.textEdit_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Patient ID</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>"))
        self.textEdit_8.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#767676;\">  Report ID</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Check Report"))
        self.pushButton_4.setText(_translate("Dialog", "Submit Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

