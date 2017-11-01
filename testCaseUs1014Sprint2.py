import unittest
import userStory10
import userStory14

class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertTrue(userStory10.marriageAfter14 is not 0)
    def test2(self):
        s = userStory14.multipleBirthslessThan5
        self.assertGreaterEqual(s, 5)
        		
unittest.main()
