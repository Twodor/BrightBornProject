# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proje5.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets

import complexReport, patientLogin

connection = mysql.connector.connect(host='localhost',
                                     database='se315',
                                     user='root',
                                     password='')

cursor = connection.cursor()


class Ui_Dialog(object):
    def __init__(self, message):
        self.ID = message
        print("ID:", self.ID)
        query = "Select * FROM patients WHERE id = %s"
        cursor.execute(query, (self.ID,))
        result = cursor.fetchall()
        for row in result:
            self.reshbb = "HBB status: " + row[7] + "\n"
            self.rescftr = "CFTR status: " + row[8] + "\n"
            self.resoca2 = "OCA2 status: " + row[9] + "\n"
            self.respah = "PAH status: " + row[10] + "\n"
            self.reshtt = "HTT status: " + row[11] + "\n"
            self.resp53 = "P53 status: " + row[12] + "\n"
            self.name = "NAME status: " + row[13] + "\n"
        self.values = self.reshbb + self.rescftr + self.resoca2 + self.respah + self.reshtt + self.resp53

    def complexReport(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = complexReport.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(706, 512)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 10, 241, 51))
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 110, 211, 151))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setText(self.values)

        '''
        self.textBrowser_2.setText(self.rescftr)
        self.textBrowser_2.setText(self.resoca2)
        self.textBrowser_2.setText(self.respah)
        self.textBrowser_2.setText(self.reshtt)
        self.textBrowser_2.setText(self.resp53)
        '''

        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(310, 110, 211, 151))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(40, 290, 211, 151))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(310, 290, 211, 151))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(500, 450, 201, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.complexReport)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(550, 20, 131, 151))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Report"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:18pt; color:#5d5d5d;\">Report ID : "+self.ID+"</span></p></body></html>"))
        self.commandLinkButton.setText(_translate("Dialog", "Detailed Report"))
        self.label_3.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:11pt; font-style:italic; color:#ff0000;\">Some of the</span></p><p><span style=\" font-size:11pt; font-style:italic; color:#ff0000;\">information must</span></p><p><span style=\" font-size:11pt; font-style:italic; color:#ff0000;\">be colored due to</span></p><p><span style=\" font-size:11pt; font-style:italic; color:#ff0000;\">complexity of</span></p><p><span style=\" font-size:11pt; font-style:italic; color:#ff0000;\">understing for the</span></p><p><span style=\" font-size:11pt; font-style:italic; color:#ff0000;\">patients</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
