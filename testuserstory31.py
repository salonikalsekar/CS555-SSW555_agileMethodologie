import unittest
import userStory31

class TestUserStoriestwo(unittest.TestCase):
    
    def testnamesone(self):
        list2 = ['Roberts','Jack','Alia']
        self.assertNotEqual(userStory31.listLivingSingle,list2)
        
    
    def testnamestwo(self):
        list1 = []
        self.assertTrue(userStory31.listLivingSingle is not list1)

unittest.main()        
