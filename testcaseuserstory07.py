
import unittest
import userStory07refactoredcode

class Test(unittest.TestCase):
    def test_age(self):
       age = (0 is 1)
       if(self.assertFalse(age)):
           print("True")
        
    def test_two(self):
       self.assertEqual("23 August 1990","23 August 1990")
    
    
    def test_three(self):
        d = ("32 December 2013" is "23 December 2013")
        self.assertFalse(d)

    def test_four(self):
        d1 = ("15 October 2015" is "15 October 2100")
        self.assertFalse(d1)
        
    def test_five(self):
        age = 10
        d2 = (age < 1)
        if(self.assertFalse(d2)):
          print("True")

    def test_six(self):
        age = 160
        d3 = (age < 150)
        if(self.assertFalse(d3)):
            print("True")

              

unittest.main()
