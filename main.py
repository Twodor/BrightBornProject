import mysql.connector
from mysql.connector import Error
from string import digits
import difflib
from difflib import SequenceMatcher
import numpy as np

connection = mysql.connector.connect(host='localhost',
                                     database='se315',
                                     user='root',
                                     password='')

db_Info = connection.get_server_info()
cursor = connection.cursor()
"""

# Deleting digits
remove_digits = str.maketrans('', '', digits)
cftr = open("cftr.txt", "r").read().replace(" ", "").translate(remove_digits)
hbb = open("hbb.txt", "r").read().replace(" ", "").translate(remove_digits)
htt = open("htt.txt", "r").read().replace(" ", "").translate(remove_digits)
oca2 = open("oca2.txt", "r").read().replace(" ", "").translate(remove_digits)
pah = open("pah.txt", "r").read().replace(" ", "").translate(remove_digits)
tp53 = open("tp53.txt", "r").read().replace(" ", "").translate(remove_digits)
query2 = "INSERT INTO patients(hbb, cftr, oca2, pah, htt, tp53) values(%s, %s, %s, %s, %s, %s)"
values2= (hbb, cftr, oca2, pah, htt, tp53)
cursor.execute(query2, values2)
connection.commit()
#patient1 = open("Patient_1[CFTR_1567-TP53_180].txt", "r").read().replace(" ", "").translate(remove_digits)
#patient2 = open("Patient_1[CFTR_1567-TP53_180].txt", "r").read()


patien1CFTR = open("patient1/CFTR_Mutant_1567G-T.txt").read().replace(" ", "").translate(remove_digits)
patien1HBB = open("patient1/HBB_Healty.txt").read().replace(" ", "").translate(remove_digits)
patien1HTT = open("patient1/HTT_Healty.txt").read().replace(" ", "").translate(remove_digits)
patien1OCA2 = open("patient1/OCA2_Healty.txt").read().replace(" ", "").translate(remove_digits)
patien1PAH = open("patient1/PAH_Healty.txt").read().replace(" ", "").translate(remove_digits)
patien1TP53 = open("patient1/TP53_Mutant_180_GAG-AAG.txt").read().replace(" ", "").translate(remove_digits)
patientName = "patient1"
query = "INSERT INTO patients(hbb, cftr, oca2, pah, htt, tp53, name) values(%s, %s, %s, %s, %s, %s, %s)"
values= (patien1HBB, patien1CFTR, patien1OCA2, patien1PAH, patien1HTT, patien1TP53, patientName)
cursor.execute(query, values)
connection.commit()
"""

"""

remove_digits = str.maketrans('', '', digits)
tp53 = open("TP53.txt").read().replace(" ", "").translate(remove_digits)
"""

"""
##### PATIENT 0 ####


remove_digits = str.maketrans('', '', digits)
patientCFTR = open("CFTR.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientHBB= open("HBB.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientHTT = open("HTT.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientOCA2 = open("OCA2.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientTP53 = open("TP53.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientPAH = open("PAH.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientValues = (patientHBB, patientCFTR, patientOCA2, patientPAH, patientHTT, patientTP53)


insertionQuery = "INSERT INTO patients(hbb, cftr, oca2, pah, htt, tp53) values(%s, %s, %s, %s, %s, %s)"
patientValues = (patientHBB, patientCFTR, patientOCA2, patientPAH, patientHTT, patientTP53)
cursor.execute(insertionQuery, patientValues)
connection.commit()
"""

"""
selectionQuery = "Select * FROM patients where id = 0"
patientQuery = "Select * FROM patients where id = 21"

cursor.execute(selectionQuery)
HEALTHY_records = cursor.fetchall()

for row in HEALTHY_records:
    HEALTHYhbb = row[1]
    HEALTHYcftr = row[2]
    HEALTHYoca2 = row[3]
    HEALTHYpah = row[4]
    HEALTHYhtt = row[5]
    HEALTHYtp53 = row[6]

cursor.execute(patientQuery)
PATIENT_records = cursor.fetchall()

for row in PATIENT_records:
    PATIENT_hbb = row[1]
    PATIENT_cftr = row[2]
    PATIENT_oca2 = row[3]
    PATIENT_pah = row[4]
    PATIENT_htt = row[5]
    PATIENT_tp53 = row[6]




statusVALUES = (hbbStatus, cftrStatus, oca2Status, pahStatus, httStatus, tp53Status)
cursor.execute(insertionHealthStatus, statusVALUES)
connection.commit()
"""

"""
intSilme = open("intSilme.txt", "r").read().replace(" ", "").translate(remove_digits)

query = "Select * from patients where id = 0"
cursor.execute(query)
records = cursor.fetchall()
for row in records:
    denemeHBB = row[1]
if(hbb == denemeHBB):
    print("Oldu BEBEĞİM")
"""

'''
query = """INSERT INTO patients(
hbb,
cftr,
oca2,
pah,
htt,
tp53) 
VALUES(%s, %s, %s, %s, %s, %s) """

recordTuple = (hbb, cftr, oca2, pah, htt, tp53)
cursor.execute(query, recordTuple)
connection.commit()
'''

hbbQuery = "SELECT  * FROM hbbmutant"
cftrQuery = "SELECT * FROM cftrmutant"
httQuery = "SELECT  * FROM httmutant"
oca2Query = "SELECT * FROM oca2mutant"
tp53Query = "SELECT * FROM tp53mutant"
pahQuery = "SELECT  * FROM  pahmutant"

remove_digits = str.maketrans('', '', digits)
patientCFTR = open("CFTR.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientHBB = open("HBB.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientHTT = open("HTT.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientOCA = open("OCA2.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientTP53 = open("TP53.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientPAH = open("PAH.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")

def checkMutantGensIfGenIsUnhealthy(patientID):
    selectionQuery = "Select * FROM patients where TC_ID = %s"
    cursor.execute(selectionQuery, (patientID,))
    results = cursor.fetchall()

    for  row in results:
        hbb = row[7]
        cftr = row[8]
        oca2 = row[9]
        pah = row[10]
        htt = row[11]
        tp53 = row[12]
        name = row[13]

    if(oca2 == "Not Healthy"):
        cursor.execute(oca2Query)
        result = cursor.fetchall()
        for rows in result:
            OCA2AGG_AGT = row[1]
            OCA2CGG_TGG = row[2]
            OCA2GGA_AGA = row[3]
            OCA2GTG_TTG = row[4]
            OCA2TGG_TAG = row[5]
            OCA2TTT_TGT = row[6]
    if(OCA2GGA_AGA == patientOCA):
        print("Hastalık: OCA2GGA_AGA")
    if(hbb == "Not Healthy"):
        cursor.execute(hbbQuery)
        result = cursor.fetchall()
        for rows in result:
            HBBATG_AAG = rows[1].replace("\n", "")
            HBBATG_ACG = rows[2].replace("\n", "")
            HBBATG_ATA = rows[3].replace("\n", "")
            HBBATG_ATC = rows[4].replace("\n", "")
            HBBGTG_ATG = rows[5].replace("\n", "")
            # DELTED ASK UGUR # HBBc328G = row[6]

def take_Patient_Set_PatientGen_And_Compare_Gens_Then_Set_Healthy_Status(patientID):
    selectionQuery = "Select * FROM patients where id = 0"
    insertionQuery = "INSERT INTO patients(hbb, cftr, oca2, pah, htt, tp53, name, TC_ID) values(%s, %s, %s, %s, %s, %s, %s, %s)"
    insertionHealthStatus = "UPDATE patients SET reshbb = %s, rescftr = %s, resoca2 = %s, respah = %s, reshtt = %s, resp53 = %s WHERE TC_ID = %s"

    cursor.execute(selectionQuery)
    HEALTHY_records = cursor.fetchall()
    patientName = "patientName"
    for row in HEALTHY_records:
        HEALTHYhbb = row[1]
        HEALTHYcftr = row[2]
        HEALTHYoca = row[3]
        HEALTHYpah = row[4]
        HEALTHYhtt = row[5]
        HEALTHYtp53 = row[6]


    patientValues = (patientHBB, patientCFTR, patientOCA, patientPAH, patientHTT, patientTP53, patientName, patientID)


    cursor.execute(insertionQuery, patientValues)
    connection.commit()

    if HEALTHYhbb == patientHBB:
        hbbStatus = "healthy"
    else:
        hbbStatus = "Not Healthy"

    if HEALTHYcftr == patientCFTR:
        cftrStatus = "healthy"
    else:
        cftrStatus = "Not Healthy"

    if HEALTHYoca == patientOCA:
        oca2Status = "healthy"
    else:
        oca2Status = "Not Healthy"

    if HEALTHYpah == patientPAH:
        pahStatus = "healthy"
    else:
        pahStatus = "Not Healthy"

    if HEALTHYhtt == patientHTT:
        httStatus = "healthy"
    else:
        httStatus = "Not Healthy"

    if HEALTHYtp53 == patientTP53:
        tp53Status = "healthy"
    else:
        tp53Status = "Not Healthy"

    healthValues = (hbbStatus, cftrStatus, oca2Status, pahStatus, httStatus, tp53Status, patientID)
    cursor.execute(insertionHealthStatus, healthValues)
    connection.commit()

    checkMutantGensIfGenIsUnhealthy(patientID)

take_Patient_Set_PatientGen_And_Compare_Gens_Then_Set_Healthy_Status(6)
