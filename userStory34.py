
from datetime import datetime 
import time

file = open("My-Family_Sravanthi_KanchiSSW555.ged","r")


class Individual:
    'class for all individual'
    indilist=[]
    def __init__(self,uID):
        self.id=uID
        self.fName=""
        self.lName=""
        self.gender=""
        self.date_of_birth=[]
        self.married="false"
        self.alive="true"
        self.date_of_death=[]
        self.famc=[]
        self.fams=[]


class Family:
    'class for all family'
    famlist=[]
    def __init__(self,uID):
        self.id=uID
        self.husband=""
        self.wife=""
        self.date_of_marriage=[]
        self.state="married"
        self.date_of_divorce=[]
        self.children=[]
	

    def addchild(self,uID):
        i=100
        if len(uID)==5:
            i=int(uID[2])
        if len(uID)==6:
            i=int(uID[2]+uID[3])
        p=Individual.indilist[i-1]
        f=self
        self.children.append(p)
        p.addfamc(f)
		
    def divorce(self, d,m,y):
        self.state="divorce"
        self.date_of_divorce=changetonum([d,m,y])
        self.husband.divorce()
        self.wife.divorce()
        
    def setwife(self,uID):
        i=100
        if len(uID)==5:
            i=int(uID[2])
        if len(uID)==6:
            i=int(uID[2]+uID[3])
        p=Individual.indilist[i-1]
        f=self
        self.wife=p
        p.addfams(f)
    
    def sethusband(self,uID):
        i=100
        if len(uID)==5:
            i=int(uID[2])
        if len(uID)==6:
            i=int(uID[2]+uID[3])
        p=Individual.indilist[i-1]
        f=self
        self.husband=p
        p.addfams(f)
    
    def setdom(self,d,m,y):
        self.date_of_marriage=changetonum([d,m,y])
    


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

#get age by date of birth
def getage(dob):
    t=time.strftime('%d %m %Y',time.localtime(time.time()))
    t=t.split(' ')
    if int(t[1])>dob[1]:
        return int(t[2])-dob[2]
    if int(t[1])==dob[1]:
        if int(t[0])>=dob[0]:
            return (int(t[2])-dob[2])
        else:
            return (int(t[2])-dob[2]-1)
    if int(t[1])<int(dob[1]):
        return (int(t[2])-dob[2]-1)
        

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


def large_difference_couple():
    ans = []
    for i in range(len(Family.famlist)):
        ft=Family.famlist[i]
        a=getage(ft.husband.date_of_birth)/getage(ft.wife.date_of_birth)
        if a>=2 or a<=0.5:
            ans.append(ft)
    return ans


##def listLivingSingle(list_indi):
##    single = []
##    for i in list_indi:
##        if(i[4] == 0 and i[5] == []):
##            single.append(i[0])
##    print("User Story 31: List of Individuals living single : ", single)
##    for k in single:
##        print(k + ": " + getNameByID(list_indi, k))
##    print()




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

#listLivingSingle(list_indi)



r =large_difference_couple()
for i in range(len(r)):
    f=r[i]
    print('User Story 34:Family with unique id:'+f.id+' has a large age difference')
    print('User Story 34:Family with unique id:'+f.id+' has a large age difference')













