import unittest
import userStory23


class TestUserStories(unittest.TestCase):
    
    def testone(self):
        list1 = ['Roberts','North','Max']
        self.assertNotEqual(userStory23.unique_names_and_birth_dates,list1)

    def testtwo(self):
        self.assertTrue(userStory23.unique_names_and_birth_dates is not 1)


    
unittest.main()        
