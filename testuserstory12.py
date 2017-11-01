
import unittest
import userStory12

class Test(unittest.TestCase):
    def test_age(self):
       age = (0 is 1)
       if(self.assertFalse(age)):
           print("True")
     
    
    def test_two(self):
        age = 70
        d3 = (age < 50)
        if(self.assertFalse(d3)):
            print("True")

    def test_three(self):
        age = 60
        d2 = (age < 80)
        if(self.assertTrue(d2)):
          print("True")

            

              

unittest.main()

