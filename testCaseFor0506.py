import unittest
import userStory05
import userStory06

class Testing(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(userStory05.MarriageBeforeDeath, 0)
        
    def test2(self):
        self.assertIsNone(userStory06.getDeathDate, msg = None)
        
unittest.main()
