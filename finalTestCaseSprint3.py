import unittest
import sprint3

class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(sprint3.getGenderByID,  'F')
    def test2(self):
        self.assertNotEqual(sprint3.deceasedList, 0)
    def test3(self):
        self.assertTrue(sprint3.marriageAfter14 is not 0)
    def test4(self):
        s = sprint3.multipleBirthslessThan5
        self.assertGreaterEqual(s, 5)
    def test5(self):
        self.assertTrue(len(sprint3.individualList()) is not 0)   
    def test6(self):
        self.assertFalse(len(sprint3.familyList()) is 0)
    def test7(self):
        self.assertNotEqual(sprint3.MarriageBeforeDeath, 0)       
    def test8(self):
        self.assertIsNone(sprint3.getDeathDateByID, msg = None)
    def test_age(self):
       age = (0 is 1)
       if(self.assertFalse(age)):
           print("True")
    def test_two(self):
       self.assertEqual("23 August 1990","23 August 1990")  
    def test_three(self):
        d = ("32 December 2013" is "23 December 2013")
        self.assertFalse(d)
    def test_upper(self):
        self.assertNotEqual(sprint3.dateList, " ")
    def test_lower(self):
        self.assertFalse(len(sprint3.familyList()) is 0)
        	   		
unittest.main()
