#Project 03

#Importing file
from prettytable import PrettyTable

#For the family list
def familyList():
    flist = [0 for i in range(6)]
    flist[5] = []
    return flist

#For the individual list
def individualList():
    return [0 for i in range(7)]

#get last name
def lastName(s):
    data=''
    for i in s:
        if(i != '/'):
            data += i
    return data

#getting name using IDs
def getNameUsingID(individualList, ID):
    for i in individualList:
        if(i[0] == ID):
            return i[1]
def fileLength(f):
    for i,l in enumerate(f):
        pass
    return i+1

#parsing the gedcomo file 
def getcomParse(fileName):
    readFile = open(fileName,'r')
    f = fileLength(open(fileName))
    indiValue = 0
    famValue = 0
    indi_list = []
    fam_list = []
    indiData = individualList()
    famData = familyList()
    for line in readFile:
        s = line.split()
        if(s != []):
            if(s[0] == '2'):
                if(s[1] == 'DATE'):
                    date = s[4] + " " + s[3] + " " + s[2]
                    if(dateID == 'BIRT'):
                        indiData[3] = date
                    if(dateID == 'DEAT'):
                        indiData[4] = date
                    if(dateID == 'MARR'):
                        famData[3] = date
                    if(dateID == 'DIV'):
                        famData[4] = date

            if(s[0] == '1'):
                if(s[1] == 'NAME'):
                    indiData[1] = s[2] + " " + lastName(s[3])
                if(s[1] == 'SEX'):
                    indiData[2] = s[2]
                if(s[1] == 'BIRT'):
                    dateID = 'BIRT'
                if(s[1] == 'DEAT'):
                    dateID = 'DEAT'
                if(s[1] == 'MARR'):
                    dateID = 'MARR'
                if(s[1] == 'DIV'):
                    dateID = 'DIV'
                if(s[1] == 'FAMS'):
                    indiData[5] = s[2]
                if(s[1] == 'FAMC'):
                    indiData[6] = s[2]
                if(s[1] == 'HUSB'):
                    famData[1] = s[2]
                if(s[1] == 'WIFE'):
                    famData[2] = s[2]
                if(s[1] == 'CHIL'):
                    famData[5].append(s[2])
    
            if(s[0] == '0'):
                if(indiValue == 1):
                    indi_list.append(indiData)
                    indiData = individualList()
                    indiValue = 0
                if(famValue == 1):
                    fam_list.append(famData)
                    famData = familyList()
                    famValue = 0
                if(s[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(s[2] == 'INDI'):
                        indiValue = 1
                        indiData[0] = (s[1])
                    if(s[2] == 'FAM'):
                        famValue = 1
                        famData[0] = (s[1])
    return indi_list, fam_list


#Function calling
indi_list, fam_list = getcomParse("D:/SSW-555/Week 2/Akanksha_project02/My-Family-5-Sep-2017-105.ged")
indi_list.sort()
fam_list.sort()

#printing the ouput about individuals
for i in indi_list:
    table = PrettyTable(["ID", "Name" , "Sex", "Birth Date", "Death Date" , "Child" , "Spouse"])
    table.add_row([i[0] , i[1], i[2],i[3], i[4] , i[5] , i[6]])
    print (table)

#Printing Husband's and wife's details    
for i in fam_list:
    table1 = PrettyTable(["ID", "Husband's Name" , "Wife's Name"])
    table1.add_row([i[0] , getNameUsingID(indi_list,i[1]) , getNameUsingID(indi_list,i[2]) ])
    print (table1)
