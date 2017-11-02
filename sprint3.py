
#importing packages
import datetime
from prettytable import PrettyTable
import itertools as iter

dateList=[]
dataList = []



#For the individual list

def individualList():
    ilist = [0 for i in range(7)]
    ilist[5] = []
    return ilist
#getting last name data by id
def getLastNameByID(list_indi, id):
    for i in list_indi:
        if(i[0] == id):
            temp_name = i[1].split(' ')
            return temp_name[1]
	
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


#get name using id
def getNameByID(indiListData, id):
    for i in indiListData:
        if(i[0] == id):
            return i[1]
			
#get death date using ID
def getDeathDateByID(list_individual, id):
    for i in list_individual:
        if(i[0] == id):
            if(i[4] != 0):
                return i[4]
#get spouse details			
def getSpouseFamily(listIndi, id):
    for i in listIndi:
        if(i[0] == id):
            return i[5]
			
#get individual name using id       
def getIndiName(listIndi, id):
    for i in listIndi:
        if(i[0] == id):
            return i[1]

todayDate = currentDate()
#Function to get the marriage details by id				
def getMarriageByID(list_individual, id, dateOfMarriage):
    marriageDate = dateOfMarriage.split('-')
    yearOfMarriage = int(marriageDate[0])
    monthOfMarriage = int(marriageDate[1])
    dateOfMarriage = int(marriageDate[2])
    for i in list_individual:
        if(i[0] == id):
            dateOfBirth = i[3]
    birthDate = dateOfBirth.split('-')
    yearOfBirth = int(birthDate[0])
    monthOfBirth = int(birthDate[1])
    dateOfBirth = int(birthDate[2])
    return yearOfMarriage - yearOfBirth - ((monthOfMarriage, dateOfMarriage) < (monthOfBirth, dateOfBirth))

#get gender using id
def getGenderByID(list_individual, id):
    for i in list_individual:
        if(i[0] == id):
            return i[2]
#getting birth dates by id
def getBirthDateByID(indiListData, id):
    for i in indiListData:
        if(i[0] == id):
            return i[3]			



#calculate difference in months
def difference_months(dateData1, dateData2):
    temp1 = dateData1.split('-')
    temp2 = dateData2.split('-')
    ndateData1 = datetime.date(int(temp1[0]), int(temp1[1]), int(temp1[2]))
    ndateData2 = datetime.date(int(temp2[0]), int(temp2[1]), int(temp2[2]))
    return int((ndateData1 - ndateData2).days / 30.4)

#calculate difference in days
def difference_days(dateData1, dateData2):
    temp1 = dateData1.split('-')
    temp2 = dateData2.split('-')
    ndateData1 = datetime.date(int(temp1[0]), int(temp1[1]), int(temp1[2]))
    ndateData2 = datetime.date(int(temp2[0]), int(temp2[1]), int(temp2[2]))
    return abs(int((ndateData1 - ndateData2).days))
#get sex using id
def getSexByID(list_indi, id):
    for i in list_indi:
        if(i[0] == id):
            return i[2]
	        
#get age by id
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
    c_date = currentDate().split('-')
    c_year = int(c_date[0])
    c_month = int(c_date[1])
    c_date = int(c_date[2])
    return c_year - b_year - ((c_month, c_date) < (b_month, b_date))


			
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

#########################################################SPRINT 1########################################################

#User Story 1
def DatesBeforeCurrentDate(indiListData, famListData):
  
  #for individual
    for i in indiListData:
        if(i[3] > todayDate):
            dateList.append(i[3])
            print("ERROR: INDIVIDUAL: US01: " + i[3] + " : " + i[0] + " is before the current date")
        if(i[4] != 0):
            if(i[4] > todayDate):
                dateList.append(i[4])
                print("ERROR: INDIVIDUAL: US01: "+i[4] + " : " + i[0] + " is before the current date")
	#for family
    for i in famListData:
        if(i[3] > todayDate):
            dateList.append(i[3])
            print("ERROR: INDIVIDUAL: US01: i[3] + " + i[0] + " is before the current date")
        if(i[4] != 0):
            if(i[4] > todayDate):
                dateList.append(i[4])
                print("ERROR: INDIVIDUA: US01: "+ i[4] + " : " + i[0] + " is before the current date")
    if(len(dateList) == 0):
        print("US01: There are no dates before the current date :)")
    else:
        print("ERROR: INDIVIDUAL: US01: There dates after the current date :(")
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
                    print("ERROR: INDIVIDUAL: US02: "+ i[1] + " have their marriage dates before birth date")
                    break
    if(len(dateList) == 0):
        print("US02: There is no individual having birth dates after marriage dates :)")
    else:
        print("ERROR: INDIVIDUAL: US02: These people have birth dates after their marriage dates :( ")
        print(dateList)
		
#User Story 3
		
def BirthBeforeDeath(indiListData):
    for i in indiListData:
        if(i[4] != 0):
            if(i[3] > i[4]):
                dateList.append(i[1])
                print("ERROR: INDIVIDUAL: US03 "+ i[1] + " have their birth date after death date")
    if(len(dateList) == 0):
        print("US03: There is no one having birthdate after death date :)")
    else:
        print("ERROR: INDIVIDUAL: US03: These people have birth dates after their marriage dates :( ")
        print(dateList)
#User Story 4

def MarriageBeforeDivorce(famListData):
    for i in famListData:
        if(i[4] != 0):
            if(i[3] > i[4]):
                dateList.append(i[0])
                print("ERROR: INDIVIDUAL: US04: "+i[0] + " have marriage date after the divorce date")
    if(len(dateList) == 0):
        print("US04: There is no one having marriage dates after divorce date :)")
    else:
        print("ERROR: INDIVIDUAL: US04: These people have marriage dates after their divorce dates :( ")
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
                print("ERROR: INDIVIDUAL: US05: "+i[0] + " have mariage dates after death dates")
        if(getDeathDateByID(indiListData, i[2]) != None):
            if(i[3] > getDeathDateByID(indiListData, i[2])):
                dateList.append(i[0])
                print("ERROR: INDIVIDUAL: US05: "+ i[0] + " have marriage dates after death dates")
    if(len(dateList) == 0):
        print("US05: There are no marriages after the death dates :)")
    else:
        print("ERROR: INDIVIDUAL: US05: These people have marriage dates after their death dates :( ")
        print(dateList)

#User Story 6

def DivorceBeforeDeath(indiListData, famListData):
#for family

    for i in famListData:
        if(i[4] != 0):
            if(getDeathDateByID(indiListData, i[1]) != None):     #the function is called here to get all the death dates by id
                if(i[4] > getDeathDateByID(indiListData, i[1])):
                    dateList.append(i[0])
                    print("ERROR: INDIVIDUAL: US06: "+i[0] + " have divorce dates after death dates")
            if(getDeathDateByID(indiListData, i[2]) != None):
                if(i[4] > getDeathDateByID(indiListData, i[2])):
                    dateList.append(i[0])
                    print("ERROR: INDIVIDUAL: US06: "+i[0] + " have divorce dates after death dates")
    if(len(dateList) == 0):
        print("US06: There are no divorce after the death dates :)")
    else:
        print("ERROR: INDIVIDUAL: US06: These people have divorce dates after their death dates :( ")
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
            print("ERROR: INDIVIDUAL: US07" + i[0] + " have their age more than 150")
    if(len(dateList)==0):
        print("US07: All have ages less than 150 :)")
    else:
        print("ERROR: INDIVIDUAL: US07: These are people having more than 150 age")
        print(dateList)

#Function get birthdates  using id
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
                    print("ERROR: INDIVIDUAL: US08:" +j + " was born before the marriage of their parents.")
                    continue
                if(i[4] != 0):
                    finalDate = spaceof9month(i[4])
                    if(getBirthDateUsingID(indiListData, j) >= finalDate):   
                        dateList.append(j)
                        print("ERROR: INDIVIDUAL: US08: "+ j + " was born after the marriage of their parents")
                        continue
    if(len(dateList)==0):
        print("US08: All children have been born after the marriage of their parents :)")
    else:
        print("ERROR: INDIVIDUAL: US08: These children were born before marriage of their parents :(")
        print(dateList)
		
		
################################################SPRINT 2###########################################33
		
#UserStory 09
def birthBeforeDeathOfParents(indiListData, famListData):
    for i in famListData:
        if(i[5] != []):
            for j in i[5]:
			
                childBirthDate= getBirthDateByID(indiListData, j)
                motherDeathDate = getDeathDateByID(indiListData, i[2])
                fatherDeathDate = getDeathDateByID(indiListData, i[1])

                if(motherDeathDate != None):
                    if(childBirthDate > motherDeathDate):
                        dateList.append(j)
                        print("ERROR: INDIVIDUAL: US09: " + j + "was born after death of mother" + i[2])
                        if(fatherDeathDate != None):
                            if(childBirthDate > fatherDeathDate):
                                dateList.append(j)
                                print("ERROR: INDIVIDUAL: US09: " + j + "was born after death of father" + i[1])
    if(len(dateList) == 0):
        print("US09: There is no one who was born after their parent's death")
    else:
        print("ERROR: INDIVIDUAL: US09: These were born after their parent's death")
        print(dateList)

  

#User Story 10


def marriageAfter14(indiListData, famListData):
    marriagelist = []
    for i in famListData:
        if(getMarriageByID(indiListData, i[1], i[3])<14):
            marriagelist.append(i[1])
            print("ERROR: INDIVIDUAL: US10: User Story 10: This individual with ID " + i[1] + " married before he/she turned 14 in family with ID" + i[0])
        if(getMarriageByID(indiListData, i[2], i[3])<14):
            marriagelist.append(i[2])
            print("ERROR: INDIVIDUAL: US10: This individual with ID " + i[2] + " married before he/she turned 14 in family with ID " + i[0])

    if(len(marriagelist) != 0):
        print("ERROR: INDIVIDUAL: US10:  The individuals mentioned below married before they turned 14: ")
        print(marriagelist)       
    else:
        print("US10: There are no individuals who married before they turned 14 years.")
		
		
#User Story 11
def getSpouseNameById(famListData, famId, spouseId):
    for i in famListData:
        if(i[0] == famId):
            if(i[1] == spouseId):
                return i[2]
            if(i[2] == spouseId):
                return i[1]

def getDivorceDateById(famListData, famId):
    for i in famListData:
        if(i[0] == famId):
            if(i[4] != 0):
                return i[4]
def getMarriageDateById(famListData, id):
    for i in famListData:
        if(i[0] == id):
            return i[3]
def noBigamy(indiListData, famListData):
    noBigamyList = []
    for i in indiListData:
        family = []
        t = []
        if(len(i[5]) > 1):
            selfId = i[0]
            for j in i[5]:
                t.append(getMarriageDateById(famListData, j))
                t.append(j)
                t.append(getSpouseNameById(famListData, j, selfId))
                t.append(getDivorceDateById(famListData, j))
                t.append(getDeathDateByID(indiListData, getSpouseNameById(famListData, j, selfId)))
                family.append(t)
                t = []
            family.sort()
            for z in range(1, len(family)):
                if(family[z-1][3] == None and family[z-1][4] == None):
                    noBigamyList.append(selfId)
                    print("ERROR: INDIVIDUAL: US11: The person with id " + selfId + " is married to the person " + family[z][2] + " with family id " + family[z][1] + " while the person is still married to person with id " + family[z-1][2] + " in family " + family[z-1][1])
                else:
                    if(family[z-1][3] != None):
                        if(family[z][0] < family[z-1][3]):
                            noBigamyList.append(selfId)
                            print("ERROR: INDIVIDUAL: US11: The person with id " + selfId + " is married to the person " + family[z][2] + " with family id " + family[z][1] + " before the person filed divorce with spouse " + family[z-1][2] + " in family " + family[z-1][1])
                    if(family[z-1][4] != None):
                        if(family[z][0] < family[z-1][4]):
                            noBigamyList.append(selfId)
                            print("ERROR: INDIVIDUAL: US11: The person with id " + selfId + " is married to the person " + family[z][2] + " with family id  " + family[z][1] + " before his/her spouse's death" + family[z-1][2] + " in family " + family[z-1][1])
    if(len(noBigamyList) == 0):
        print("US11: The individual in the given gedcom file is not involved in Bigamy.")
    else:
        print("ERROR: INDIVIDUAL: US11: The individuals who are involved in Bigamy are as follows: ")
        print(noBigamyList)
	

#User Story 12

def parentsNotTooOld(list_indi, list_fam):
    list1 = []
    for i in list_fam:
        if(i[5] != []):
            mother_age = getAgeByID(list_indi, i[2])
            father_age = getAgeByID(list_indi, i[1])
            for j in i[5]:
                child_age = getAgeByID(list_indi, j)
                if(mother_age - child_age >= 60):
                    list1.append(i[2])
                    print("ERROR: INDIVIDUAL: US12: " + i[2] + " Mother is 60 years or more older than her child " + j)
                if(father_age - child_age >= 80):
                    list1.append(i[1])
                    print("ERROR: INDIVIDUAL: US12:" + i[1] + " Father is 80 years or more older than his child " + j)
    if(len(list1) == 0):
        print("US12: Both mother and father are not too old")
    else:
        print("ERROR: INDIVIDUAL: US12: Parents who are too old compared to their children: ")
        print(list1)

		
#UserStory 13
def SiblingsSpacing(famListData, indiListData):
    for i in famListData:
        if(i[5] != [] and len(i[5]) > 1):
            siblingPairs = list(iter.combinations(i[5], 2))
            for j in siblingPairs:
                siblings_months = abs(difference_months(getBirthDateByID(indiListData, j[0]), getBirthDateByID(indiListData, j[1])))
                siblings_days = abs(difference_days(getBirthDateByID(indiListData, j[0]), getBirthDateByID(indiListData, j[1])))
                if(siblings_months <= 8 and siblings_days >= 3):
                    dateList.append(j)
                    print("ERROR: INDIVIDUAL: US13: Siblings " + j[0] + " and " + j[1] + " have their birth dates eight months apart")
                if(siblings_months == 0 and siblings_days >= 2):
                    dateList.append(j)
                    print("ERROR: INDIVIDUAL: US13: Siblings " + j[0] + " and " + j[1] + " have their birth days 2 or more days apart")
    if(len(dateList)==0):
        print("US13: All the Siblings have correct spacing")
    else:
        print("ERROR: INDIVIDUAL: US13: The following Sibling pairs have bad birth date spacings")
        print(dateList)

	
#User Story 14


def multipleBirthslessThan5(list_individual,list_family):
    multipleBirthsList = []
    m = 0
    for i in list_family:
        birthList = []
        if(i[5] != [] and len(i[5]) > 5):
            for j in i[5]:
                birthList.append(getBirthDateByID(list_individual, j))
            birthListLength = len(birthList)
            birthListSet = set(birthList)
            listsetLength = len(birthListSet)
            m = (birthListLength - listsetLength)
            if( m >= 5):
                multipleBirthsList.append(i[0])
                print("ERROR: FAMILY: US14: The Family with ID " + i[0] + " had more than 5 Births and hence is not valid.")
    if(len(multipleBirthsList)!=0):
        print("ERROR: FAMILY: US14: The families mentioned below had more than 5 kids during the time of birth:")
        print(multipleBirthsList)       
    else:
        print("Us14: There are no families with more than 5 kids.")
    return m

		
#User Story 15
def lessThan15Siblings(famListData):
    siblingList = []
    for i in famListData:
        if(len(i[5]) >= 15):
            siblingList.append(i[0])
            print("ERROR: FAMILY: US15: The family with id " + i[0] + " has 15 or more siblings.")
    if(len(siblingList)==0):
        print("US15: There are no families with 15 or more siblings.")
    else:
        print("ERROR: FAMILY: US15: The families with 15 or more siblings are as follows: ")
        print(siblingList)
        
#User Story 16

def maleLastNames(list_indi, list_fam):
    list1 = []
    for j in list_fam:
        male_names = []
        male_names.append(getLastNameByID(list_indi, j[1]))
        if(j[5] != []):
            for k in j[5]:
                if(getSexByID(list_indi, k) == 'M'):
                    male_names.append(getLastNameByID(list_indi, k))
        if(len(set(male_names)) != 1):
            list1.append(j[0])
            print('"ERROR: FAMILY: US16: Family ' + j[0] + ' has one or more male members with different last name(s).')
    if(len(list1)==0):
        print("US16: Males in all families have the same last name.")
    else:
        print("ERROR: FAMILY: US16: Families which have one or more male members with different last name(s): ")
        print(list1)


			
########################################SPRINT3###########################################3
#User Story 21
def correctGenderForRoles(indiListData, famListData):
    genderRoleList = []
    for i in famListData:
        if(getGenderByID(indiListData, i[2]) != 'F'):
            genderRoleList.append(i[2])
            print("ERROR: US21: INDIVIDUAL: This Individual with ID " + i[2] + " in family with ID" + i[0] + " has incorrect Gender role.")
        if(getGenderByID(indiListData, i[1]) != 'M'):
            genderRoleList.append(i[1])
            print("ERROR: US21: INDIVIDUAL: This Individual with ID " + i[1] + " in the family with ID" + i[0] + " has incorrect Gender role.")      
    if(len(genderRoleList) != 0):
        print("ERROR: INDIVIDUAL: US21: The individuals mentioned below have incorrect gender role: ")
        print(genderRoleList)
    else:
        print("US21: There are no individuals with incorrect gender roles.")
   	
#User Story 22
def uniqueId(indiListData, famListData):
    individualIdList = []
    familyIdList = []
    individualDuplicateIdList = []
    familyDuplicateList = []
    f = 0
    for i in indiListData:
        individualIdList.append(i[0])
    for i in famListData:
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
            print("ERROR: US22: FAMILY: The following individuals have duplicate id's: ")
            print(set(individualDuplicateIdList))
        if(len(familyDuplicateList) != 0):
            print("ERROR: US22: FAMILY: The following families have duplicate id's: ")
            print(set(familyDuplicateList))            
    else:
        print("US22: The IDs in the list are unique.")

#User Story 23

def unique_names_and_birth_dates(indiListData):
    list1 = []
    list2 = []
    for i in indiListData:
        list2.append((i[1], i[3]))
    if(len(list2) == len(set(list2))):
        print("US23: all Individuals have unique name and birth date accordingly .")
    else:
        for i in list2:
            flag = 0
            for j in list2:
                if (i == j):
                    flag += 1
                    if(flag > 1):
                        list1.append(i)
        if(len(list1) != 0):
            print("ERROR: US23: INDIVIDUAL: According to unique name and birth date, following Individual(s) dont have unique name and birth date : ")
            print(set(list1))
#User Story 24
def uniqueFamiliesBySpouses(indiListData, famListData):
    for i in famListData:
        dataList.append((getNameByID(indiListData, i[1]), getNameByID(indiListData, i[2]), i[3]))
    if(len(dataList) == len(set(dataList))):
        print("US24: All Families are unique.")
    else:
        for i in dataList:
            flag = 0
            for j in dataList:
                if (i == j):
                    flag += 1
                    if(flag > 1):
                        dateList.append(i)
        if(len(dateList) != 0):
            print("ERROR: FAMILY: US24:  These families are not unique considering the spouse details: " + set(dateList))

#User Story 29
def deceasedList(indiListData):
    deceasedList = []
    for individual in indiListData:
        if individual[4] is not 0:
            deceasedList.append(individual[0])
    print("ERROR: INDIVIDUAL: US29: Deceased individuals list is as follows : ", deceasedList)
    for i in deceasedList:
        print("ERROR: INDIVIDUAL: US29: Individual with ID " + i + " and name " + getNameByID(indiListData, i) + " passed away on " + getDeathDateByID(indiListData, i))
    return deceasedList

#User Story 30
def livingPeopleMarried(indiListData, famListData):
    marriedPeopleList = []
    for i in famListData:
        if(getGenderByID(indiListData, i[1]) == None):
            if(i[1] not in marriedPeopleList):
                marriedPeopleList.append(i[1])
        if(getGenderByID(indiListData, i[2]) == None):
            if(i[2] not in marriedPeopleList):
                marriedPeopleList.append(i[2])
    print ("ERROR: US30: INDIVIDUAL: Individuals who are married and alive", marriedPeopleList)
    for i in marriedPeopleList:
        print("ERROR: INDIVIDUAL: US30: ID:" + i + " with name " + getIndiName(indiListData, i) + " is married with family " + str(getSpouseFamily(indiListData, i)))
   
#User Story 31

def listLivingSingle(indiListData):
    single = []
    for i in indiListData:
        if(i[4] == 0 and i[5] == []):
            single.append(i[0])
    print("ERROR: US31: INDIVIDUAL: List of Individuals living single : ", single)
    for k in single:
        print("ERROR: INDIVIDUAL: US31: " + k + ": " + getNameByID(indiListData, k))
   
#User Story 32
def listOfMultipleBirths(indiListData, famListData):
    for i in famListData:
        listOfMultipleBirth = []
        listOfBirthDates = []
        if(i[5] != []):
            for j in i[5]:
                listOfBirthDates.append(getBirthDateUsingID(indiListData, j))
            for j in set(listOfBirthDates):
                temp = []
                for k in i[5]:
                    if(j == getBirthDateUsingID(indiListData, k)):
                        temp.append(k)
                listOfMultipleBirth.append(temp)
        if(listOfMultipleBirth != []):
            for j in listOfMultipleBirth:
                if(len(j) > 1):
                    print('ERROR: US32: INDIVIDUAL: These individuals ' + i[0] + ' were born at the same time: ', j)
                    for k in j:
                        print("ERROR: US32: INDIVIDUAL: "+ k + ': ' + getNameByID(indiListData, k))


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
    for i in indiListData:
        table = PrettyTable(["ID", "Name" , "Sex", "Birth Date", "Death Date" , "Child" , "Spouse"])
        table.add_row([i[0] , i[1], i[2],i[3], i[4] , i[5] , i[6]])
        print (table)
    for i in famListData:
        table1 = PrettyTable(["ID", "Husband's Name" , "Wife's Name"])
        table1.add_row([i[0] , getNameByID(indiListData,i[1]) , getNameByID(indiListData,i[2]) ])
        print (table1)

	#Sprint 1
    DatesBeforeCurrentDate(indiListData, famListData)
    birthBeforeMarriage(indiListData, famListData)
    BirthBeforeDeath(indiListData)
    MarriageBeforeDivorce(famListData)
    MarriageBeforeDeath(indiListData, famListData)
    DivorceBeforeDeath(indiListData, famListData)
    lessThan150Years(indiListData)
    birthBeforeMarriageofParents(indiListData, famListData)
	
    #Sprint 2
    birthBeforeDeathOfParents(indiListData, famListData)
    marriageAfter14(indiListData, famListData)
    noBigamy(indiListData, famListData)
    parentsNotTooOld(indiListData, famListData)
    SiblingsSpacing(famListData, indiListData)
    multipleBirthslessThan5(indiListData, famListData)
    lessThan15Siblings(famListData)
    maleLastNames(indiListData, famListData)
    
	#Sprint 3
    correctGenderForRoles(indiListData, famListData)
    uniqueId(indiListData, famListData)
    unique_names_and_birth_dates(indiListData)
    uniqueFamiliesBySpouses(indiListData, famListData)
    deceasedList(indiListData)
    livingPeopleMarried(indiListData, famListData)
    listLivingSingle(indiListData)
    listOfMultipleBirths(indiListData, famListData)

    
	
fileInput= 'C:\SEM 3\Agile\9\Sprint3\errorGedcom.ged'
main(fileInput)
