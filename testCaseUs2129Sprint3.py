import unittest
import userStory21
import userStory29

class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(userStory21.getGenderByID,  'F')
    def test2(self):
        self.assertNotEqual(userStory29.deceasedList, 0)
	   
		
unittest.main()
