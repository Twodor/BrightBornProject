# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proje3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from string import digits

from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtWidgets import QFileDialog
import PyQt5.QtWidgets
import doctor
import basicReport


class Ui_Dialog(object):
    def __init__(self, name, surname, ID):
        self.name = name
        self.surname = surname
        self.ID = str(ID)



    def saveText(self):
        print("anna")

    def pushButtonHandlerMan(self):
        self.dialogBoxMan()
    def dialogBoxMan(self):
        remove_digits = str.maketrans('', '', digits)
        filePath = QFileDialog.getOpenFileName()
        path = filePath[0]
        print(path)
        a = open (path,"r").read().replace(" ","").translate(remove_digits).replace("\n", "")

        self.cftrMan = a[282662:471362]
        self.hbbMan = a[754024:755584]
        self.httMan = a[1038246:1207506]
        self.tp53Man = a[1490168:1509308]
        self.pahMan = a[1791970:1913470]
        self.oca2Man = a[1913470:2257870]

    def pushButtonHandlerWoman(self):
        self.dialogBoxWoman()
    def dialogBoxWoman(self):
        remove_digits = str.maketrans('', '', digits)
        filePath = QFileDialog.getOpenFileName()
        path = filePath[0]
        print(path)
        a = open(path, "r").read().replace(" ", "").translate(remove_digits).replace("\n", "")
        self.cftrWoman = a[282662:471362]
        self.hbbWoman  = a[754024:755584]
        self.httWoman  = a[1038246:1207506]
        self.tp53Woman  = a[1490168:1509308]
        self.pahWoman  = a[1791970:1913470]
        self.oca2Woman  = a[1913470:2257870]

    def browse(self):
        filePath = QFileDialog.getOpenFileName(self,'Single File',"C:/Users/ASUS/PycharmProjects/BrightBorn/myPackage/documents",'*.text')
        print('filePath ',filePath)
        fileHandle = open(filePath,'r')
        lines = fileHandle.readlines()
        for line in lines:
            print(line)
    def openSayfa5(self):
        self.window = QtWidgets.QMainWindow()
        self.message = self.reportID.text()
        print(self.message)
        self.ui = basicReport.Ui_Dialog(self.message)
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

        self.doctorID = QtWidgets.QTextEdit(Dialog)
        self.doctorID.setGeometry(QtCore.QRect(10, 230, 161, 31))
        self.doctorID.setObjectName("textEdit")

        self.doctorName = QtWidgets.QTextEdit(Dialog)
        self.doctorName.setGeometry(QtCore.QRect(10, 300, 161, 31))
        self.doctorName.setObjectName("textEdit_2")

        self.doctorSurname = QtWidgets.QTextEdit(Dialog)
        self.doctorSurname.setGeometry(QtCore.QRect(10, 370, 161, 31))
        self.doctorSurname.setObjectName("textEdit_3")

        self.radioButtonFemale = QtWidgets.QRadioButton(Dialog)
        self.radioButtonFemale.setGeometry(QtCore.QRect(530, 200, 82, 17))
        self.radioButtonFemale.setObjectName("radioButton_2")

        self.fullNamePatient1 = QtWidgets.QLineEdit(Dialog)
        self.fullNamePatient1.setGeometry(QtCore.QRect(280, 250, 104, 31))
        self.fullNamePatient1.setObjectName("textEdit_4")

        self.patientIDPatient1 = QtWidgets.QLineEdit(Dialog)
        self.patientIDPatient1.setGeometry(QtCore.QRect(280, 310, 104, 31))
        self.patientIDPatient1.setObjectName("textEdit_5")

        self.saveButtonMan = QtWidgets.QPushButton(Dialog)
        self.saveButtonMan.setGeometry(QtCore.QRect(300, 380, 75, 61))
        self.saveButtonMan.setText("")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pictures/submit.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButtonMan.setIcon(icon)
        self.saveButtonMan.setIconSize(QtCore.QSize(32, 32))
        self.saveButtonMan.setObjectName("pushButton_2")
        self.saveButtonMan.clicked.connect(self.pushButtonHandlerMan)

        self.saveButtonWoman = QtWidgets.QPushButton(Dialog)
        self.saveButtonWoman.setGeometry(QtCore.QRect(530, 380, 75, 61))
        self.saveButtonWoman.setText("")
        self.saveButtonWoman.setIcon(icon)
        self.saveButtonWoman.setIconSize(QtCore.QSize(32, 32))
        self.saveButtonWoman.setObjectName("pushButton_3")
        self.saveButtonWoman.clicked.connect(self.pushButtonHandlerWoman)

        self.radioButtonMale = QtWidgets.QRadioButton(Dialog)
        self.radioButtonMale.setGeometry(QtCore.QRect(300, 200, 61, 20))
        self.radioButtonMale.setObjectName("radioButton")

        self.fullNamePatient2 = QtWidgets.QLineEdit(Dialog)
        self.fullNamePatient2.setGeometry(QtCore.QRect(510, 250, 104, 31))
        self.fullNamePatient2.setObjectName("textEdit_6")

        self.patientIDPatient2 = QtWidgets.QLineEdit(Dialog)
        self.patientIDPatient2.setGeometry(QtCore.QRect(510, 310, 104, 31))
        self.patientIDPatient2.setObjectName("textEdit_7")

        self.reportID = QtWidgets.QLineEdit(Dialog)
        self.reportID.setGeometry(QtCore.QRect(370, 20, 201, 61))
        self.reportID.setObjectName("textEdit_8")

        self.searchReportID = QtWidgets.QPushButton(Dialog)
        self.searchReportID.setGeometry(QtCore.QRect(430, 110, 75, 23))
        self.searchReportID.setObjectName("pushButton")
        self.searchReportID.clicked.connect(self.openSayfa5)

        self.submitData = QtWidgets.QPushButton(Dialog)
        self.submitData.setGeometry(QtCore.QRect(420, 470, 75, 23))
        self.submitData.setObjectName("pushButton_4")
        self.submitData.clicked.connect(self.saveText)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 111, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/ASUS/PycharmProjects/BrightBorn/myPackage/images/doctor.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.radioButtonMale.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.doctorID.raise_()
        self.doctorName.raise_()
        self.doctorSurname.raise_()
        self.radioButtonFemale.raise_()
        self.fullNamePatient1.raise_()
        self.saveButtonMan.raise_()
        self.patientIDPatient1.raise_()
        self.fullNamePatient2.raise_()
        self.patientIDPatient2.raise_()
        self.saveButtonWoman.raise_()
        self.reportID.raise_()
        self.searchReportID.raise_()
        self.submitData.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.doctorID.setHtml(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; color:#4f4f4f;\">Doctor ID: " + self.ID + "</span></p></body></html>"))
        self.doctorName.setHtml(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; color:#4f4f4f;\">Name: " + self.name + "</span></p></body></html>"))
        self.doctorSurname.setHtml(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; color:#4f4f4f;\">Surname: " + self.surname + "</span></p></body></html>"))
        self.radioButtonFemale.setText(_translate("Dialog", "Female"))

        self.radioButtonMale.setText(_translate("Dialog", "Male"))


        self.searchReportID.setText(_translate("Dialog", "Check Report"))
        self.submitData.setText(_translate("Dialog", "Submit Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

