	
import unittest
import sprint2


check=(sprint2.fileInput is " ")



class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertNotEqual(sprint2.dateList, " ")
	   
		
    def testFile(self):
        self.assertFalse(check)
	
    def test4(self):
        self.assertTrue(len(sprint2.individualList()) is not 0)
    
    def test5(self):
        self.assertFalse(len(sprint2.familyList()) is 0)
		
	
		

unittest.main()
