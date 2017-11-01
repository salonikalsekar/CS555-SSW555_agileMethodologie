import unittest
import userStory03
import userStory04

class TestStringMethods(unittest.TestCase):
	
    def test1(self):
        self.assertTrue(len(userStory03.individualList()) is not 0)
    
    def test5(self):
        self.assertFalse(len(userStory04.familyList()) is 0)
		
	
		

unittest.main()
