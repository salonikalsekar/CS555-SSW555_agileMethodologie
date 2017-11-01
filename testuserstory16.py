 
import unittest
import userStory16

class Test(unittest.TestCase):
    def test_samename(self):
       malename = 'Roberts' is 'Roberts' 
       if(self.assertTrue(malename)):
           print("True")
        
    def test_diffname(self):
        malename = 'Roberts' is 'Max'
        if(self.assertFalse(malename)):
            print("False")



            

              

unittest.main()
