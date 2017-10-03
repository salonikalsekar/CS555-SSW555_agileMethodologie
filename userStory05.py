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

def getDeathDate(list_indi, id):
    for i in list_indi:
        if(i[0] == id):
            if(i[4] != 0):
                return i[4]

def parseTheFile(fileName):
    f = open(fileName,'r')
    indiOn = 0
    famOn = 0
    indi = indiList()
    fam = famList()
    list_indi = []
    list_fam = []
  
    for line in f:
        str = line.split()
        if(str != []):
            if(str[0] == '0'):
                if(indiOn == 1):
                    list_indi.append(indi)
                    indi = indiList()
                    indiOn = 0
                if(famOn == 1):
                    list_fam.append(fam)
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
                if(str[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = str[1]
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
    return list_indi, list_fam

def MarriageBeforeDeath(list_fam, list_indi):
    marrBeforeDeath_list = []
    for i in list_fam:
        if(getDeathDate(list_indi, i[1]) != None):
            if(i[3] > getDeathDate(list_indi, i[1])):
                marrBeforeDeath_list.append(i[0])
                print("The family " + i[0] + " have marriage dates after the death dates of " + i[1])
        if(getDeathDate(list_indi, i[2]) != None):
            if(i[3] > getDeathDate(list_indi, i[2])):
                marrBeforeDeath_list.append(i[0])
                print("The family " + i[0] + " have marriage dates after the death dates of " + i[2])
    if(len(marrBeforeDeath_list) == 0):
        print("There are no families having their marriage dates before the death dates of their husband/wife.")
    else:
        print("The families with marriage dates after the death date:")
        print(marrBeforeDeath_list)

def main(fileName):
    list_indi, list_fam = parseTheFile(fileName)
    list_indi.sort()
    list_fam.sort()
    MarriageBeforeDeath(list_fam, list_indi)
main('C:/Users/Lenovo/Desktop/Homewrk_4_Achal/Achal Project01.ged')

