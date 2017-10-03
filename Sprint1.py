
#importing packages
import datetime
from prettytable import PrettyTable

dateList=[]
#getting name using IDs
def getNameUsingID(individualList, ID):
    for i in individualList:
        if(i[0] == ID):
            return i[1]
#For the individual list

def individualList():
    ilist = [0 for i in range(7)]
    ilist[5] = []
    return ilist

	
#For the family list
def familyList():
    flist = [0 for i in range(6)]
    flist[5] = []
    return flist

#get last name
def lastName(s):
    temp=''
    for i in s:
        if(i != '/'):
            temp += i
    return temp

#get today's date
def currentDate():
    currDate = str(datetime.date.today())
    return currDate

#Converting date into a standard format
def convertDateFormat(date):
    temp = date.split()
    if(temp[1] == 'JAN'): temp[1] = '01';
    if(temp[1] == 'FEB'): temp[1] = '02';
    if(temp[1] == 'MAR'): temp[1] = '03';
    if(temp[1] == 'APR'): temp[1] = '04';
    if(temp[1] == 'MAY'): temp[1] = '05';
    if(temp[1] == 'JUN'): temp[1] = '06';
    if(temp[1] == 'JUL'): temp[1] = '07';
    if(temp[1] == 'AUG'): temp[1] = '08';
    if(temp[1] == 'SEP'): temp[1] = '09';
    if(temp[1] == 'OCT'): temp[1] = '10';
    if(temp[1] == 'NOV'): temp[1] = '11';
    if(temp[1] == 'DEC'): temp[1] = '12';
    if(temp[2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        temp[2] = '0' + temp[2]
    return (temp[0] + '-' + temp[1] + '-' + temp[2])

dateList = []
todayDate = currentDate()

#User Story 1
def DatesBeforeCurrentDate(indiListData, famListData):
  
  #for individual
    for i in indiListData:
        if(i[3] > todayDate):
            dateList.append(i[3])
            print(i[3] + " : " + i[0] + " is before the current date")
        if(i[4] != 0):
            if(i[4] > todayDate):
                dateList.append(i[4])
                print(i[4] + " : " + i[0] + " is before the current date")
	#for family
    for i in famListData:
        if(i[3] > todayDate):
            dateList.append(i[3])
            print(i[3] + " : " + i[0] + " is before the current date")
        if(i[4] != 0):
            if(i[4] > todayDate):
                dateList.append(i[4])
                print(i[4] + " : " + i[0] + " is before the current date")
    if(len(dateList) == 0):
        print("There are no dates before the current date :)")
    else:
        print("There dates after the current date :(")
        print(dateList)

#User Story 2

#this function helps to get all the marriage dates
def getMarriedDateUsingID(famListData, id):
    for i in famListData:
        if(i[0] == id):
            return i[3]
			
def birthBeforeMarriage(indiListData, famListData):
    for i in indiListData:
        birthDate = i[3]
        if(i[5] != []):
            for j in i[5]:
                if(birthDate > getMarriedDateUsingID(famListData, j)): #We call the function here to get the dates
                    dateList.append(i[1])
                    print(i[1] + " have their marriage dates before birth date")
                    break
    if(len(dateList) == 0):
        print("There is no individual having birth dates after marriage dates :)")
    else:
        print("These people have birth dates after their marriage dates :( ")
        print(dateList)
		
#User Story 3
		
def BirthBeforeDeath(indiListData):
    for i in indiListData:
        if(i[4] != 0):
            if(i[3] > i[4]):
                dateList.append(i[1])
                print(i[1] + " have their birth date after death date")
    if(len(dateList) == 0):
        print("There is no one having birthdate after death date :)")
    else:
        print("These people have birth dates after their marriage dates :( ")
        print(dateList)
#User Story 4

def MarriageBeforeDivorce(famListData):
    for i in famListData:
        if(i[4] != 0):
            if(i[3] > i[4]):
                dateList.append(i[0])
                print(i[0] + " have marriage date after the divorce date")
    if(len(dateList) == 0):
        print("There is no one having marriage dates after divorce date :)")
    else:
        print("These people have marriage dates after their divorce dates :( ")
        print(dateList)
		
#This function returns all the death dates
def getDeathDateByID(indiListData, id):
    for i in indiListData:
        if(i[0] == id):
            if(i[4] != 0):
                return i[4]

		
#User Story 5
def MarriageBeforeDeath(indiListData, famListData):
#for family
    for i in famListData:
        if(getDeathDateByID(indiListData, i[1]) != None):  
            if(i[3] > getDeathDateByID(indiListData, i[1])):  #the function is called here to get all the death dates by id
                dateList.append(i[0])
                print(i[0] + " have mariage dates after death dates")
        if(getDeathDateByID(indiListData, i[2]) != None):
            if(i[3] > getDeathDateByID(indiListData, i[2])):
                dateList.append(i[0])
                print(i[0] + " have marriage dates after death dates")
    if(len(dateList) == 0):
        print("There are no marriages after the death dates :)")
    else:
        print("These people have marriage dates after their death dates :( ")
        print(dateList)

#User Story 6

def DivorceBeforeDeath(indiListData, famListData):
#for family

    for i in famListData:
        if(i[4] != 0):
            if(getDeathDateByID(indiListData, i[1]) != None):     #the function is called here to get all the death dates by id
                if(i[4] > getDeathDateByID(indiListData, i[1])):
                    dateList.append(i[0])
                    print(i[0] + " have divorce dates after death dates")
            if(getDeathDateByID(indiListData, i[2]) != None):
                if(i[4] > getDeathDateByID(indiListData, i[2])):
                    dateList.append(i[0])
                    print(i[0] + " have divorce dates after death dates")
    if(len(dateList) == 0):
        print("There are no divorce after the death dates :)")
    else:
        print("These people have divorce dates after their death dates :( ")
        print(dateList)
		
		
#Function to get the age
def getAgeUsingID(indiListData, id):
	flag = 0
	for i in indiListData:
		if(i[0] == id):
			birthdayDay = i[3]
			value = birthdayDay.split('-')
			birthYear = int(value[0])
			birthMonth = int(value[1])
			birthdayDay = int(value[2])
			if(i[4] != 0):
				deathDay = i[4]
				flag = 1
				
	if(flag == 1):
		value = deathDay.split('-')
		deathYear = int(value[0])
		deathMonth = int(value[1])
		deathDay = int(value[2])
		return deathYear - birthYear - ((deathMonth, deathDay) < (birthMonth, birthdayDay))
    
	
	currentDay = currentDate().split('-')
	currentYear = int(currentDay[0])
	currentMonth = int(currentDay[1])
	currentDay = int(currentDay[2])
	return currentYear - birthYear - ((currentMonth, currentDay) < (birthMonth, birthdayDay))	
		
#User Story 7

def lessThan150Years(indiListData):
    for i in indiListData:
        if(getAgeUsingID(indiListData, i[0]) >= 150):  #calling the function to get the age using id
            dateList.append(i[0])
            print(i[0] + " have their age more than 150")
    if(len(dateList)==0):
        print("All have ages less than 150 :)")
    else:
        print("These are people having more than 150 age")
        print(dateList)

#Function t get birthdates  using id
def getBirthDateUsingID(indiListData, id):
    for i in indiListData:
        if(i[0] == id):
            return i[3]
			
#Calculating the space of 9 months that is adding the 9 months so that we can compare the and find if the birth of the child is before the marriage date of his parents
def spaceof9month(dateValue):
    dateData = dateValue.split('-')
    if(int(dateData[1]) <= 3):
        dateData[1] = str(int(dateData[1]) + 9)
    else:
        dateData[1] = '0'+str(int(dateData[1]) - 3)
        dateData[0] = str(int(dateData[0]) + 1)
    dateValue = dateData[0] + '-' + dateData[1] + '-' + dateData[2]
    return dateValue


#User Story 8
def birthBeforeMarriageofParents(indiListData, famListData):
    for i in famListData:
        if(i[5] != []):
            dateData = i[3]
            for j in i[5]:
                if(getBirthDateUsingID(indiListData, j) <= dateData): #getting birthdates using id
                    dateList.append(j)
                    print(j + " was born before the marriage of their parents.")
                    continue
                if(i[4] != 0):
                    finalDate = spaceof9month(i[4])
                    if(getBirthDateUsingID(indiListData, j) >= finalDate):   
                        dateList.append(j)
                        print(j + " was born after the marriage of their parents")
                        continue
    if(len(dateList)==0):
        print("All children have been born after the marriage of their parents :)")
    else:
        print("These children were born before marriage of their parents :(")
        print(dateList)


#parsing the gedcom file 
def getcomParse(file_name):
    f = open(file_name,'r')
    indiValue = 0
    famValue = 0
    indiListData = []
    famListData = []
    indiData = individualList()
    famData = familyList()
    for line in f:
        s = line.split()
        if(s != []):
            if(s[0] == '0'):
                if(indiValue == 1):
                    indiListData.append(indiData)
                    indiData = individualList()
                    indiValue = 0
                if(famValue == 1):
                    famListData.append(famData)
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
            if(s[0] == '1'):
                if(s[1] == 'NAME'):
                    indiData[1] = s[2] + " " + lastName(s[3])
                if(s[1] == 'SEX'):
                    indiData[2] = s[2]
                if(s[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = s[1]
                if(s[1] == 'FAMS'):
                    indiData[5].append(s[2])
                if(s[1] == 'FAMC'):
                    indiData[6] = s[2]
                if(s[1] == 'HUSB'):
                    famData[1] = s[2]
                if(s[1] == 'WIFE'):
                    famData[2] = s[2]
                if(s[1] == 'CHIL'):
                    famData[5].append(s[2])
            if(s[0] == '2'):
                if(s[1] == 'DATE'):
                    date = s[4] + " " + s[3] + " " + s[2]
                    if(date_id == 'BIRT'):
                        indiData[3] = convertDateFormat(date)
                    if(date_id == 'DEAT'):
                        indiData[4] = convertDateFormat(date)
                    if(date_id == 'MARR'):
                        famData[3] = convertDateFormat(date)
                    if(date_id == 'DIV'):
                        famData[4] = convertDateFormat(date)
    return indiListData, famListData


def main(file_name):
    indiListData, famListData = getcomParse(file_name)
    indiListData.sort()
    famListData.sort()
    DatesBeforeCurrentDate(indiListData, famListData)
    birthBeforeMarriage(indiListData, famListData)
    BirthBeforeDeath(indiListData)
    MarriageBeforeDivorce(famListData)
    MarriageBeforeDeath(indiListData, famListData)
    DivorceBeforeDeath(indiListData, famListData)
    lessThan150Years(indiListData)
    birthBeforeMarriageofParents(indiListData, famListData)
    for i in indiListData:
        table = PrettyTable(["ID", "Name" , "Sex", "Birth Date", "Death Date" , "Child" , "Spouse"])
        table.add_row([i[0] , i[1], i[2],i[3], i[4] , i[5] , i[6]])
        print (table)
    for i in famListData:
        table1 = PrettyTable(["ID", "Husband's Name" , "Wife's Name"])
        table1.add_row([i[0] , getNameUsingID(indiListData,i[1]) , getNameUsingID(indiListData,i[2]) ])
        print (table1)

fileInput= 'C:\SEM 3\Agile\hw4\Updated2GedcomFile.ged'
main(fileInput)

