import mysql.connector
from mysql.connector import Error
from string import digits
import difflib
from difflib import SequenceMatcher
import numpy as np
import itertools



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
'''
remove_digits = str.maketrans('', '', digits)
patientCFTR = open("CFTR.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientHBB = open("HBB.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientHTT = open("HTT.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientOCA = open("OCA2.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientTP53 = open("TP53.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
patientPAH = open("PAH.txt").read().replace(" ", "").translate(remove_digits).replace("\n", "")
'''
'''
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


    if (tp53 == "Not Healthy"):
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
        if(TP53AGT_AGX == patientTP53):
            print("TP53AGT_AGX")
        elif(TP53CGA_TGA == patientTP53):
            print("TP53CGA_TGA")
        elif (TP53CGG_TGG == patientTP53):
            print("TP53CGG_TGG")
        elif (TP53GAA_AAA == patientTP53):
            print("TP53GAA_AAA")
        elif (TP53GAG_AAG == patientTP53):
            print("TP53GAG_AAG")
        elif (TP53GAT_GAX == patientTP53):
            print("TP53GAT_GAX")
        elif (TP53GCC_TGC == patientTP53):
            print("TP53GCC_TGC")

    if(pah == "Not Healthy"):
        cursor.execute(pahQuery)
        result = cursor.fetchall()
        for rows in result:
            PAH42AAA_GAA = rows[1]
            PAHATG_AGG = rows[2]
            PAHCAG_CAC = rows[3]
            PAHCGC_GGC = rows[4]
            PAHGAA_TAA = rows[5]
            PAHGCC_GAC = rows[6]
        if(PAH42AAA_GAA == patientPAH):
            print("PAH42AAA_GAA")
        elif(PAHATG_AGG == patientPAH):
            print("PAHATG_AGG")
        elif (PAHCAG_CAC == patientPAH):
            print("PAHCAG_CAC")
        elif (PAHCGC_GGC == patientPAH):
            print("PAHCGC_GGC")
        elif (PAHGAA_TAA == patientPAH):
            print("PAHGAA_TAA")
        elif (PAHGCC_GAC == patientPAH):
            print("PAHGCC_GAC")


    if(htt == "Not Healthy"):
        cursor.execute(httQuery)
        result = cursor.fetchall()
        for rows in result:
            htt40 = rows[1]
            htt65 = rows[2]
            htt120 = rows[3]
            httACG_ATG = rows[4]
            httCCG_CTG = rows[5]
        if(htt40 == patientHTT):
            print("htt40")
        elif(htt65 == patientHTT):
            print("htt65")
        elif (htt120 == patientHTT):
            print("htt120")
        elif (httACG_ATG == patientHTT):
            print("httACG_ATG")
        elif (httCCG_CTG == patientHTT):
            print("httCCG_CTG")


    if(cftr == "Not Healthy"):
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

        if(cftr188 == patientCFTR):
            print("cftr188")
        elif(cftr1456 == patientCFTR):
            print("cftr1456")
        elif (cftr1526 == patientCFTR):
            print("cftr1526")
        elif (cftr1567 == patientCFTR):
            print("cftr1567")
        elif (cftr1717 == patientCFTR):
            print("cftr1717")
        elif (cftr220 == patientCFTR):
            print("cftr220")
        elif (cftr3808 == patientCFTR):
            print("cftr3808")
        elif (cftr870 == patientCFTR):
            print("cftr870")
        elif (cftr3874 == patientCFTR):
            print("cftr3874")


    if(oca2 == "Not Healthy"):
        cursor.execute(oca2Query)
        result = cursor.fetchall()
        for rows in result:
            OCA2AGG_AGT = rows[0].replace("\n", "")
            OCA2CGG_TGG = rows[1].replace("\n", "")
            OCA2GGA_AGA = rows[2]
            OCA2GTG_TTG = rows[3].replace("\n", "")
            OCA2TGG_TAG = rows[4].replace("\n", "")
            OCA2TTT_TGT = rows[5].replace("\n", "")

        if(OCA2GGA_AGA == patientOCA):
            print("OCA2GGA_AGA")
        elif(OCA2AGG_AGT == patientOCA):
            print("OCA2AGG_AGT")
        elif(OCA2CGG_TGG == patientOCA):
            print("OCA2CGG_TGG")
        elif(OCA2GTG_TTG == patientOCA):
            print("OCA2GTG_TTG")
        elif(OCA2TGG_TAG == patientOCA):
            print("OCA2TGG_TAG")
        elif(OCA2TTT_TGT == patientOCA):
             print("OCA2TGG_TAG")


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
        if(HBBATG_AAG == patientHBB):
            print("HBBATG_AAG")
        elif(HBBATG_ACG == patientHBB):
            print("HBBATG_ACG")
        elif (HBBATG_ATA == patientHBB):
            print("HBBATG_ATA")
        elif (HBBATG_ATC == patientHBB):
            print("HBBATG_ATC")
        elif (HBBGTG_ATG == patientHBB):
            print("HBBGTG_ATG")
        else:
            print("HBB CLEAR!")


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

#take_Patient_Set_PatientGen_And_Compare_Gens_Then_Set_Healthy_Status(1)
'''


def xstr(s):
    if s is None:
        return " "
    return str(s)


q = "Select * FROM patients where TC_ID = %s"
q2 = "Select * FROM patients where TC_ID = %s"
qv = 1234
q2v = 1232

cursor.execute(q, (qv,))
res1 = cursor.fetchall()


cursor.execute(q2, (q2v,))
res2 = cursor.fetchall()

for row in res1:
    hbbM = row[7]
    cftrM = row[8]
    oca2M = row[9]
    pahM = row[10]
    httM = row[11]
    tp53M = row[12]

for row in res2:
    hbbW = row[7]
    cftrW = row[8]
    oca2W = row[9]
    pahW = row[10]
    httW = row[11]
    tp53W = row[12]

selectionQuery = "Select * FROM patients where TC_ID = %s"
cursor.execute(selectionQuery, (qv,))
results = cursor.fetchall()


for row in results:
    hbbDiseaseMAN = row[17]
    cftrDiseaseMAN = row[19]
    ocaDisease2MAN = row[20]
    pahDiseaseMAN = row[18]
    httDiseaseMAN = row[21]
    tp53DiseaseMAN = row[22]

    hbbDiseaseMAN = xstr(hbbDiseaseMAN)
    cftrDiseaseMAN = xstr(cftrDiseaseMAN)
    ocaDisease2MAN = xstr(ocaDisease2MAN)
    pahDiseaseMAN = xstr(pahDiseaseMAN)
    httDiseaseMAN = xstr(httDiseaseMAN)
    tp53DiseaseMAN = xstr(tp53DiseaseMAN)

    hbbMAN = row[1]
    cftrMAN = row[2]
    oca2MAN = row[3]
    pahMAN = row[4]
    httMAN = row[5]
    tp53MAN = row[6]

    TC_IDMan = row[14]
selectionQuery = "Select * FROM patients where TC_ID = %s"
cursor.execute(selectionQuery, (q2v,))
results = cursor.fetchall()

for row in results:
    hbbDiseaseWOMAN = row[17]
    cftrDiseaseWOMAN = row[19]
    oca2DiseaseWOMAN = row[20]
    pahDiseaseWOMAN = row[18]
    httDiseaseWOMAN = row[21]
    tp53DiseaseWOMAN = row[22]

    hbbDiseaseWOMAN = xstr(hbbDiseaseWOMAN)
    cftrDiseaseWOMAN = xstr(cftrDiseaseWOMAN)
    oca2DiseaseWOMAN = xstr(oca2DiseaseWOMAN)
    pahDiseaseWOMAN = xstr(pahDiseaseWOMAN)
    httDiseaseWOMAN = xstr(httDiseaseWOMAN)
    tp53DiseaseWOMAN = xstr(tp53DiseaseWOMAN)

    hbbWOMAN = row[1]
    cftrWOMAN = row[2]
    oca2WOMAN = row[3]
    pahWOMAN = row[4]
    httWOMAN = row[5]
    tp53WOMAN = row[6]
    TC_IDWoman = row[14]

linkeagedGenNumber = 3
tempPaternalList = ["AM", "BW", "CM"]
tempMaternalList = ["AW", "BM", "CM"]
exListOffSpring=[]


def combine(paternal, maternal, current):
    tempList = []
    if (isinstance(current, str)):
        tempList = [current + paternal, current + maternal]
    elif (isinstance(current, type([]))):
        length = len(current)

        for i in range(0, length):
            tempList.append(current[i] + paternal)
            tempList.append(current[i] + maternal)
    return tempList



exListOffSpring=combine(tempPaternalList[0], tempMaternalList[0], "")
for i in range(1, linkeagedGenNumber):
    exListOffSpring=combine(tempPaternalList[i], tempMaternalList[i], exListOffSpring)


print(exListOffSpring)
