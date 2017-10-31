import datetime
def getLastName(str):
    tem=''
    for i in str:
        if(i != '/'):
            tem += i
    return tem

def famList():
    p_list = [0 for i in range(6)]
    p_list[5] = []
    return p_list

def indiList():
    p_list = [0 for i in range(7)]
    p_list[5] = []
    return p_list

def DateFormat(date):
    t = date.split()
    if(t[1] == 'JAN'): t[1] = '01';
    if(t[1] == 'FEB'): t[1] = '02';
    if(t[1] == 'MAR'): t[1] = '03';
    if(t[1] == 'APR'): t[1] = '04';
    if(t[1] == 'MAY'): t[1] = '05';
    if(t[1] == 'JUN'): t[1] = '06';
    if(t[1] == 'JUL'): t[1] = '07';
    if(t[1] == 'AUG'): t[1] = '08';
    if(t[1] == 'SEP'): t[1] = '09';
    if(t[1] == 'OCT'): t[1] = '10';
    if(t[1] == 'NOV'): t[1] = '11';
    if(t[1] == 'DEC'): t[1] = '12';
    if(t[2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        t[2] = '0' + t[2]
    return (t[0] + '-' + t[1] + '-' + t[2])

def uniqueId(listIndi, listFam):
    individualIdList = []
    familyIdList = []
    individualDuplicateIdList = []
    familyDuplicateList = []
    f = 0
    for i in listIndi:
        individualIdList.append(i[0])
    for i in listFam:
        familyIdList.append(i[0])
    if(len(individualIdList) != len(set(individualIdList)) and len(familyIdList) != len(set(familyIdList))):
        for i in individualIdList:
            f = 0
            for j in individualIdList:
                if (i == j):
                    f += 1
                    if(f > 1):
                        individualDuplicateIdList.append(i)
        for i in familyIdList:
            f = 0
            for j in familyIdList:
                if (i == j):
                    f += 1
                    if(f > 1):
                        familyDuplicateList.append(i)
        if(len(individualDuplicateIdList) != 0):
            print("User story 22: The following individuals have duplicate id's: ")
            print(set(individualDuplicateIdList))
        if(len(familyDuplicateList) != 0):
            print("User story 22: The following families have duplicate id's: ")
            print(set(familyDuplicateList))            
    else:
        print("User story 22: The IDs in the list are unique.")

def parseTheFile(fileName):
    f = open(fileName,'r')
    indiOn = 0
    famOn = 0
    indi = indiList()
    fam = famList()
    listIndi = []
    listFam = []  
    for line in f:
        str = line.split()
        if(str != []):
            if(str[0] == '0'):
                if(indiOn == 1):
                    listIndi.append(indi)
                    indi = indiList()
                    indiOn = 0
                if(famOn == 1):
                    listFam.append(fam)
                    fam = famList()
                    famOn = 0
                if(str[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(str[2] == 'INDI'):
                        indiOn = 1
                        indi[0] = (str[1])
                    if(str[2] == 'FAM'):
                        famOn = 1
                        fam[0] = (str[1])
            if(str[0] == '1'):
                if(str[1] == 'NAME'):
                    indi[1] = str[2] + " " + getLastName(str[3])
                if(str[1] == 'SEX'):
                    indi[2] = str[2]
                if(str[1] == 'FAMS'):
                    indi[5].append(str[2])
                if(str[1] == 'FAMC'):
                    indi[6] = str[2]
                if(str[1] == 'HUSB'):
                    fam[1] = str[2]
                if(str[1] == 'WIFE'):
                    fam[2] = str[2]
                if(str[1] == 'CHIL'):
                    fam[5].append(str[2])
                if(str[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = str[1]
            if(str[0] == '2'):
                if(str[1] == 'DATE'):
                    date = str[4] + " " + str[3] + " " + str[2]
                    if(date_id == 'BIRT'):
                        indi[3] = DateFormat(date)
                    if(date_id == 'DEAT'):
                        indi[4] = DateFormat(date)
                    if(date_id == 'MARR'):
                        fam[3] = DateFormat(date)
                    if(date_id == 'DIV'):
                        fam[4] = DateFormat(date)
    return listIndi, listFam

def main(fileName):
    listIndi, listFam = parseTheFile(fileName)
    listIndi.sort()
    listFam.sort()
    uniqueId(listIndi, listFam)

main('C:/Users/Lenovo/Desktop/Homewrk_4_Achal/Achal Project01.ged')

