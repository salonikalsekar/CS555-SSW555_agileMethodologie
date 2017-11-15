from collections import OrderedDict
from operator import itemgetter
import datetime 

file = open("My-Family_Sravanthi_KanchiSSW555.ged","r")

date_format = "%d %b %Y"


def orderSiblingsByAge(list_indi, list_fam):
    child = {}
    print("\n\nUser Story 28 : Order Siblings by Age\n")
    for fam in list_fam:
        child.clear()
        for i in range(len(fam)):
            famid = fam[0]
            if (fam[i] for i in list_fam) == "CHIL":
                id = fam[i][5:]
                for ind in list_indi:
                    if ind[0] == id:
                        my_date = ind[3][10:].strip()
                        birthDate = datetime.datetime.strptime(my_date,'%Y-%m-%d')
                        Today = datetime.datetime.today()
                        age = (Today - birthDate).days/365
                        if age < 0:
                            child.setdefault(ind[1][5:], []).append("Invalid")
                        else:
                            child.setdefault(ind[1][5:], []).append(age)
        print(famid + "\n")
        sortedChildren = OrderedDict(sorted(child.items(), key = itemgetter(1)))
        for key,value in sortedChildren.items():
            print(str(key) + " , Age : " + str(value) + "\n")
        sortedChildren.clear()



def converttoDate(date):
    n = date.split()
    if(n[1] == 'JAN'): n[1] = '01';
    if(n[1] == 'FEB'): n[1] = '02';
    if(n[1] == 'MAR'): n[1] = '03';
    if(n[1] == 'APR'): n[1] = '04';
    if(n[1] == 'MAY'): n[1] = '05';
    if(n[1] == 'JUN'): n[1] = '06';
    if(n[1] == 'JUL'): n[1] = '07';
    if(n[1] == 'AUG'): n[1] = '08';
    if(n[1] == 'SEP'): n[1] = '09';
    if(n[1] == 'OCT'): n[1] = '10';
    if(n[1] == 'NOV'): n[1] = '11';
    if(n[1] == 'DEC'): n[1] = '12';
    if(n[2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        n[2] = '0' + n[2]
    return (n[0] + '-' + n[1] + '-' + n[2])

        

def getAgeByID(ind_list, id):
    d_flag = 0
    for i in ind_list:
        if(i[0] == id):
            b_date = i[3]
            m = b_date.split('-')
            b_year = int(m[0])
            b_month = int(m[1])
            b_date = int(m[2])
            if(i[4] != 0):
                d_date = i[4]
                d_flag = 1
    if(d_flag == 1):
        m = d_date.split('-')
        d_year = int(m[0])
        d_month = int(m[1])
        d_date = int(m[2])
        return d_year - b_year - ((d_month, d_date) < (b_month, b_date))
    c_date = getCurrDate().split('-')
    c_year = int(c_date[0])
    c_month = int(c_date[1])
    c_date = int(c_date[2])
    return c_year - b_year - ((c_month, c_date) < (b_month, b_date))





def listLivingSingle(list_indi):
    single = []
    for i in list_indi:
        if(i[4] == 0 and i[5] == []):
            single.append(i[0])
    print("User Story 31: List of Individuals living single : ", single)
    for k in single:
        print(k + ": " + getNameByID(list_indi, k))
    print()




def getNameByID(list_indi, id):
    for i in list_indi:
        if(i[0] == id):
            return i[1]

def getCurrDate():
    c_date = str(datetime.date.today())
    return c_date

    return op_list

def fam_list():
    o_list = [0 for i in range(6)]
    o_list[5] = []
    return o_list

def ind_list():
    o_list = [0 for i in range(7)]
    o_list[5] = []
    return o_list

def getLastName(s):
    t=''
    for i in s:
        if(i != '/'):
            t += i
    return t


        


def parse(file):
    indi_flag = 0
    fam_flag = 0
    list_indi = []
    list_fam = []
    indi = ind_list()
    fam = fam_list()
    for line in file:
        str = line.split()
        if(str != []):
            if(str[0] == '0'):
                if(indi_flag == 1):
                    list_indi.append(indi)
                    indi = ind_list()
                    indi_flag = 0
                if(fam_flag == 1):
                    list_fam.append(fam)
                    fam = fam_list()
                    fam_flag = 0
                if(str[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(str[2] == 'INDI'):
                        indi_flag = 1
                        indi[0] = (str[1])
                    if(str[2] == 'FAM'):
                        fam_flag = 1
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
                        indi[3] = converttoDate(date)
                    if(date_id == 'DEAT'):
                        indi[4] = converttoDate(date)
                    if(date_id == 'MARR'):
                        fam[3] = converttoDate(date)
                    if(date_id == 'DIV'):
                        fam[4] = converttoDate(date)
    return list_indi, list_fam


list_indi, list_fam = parse(file)

# listLivingSingle(list_indi)


orderSiblingsByAge(list_indi, list_fam)
































