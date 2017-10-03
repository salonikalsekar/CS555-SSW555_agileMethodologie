import datetime

def individualList():
    output_list = [0 for i in range(7)]
    output_list[5] = []
    return output_list
def getLastName(str):
    temp_var=''
    for i in str:
        if(i != '/'):
            temp_var += i
    return temp_var
def familyList():
    output_list = [0 for i in range(6)]
    output_list[5] = []
    return output_list

def marriageBeforeDivorce(list_family):
    marrBeforeDiv_List = []
    if(len(marrBeforeDiv_List) == 0):
        print("For user story 4, all the families have their marriage dates before their divorce dates.")
    else:
        print("For user story 4, below are the family/families who have their marriage dates occuring after their divorce dates: ")
        print(marrBeforeDiv_List)    
    for i in list_family:
        if(i[4] != 0):
            if(i[3] > i[4]):
                marrBeforeDiv_List.append(i[0])
                print("For user story 4, the family with name " + i[0] + " has their marriage date after the Divorce date.")
    
def dateFormatConversion(date):
    m = date.split()
    if(m[1] == 'JAN'): m[1] = '01';
    if(m[1] == 'FEB'): m[1] = '02';
    if(m[1] == 'MAR'): m[1] = '03';
    if(m[1] == 'APR'): m[1] = '04';
    if(m[1] == 'MAY'): m[1] = '05';
    if(m[1] == 'JUN'): m[1] = '06';
    if(m[1] == 'JUL'): m[1] = '07';
    if(m[1] == 'AUG'): m[1] = '08';
    if(m[1] == 'SEP'): m[1] = '09';
    if(m[1] == 'OCT'): m[1] = '10';
    if(m[1] == 'NOV'): m[1] = '11';
    if(m[1] == 'DEC'): m[1] = '12';
    if(m[2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        m[2] = '0' + m[2]
    return (m[0] + '-' + m[1] + '-' + m[2])

def toParse(gedFileName):
    f = open(gedFileName,'r')
    list_individual = []
    list_family = []
    indi_on = 0
    fam_on = 0
    individual = individualList()
    family = familyList()
    for line in f:
        str = line.split()
        if(str != []):
            if(str[0] == '0'):
                if(fam_on == 1):
                    list_family.append(family)
                    family = familyList()
                    fam_on = 0
                if(indi_on == 1):
                    list_individual.append(individual)
                    individual = individualList()
                    indi_on = 0               
                if(str[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(str[2] == 'INDI'):
                        indi_on = 1
                        individual[0] = (str[1])
                    if(str[2] == 'FAM'):
                        fam_on = 1
                        family[0] = (str[1])
            if(str[0] == '1'):
                if(str[1] == 'NAME'):
                    individual[1] = str[2] + " " + getLastName(str[3])
                if(str[1] == 'SEX'):
                    individual[2] = str[2]
                if(str[1] == 'FAMS'):
                    individual[5].append(str[2])
                if(str[1] == 'FAMC'):
                    individual[6] = str[2]
                if(str[1] == 'HUSB'):
                    family[1] = str[2]
                if(str[1] == 'WIFE'):
                    family[2] = str[2]
                if(str[1] == 'CHIL'):
                    family[5].append(str[2])
                if(str[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = str[1]                                
            if(str[0] == '2'):
                if(str[1] == 'DATE'):
                    date = str[4] + " " + str[3] + " " + str[2]
                    if(date_id == 'MARR'):
                        family[3] = dateFormatConversion(date)
                    if(date_id == 'DIV'):
                        family[4] = dateFormatConversion(date)
                    if(date_id == 'BIRT'):
                        individual[3] = dateFormatConversion(date)
                    if(date_id == 'DEAT'):
                        individual[4] = dateFormatConversion(date)
                    
    return list_individual,list_family

def main(gedFileName):
    list_individual, list_family= toParse(gedFileName)
    list_individual.sort()
    list_family.sort()
    marriageBeforeDivorce(list_family)

main('D:/SSW-555/Week 5/Akanksha_Homework 4/Homework 4/akankshaGedcom.ged')
