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

def getSpouseNameById(listFam, famId, spouseId):
    for i in listFam:
        if(i[0] == famId):
            if(i[1] == spouseId):
                return i[2]
            if(i[2] == spouseId):
                return i[1]

def getDivorceDateById(listFam, famId):
    for i in listFam:
        if(i[0] == famId):
            if(i[4] != 0):
                return i[4]           
def noBigamy(listIndi, listFam):
    noBigamyList = []
    for i in listIndi:
        family = []
        t = []
        if(len(i[5]) > 1):
            selfId = i[0]
            for j in i[5]:
                t.append(getMarriageDateById(listFam, j))
                t.append(j)
                t.append(getSpouseNameById(listFam, j, selfId))
                t.append(getDivorceDateById(listFam, j))
                t.append(getDeathDateById(listIndi, getSpouseNameById(listFam, j, selfId)))
                family.append(t)
                t = []
            family.sort()
            for z in range(1, len(family)):
                if(family[z-1][3] == None and family[z-1][4] == None):
                    noBigamyList.append(selfId)
                    print("User story 11: The person with id " + selfId + " is married to the person " + family[z][2] + " with family id " + family[z][1] + " while the person is still married to person with id " + family[z-1][2] + " in family " + family[z-1][1])
                else:
                    if(family[z-1][3] != None):
                        if(family[z][0] < family[z-1][3]):
                            noBigamyList.append(selfId)
                            print("User story 11: The person with id " + selfId + " is married to the person " + family[z][2] + " with family id " + family[z][1] + " before the person filed divorce with spouse " + family[z-1][2] + " in family " + family[z-1][1])
                    if(family[z-1][4] != None):
                        if(family[z][0] < family[z-1][4]):
                            noBigamyList.append(selfId)
                            print("User story 11: The person with id " + selfId + " is married to the person " + family[z][2] + " with family id  " + family[z][1] + " before his/her spouse's death" + family[z-1][2] + " in family " + family[z-1][1])
    if(len(noBigamyList) == 0):
        print("User story 11: The individual in the given gedcom file is not involved in Bigamy.")
    else:
        print("User story 11: The individuals who are involved in Bigamy are as follows: ")
        print(noBigamyList)

def getMarriageDateById(listFam, id):
    for i in listFam:
        if(i[0] == id):
            return i[3]

def getDeathDateById(listIndi, indiId):
    for i in listIndi:
        if(i[0] == indiId):
            if(i[4] != 0):
                return i[4]

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
    noBigamy(listIndi, listFam)

main('C:/Users/Lenovo/Desktop/Homewrk_4_Achal/Achal Project01.ged')
