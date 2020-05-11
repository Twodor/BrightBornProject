# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proje3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from string import digits

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtWidgets import QFileDialog
import PyQt5.QtWidgets
import doctor
import basicReport

connection = mysql.connector.connect(host='localhost',
                                     database='se315',
                                     user='root',
                                     password='')

cursor = connection.cursor()

hbbQuery = "SELECT  * FROM hbbmutant"
cftrQuery = "SELECT * FROM cftrmutant"
httQuery = "SELECT  * FROM httmutant"
oca2Query = "SELECT * FROM oca2mutant"
tp53Query = "SELECT * FROM tp53mutant"
pahQuery = "SELECT  * FROM  pahmutant"

class Ui_Dialog(object):
    def __init__(self, name, surname, ID):
        self.name = name
        self.surname = surname
        self.ID = str(ID)

    def pushButtonHandlerMan(self):
        self.dialogBoxMan()

    def dialogBoxMan(self):
        remove_digits = str.maketrans('', '', digits)
        filePath = QFileDialog.getOpenFileName()
        path = filePath[0]
        a = open(path, "r").read().replace(" ", "").translate(remove_digits).replace("\n", "")

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
        self.hbbWoman = a[754024:755584]
        self.httWoman = a[1038246:1207506]
        self.tp53Woman = a[1490168:1509308]
        self.pahWoman = a[1791970:1913470]
        self.oca2Woman = a[1913470:2257870]

    def checkHealthStatus(self, hbb, cftr, oca, pah, htt, tp53, TC_ID):
            selectionQuery = "Select * FROM patients where id = 0"
            insertionHealthStatus = "UPDATE patients SET reshbb = %s, rescftr = %s, resoca2 = %s, respah = %s, reshtt = %s, resp53 = %s WHERE TC_ID = %s"

            cursor.execute(selectionQuery)
            HEALTHY_records = cursor.fetchall()

            for row in HEALTHY_records:
                HEALTHYhbb = row[1]
                HEALTHYcftr = row[2]
                HEALTHYoca = row[3]
                HEALTHYpah = row[4]
                HEALTHYhtt = row[5]
                HEALTHYtp53 = row[6]


            if HEALTHYhbb == hbb:
                hbbStatus = "healthy"
            else:
                hbbStatus = "Not Healthy"

            if HEALTHYcftr == cftr:
                cftrStatus = "healthy"
            else:
                cftrStatus = "Not Healthy"

            if HEALTHYoca == oca:
                oca2Status = "healthy"
            else:
                oca2Status = "Not Healthy"

            if HEALTHYpah == pah:
                pahStatus = "healthy"
            else:
                pahStatus = "Not Healthy"

            if HEALTHYhtt == htt:
                httStatus = "healthy"
            else:
                httStatus = "Not Healthy"

            if HEALTHYtp53 == tp53:
                tp53Status = "healthy"
            else:
                tp53Status = "Not Healthy"

            healthValues = (hbbStatus, cftrStatus, oca2Status, pahStatus, httStatus, tp53Status, TC_ID)
            cursor.execute(insertionHealthStatus, healthValues)
            connection.commit()

            self.checkMutantGensIfGenIsUnhealthy(hbb, cftr, oca, pah, htt, tp53, TC_ID)

    def checkMutantGensIfGenIsUnhealthy(self, hbb, cftr, oca, pah, htt, tp53, TC_ID):
        selectionQuery = "Select * FROM patients where TC_ID = %s"
        cursor.execute(selectionQuery, (TC_ID,))
        results = cursor.fetchall()

        for row in results:
            reshbb = row[7]
            rescftr = row[8]
            resoca2 = row[9]
            respah = row[10]
            reshtt = row[11]
            restp53 = row[12]


        if (restp53 == "Not Healthy"):
            cursor.execute(tp53Query)
            result = cursor.fetchall()
            for rows in result:
                TP53AGT_AGX = rows[1]
                TP53CGA_TGA = rows[2]
                TP53CGG_TGG = rows[3]
                TP53GAA_AAA = rows[4]
                TP53GAG_AAG = rows[5]
                TP53GAT_GAX = rows[6]
                TP53GCC_TGC = rows[7]
            if (TP53AGT_AGX == tp53):
                self.TP53Reason = "TP53AGT_AGX"
            elif (TP53CGA_TGA == tp53):
                self.TP53Reason = "TP53CGA_TGA"
            elif (TP53CGG_TGG == tp53):
                self.TP53Reason = "TP53CGG_TGG"
            elif (TP53GAA_AAA == tp53):
                self.TP53Reason = "TP53GAA_AAA"
            elif (TP53GAG_AAG == tp53):
                self.TP53Reason = "TP53GAG_AAG"
            elif (TP53GAT_GAX == tp53):
                self.TP53Reason = "TP53GAT_GAX"
            elif (TP53GCC_TGC == tp53):
                self.TP53Reason = "TP53GCC_TGC"
            qq = "UPDATE patients SET tp53Diseases = %s WHERE TC_ID = %s"
            val = (self.TP53Reason, TC_ID)
            cursor.execute(qq, val)
            connection.commit()

        if (respah == "Not Healthy"):
            cursor.execute(pahQuery)
            result = cursor.fetchall()
            for rows in result:
                PAH42AAA_GAA = rows[1]
                PAHATG_AGG = rows[2]
                PAHCAG_CAC = rows[3]
                PAHCGC_GGC = rows[4]
                PAHGAA_TAA = rows[5]
                PAHGCC_GAC = rows[6]
            if (PAH42AAA_GAA == pah):
                self.PAHReason = "PAH42AAA_GAA"
            elif (PAHATG_AGG == pah):
                self.PAHReason = "PAHATG_AGG"
            elif (PAHCAG_CAC == pah):
                self.PAHReason = "PAHCAG_CAC"
            elif (PAHCGC_GGC == pah):
                self.PAHReason = "PAHCGC_GGC"
            elif (PAHGAA_TAA == pah):
                self.PAHReason = "PAHGAA_TAA"
            elif (PAHGCC_GAC == pah):
                self.PAHReason = "PAHGCC_GAC"
            qq = "UPDATE patients SET pahDiseases = %s WHERE TC_ID = %s"
            val = (self.PAHReason, TC_ID)
            cursor.execute(qq, val)
            connection.commit()

        if (reshtt == "Not Healthy"):
            cursor.execute(httQuery)
            result = cursor.fetchall()
            for rows in result:
                htt40 = rows[1]
                htt65 = rows[2]
                htt120 = rows[3]
                httACG_ATG = rows[4]
                httCCG_CTG = rows[5]
            if (htt40 == htt):
                self.HTTReason = "htt40"
            elif (htt65 == htt):
                self.HTTReason = "htt65"
            elif (htt120 == htt):
                self.HTTReason = "htt120"
            elif (httACG_ATG == htt):
                self.HTTReason = "httACG_ATG"
            elif (httCCG_CTG == htt):
                self.HTTReason = "httCCG_CTG"
            qq = "UPDATE patients SET httDiseases = %s WHERE TC_ID = %s"
            val = (self.HTTReason, TC_ID)
            cursor.execute(qq, val)
            connection.commit()

        if (rescftr == "Not Healthy"):
            cursor.execute(cftrQuery)
            result = cursor.fetchall()
            for rows in result:
                cftr188 = rows[1]
                cftr1456 = rows[2]
                cftr1526 = rows[3]
                cftr1567 = rows[4]
                cftr1717 = rows[5]
                cftr220 = rows[6]
                cftr3808 = rows[7]
                cftr870 = rows[8]
                cftr3874 = rows[9]

            if (cftr188 == cftr):
                self.CFTRReason = "cftr188"
            elif (cftr1456 == cftr):
                self.CFTRReason = "cftr1456"
            elif (cftr1526 == cftr):
                self.CFTRReason = "cftr1526"
            elif (cftr1567 == cftr):
                self.CFTRReason = "cftr1567"
            elif (cftr1717 == cftr):
                self.CFTRReason = "cftr1717"
            elif (cftr220 == cftr):
                self.CFTRReason = "cftr220"
            elif (cftr3808 == cftr):
                self.CFTRReason = "cftr3808"
            elif (cftr870 == cftr):
                self.CFTRReason = "cftr870"
            elif (cftr3874 == cftr):
                self.CFTRReason = "cftr3874"
            qq = "UPDATE patients SET cftrDiseases = %s WHERE TC_ID = %s"
            val = (self.CFTRReason, TC_ID)
            cursor.execute(qq, val)
            connection.commit()

        if (resoca2 == "Not Healthy"):
            cursor.execute(oca2Query)
            result = cursor.fetchall()
            for rows in result:
                OCA2AGG_AGT = rows[0].replace("\n", "")
                OCA2CGG_TGG = rows[1].replace("\n", "")
                OCA2GGA_AGA = rows[2]
                OCA2GTG_TTG = rows[3].replace("\n", "")
                OCA2TGG_TAG = rows[4].replace("\n", "")
                OCA2TTT_TGT = rows[5].replace("\n", "")

            if (OCA2GGA_AGA == oca):
                self.OCA2Reason= "OCA2GGA_AGA"
            elif (OCA2AGG_AGT == oca):
                self.OCA2Reason= "OCA2AGG_AGT"
            elif (OCA2CGG_TGG == oca):
                self.OCA2Reason= "OCA2CGG_TGG"
            elif (OCA2GTG_TTG == oca):
                self.OCA2Reason= "OCA2GTG_TTG"
            elif (OCA2TGG_TAG == oca):
                self.OCA2Reason= "OCA2TGG_TAG"
            elif (OCA2TTT_TGT == oca):
                self.OCA2Reason=  "OCA2TTT_TGT"
            qq = "UPDATE patients SET oca2Diseases = %s WHERE TC_ID = %s"
            val = (self.OCA2Reason, TC_ID)
            cursor.execute(qq, val)
            connection.commit()

        if (reshbb == "Not Healthy"):
            cursor.execute(hbbQuery)
            result = cursor.fetchall()
            for rows in result:
                HBBATG_AAG = rows[1].replace("\n", "")
                HBBATG_ACG = rows[2].replace("\n", "")
                HBBATG_ATA = rows[3].replace("\n", "")
                HBBATG_ATC = rows[4].replace("\n", "")
                HBBGTG_ATG = rows[5].replace("\n", "")
                # DELTED ASK UGUR # HBBc328G = row[6]

            if (HBBATG_AAG == hbb):
                self.HBBReason= "HBBATG_AAG"
            elif (HBBATG_ACG == hbb):
                self.HBBReason= "HBBATG_ACG"
            elif (HBBATG_ATA == hbb):
                self.HBBReason= "HBBATG_ATA"
            elif (HBBATG_ATC == hbb):
                self.HBBReason= "HBBATG_ATC"
            elif (HBBGTG_ATG == hbb):
                self.HBBReason= "HBBGTG_ATG"
            qq = "UPDATE patients SET hbbDiseases = %s WHERE TC_ID = %s"
            val = (self.HBBReason, TC_ID)
            cursor.execute(qq, val)
            connection.commit()

    def saveDatabase(self):
        self.manID = self.patientIDMan.text()
        self.manName = self.fullNameMan.text()

        self.WomanID = self.patientIDWoman.text()
        self.WomanName = self.fullNameWoman.text()

        lastInsertedQuery = "Select * FROM patients order by id desc limit 1"

        query = "INSERT into patients(hbb, cftr, oca2, pah, htt, tp53, name, TC_ID, doctorID) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        valuesMan = (
        self.hbbMan, self.cftrMan, self.oca2Man, self.pahMan, self.httMan, self.tp53Man, self.manName, self.manID,
        self.ID)

        cursor.execute(query, valuesMan)
        connection.commit()

        cursor.execute(lastInsertedQuery)
        result = cursor.fetchall()
        for row in result:
            TC_ID = row[14]

        self.checkHealthStatus(self.hbbMan, self.cftrMan, self.oca2Man, self.pahMan, self.httMan, self.tp53Man, TC_ID)
        self.checkMutantGensIfGenIsUnhealthy(self.hbbMan, self.cftrMan, self.oca2Man, self.pahMan, self.httMan, self.tp53Man, TC_ID)

        valuesWoman = (self.hbbWoman, self.cftrWoman, self.oca2Woman, self.pahWoman, self.httWoman, self.tp53Woman, self.WomanName, self.WomanID, self.ID)
        cursor.execute(query, valuesWoman)
        connection.commit()

        cursor.execute(lastInsertedQuery)
        result = cursor.fetchall()
        for row in result:
            TC_ID = row[14]

        self.checkHealthStatus(self.hbbWoman, self.cftrWoman, self.oca2Woman, self.pahWoman, self.httWoman, self.tp53Woman, TC_ID)
        self.checkMutantGensIfGenIsUnhealthy(self.hbbWoman, self.cftrWoman, self.oca2Woman, self.pahWoman, self.httWoman, self.tp53Woman, TC_ID)

    def browse(self):
        filePath = QFileDialog.getOpenFileName(self, 'Single File',
                                               "C:/Users/ASUS/PycharmProjects/BrightBorn/myPackage/documents", '*.text')
        print('filePath ', filePath)
        fileHandle = open(filePath, 'r')
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

        self.fullNameMan = QtWidgets.QLineEdit(Dialog)
        self.fullNameMan.setGeometry(QtCore.QRect(280, 250, 104, 31))
        self.fullNameMan.setObjectName("textEdit_4")

        self.patientIDMan = QtWidgets.QLineEdit(Dialog)
        self.patientIDMan.setGeometry(QtCore.QRect(280, 310, 104, 31))
        self.patientIDMan.setObjectName("textEdit_5")

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

        self.fullNameWoman = QtWidgets.QLineEdit(Dialog)
        self.fullNameWoman.setGeometry(QtCore.QRect(510, 250, 104, 31))
        self.fullNameWoman.setObjectName("textEdit_6")

        self.patientIDWoman = QtWidgets.QLineEdit(Dialog)
        self.patientIDWoman.setGeometry(QtCore.QRect(510, 310, 104, 31))
        self.patientIDWoman.setObjectName("textEdit_7")

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
        self.submitData.clicked.connect(self.saveDatabase)

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
        self.fullNameMan.raise_()
        self.saveButtonMan.raise_()
        self.patientIDMan.raise_()
        self.fullNameWoman.raise_()
        self.patientIDWoman.raise_()
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
        self.doctorID.setHtml(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-size:10pt; color:#4f4f4f;\">Doctor ID: " + self.ID + "</span></p></body></html>"))
        self.doctorName.setHtml(_translate("Dialog",
                                           "<html><head/><body><p><span style=\" font-size:10pt; color:#4f4f4f;\">Name: " + self.name + "</span></p></body></html>"))
        self.doctorSurname.setHtml(_translate("Dialog",
                                              "<html><head/><body><p><span style=\" font-size:10pt; color:#4f4f4f;\">Surname: " + self.surname + "</span></p></body></html>"))
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
