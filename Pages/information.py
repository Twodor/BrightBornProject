# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proje8.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, QTextCursor
from PyQt5.QtWidgets import QListWidgetItem


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(780, 486)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 50, 431, 51))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(240, 140, 20, 351))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 130, 781, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(520, 140, 20, 351))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 131, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(260, 160, 131, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(550, 150, 171, 71))
        self.label_4.setObjectName("label_4")

        self.bb = "It is an easy and safe way to predict your childs gene combinations"
        self.brightborn = QtWidgets.QTextBrowser(Dialog)
        self.brightborn.setGeometry(QtCore.QRect(10, 210, 211, 251))
        self.brightborn.setObjectName("textBrowser")
        self.brightborn.setFontPointSize(12)
        self.brightborn.setText(self.bb)

        self.use = "Just upload your DNA code, we will handle the rest :)"
        self.howToUse = QtWidgets.QTextBrowser(Dialog)
        self.howToUse.setGeometry(QtCore.QRect(280, 210, 211, 251))
        self.howToUse.setObjectName("textBrowser_2")
        self.howToUse.setFontPointSize(12)
        self.howToUse.setText(self.use)

        self.calculation ="We are taking couples DNA, simulating crossing over as mother nature does and combining them with the high accuracy calculations to give the best result for your future..."
        self.howCalculationWorks = QtWidgets.QTextBrowser(Dialog)
        self.howCalculationWorks.setGeometry(QtCore.QRect(550, 220, 211, 251))
        self.howCalculationWorks.setObjectName("textBrowser_3")
        self.howCalculationWorks.setFontPointSize(12)
        self.howCalculationWorks.setText(self.calculation)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Brightborn Information"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:36pt; font-style:italic; color:#316394;\">What is BrightBorn?</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">BrightBorn...</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">How to use...</span></p><p><br/></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">How calculation </span></p><p><span style=\" font-size:16pt; font-weight:600;\">works...</span></p><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

