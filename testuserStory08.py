
import unittest
import userStory08

class Test(unittest.TestCase):
    def test_age(self):
       age = (0 is 1)
       if(self.assertFalse(age)):
           print("True")
        
    def test_two(self):
       self.assertEqual("23 August 1990","23 August 1990")

    def test_three(self):
        age = 10
        d2 = (age < 1)
        if(self.assertFalse(d2)):
          print("True")

    def test_four(self):
        list1 = []
        self.assertNotEqual(userStory08.birthAfterMarriageofParents,list1)
          

unittest.main()
