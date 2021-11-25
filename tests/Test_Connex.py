import sys
import os
import unittest




PARENT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.realpath(__file__))
sys.path.append(PARENT_DIR)

from Connex import *
from Parser import *

class AddTest(unittest.TestCase):
   def setUp(self):
      # initialization code for the testcase/testsuite can be added here
    self.test_class = Connex("https://www.google.com")
    

   def test_positive(self):    
    self.assertEqual(self.test_class.check_connection(),200)

   def test_negative_values(self):
    self.assertNotEqual(self.test_class.check_connection(), 404) 
   
   def test_negative(self):
      
        # error message in case if test case got failed
      message = "given object is not instance of Parser."
        # assertIsInstance() to check if obj is instance of class
      self.assertIsInstance(self.test_class, Parser, message)

   def tearDown(self):
      # Deinit and cleanup should be done here
    pass   
    
class AddTest_2(unittest.TestCase):
   def setUp(self):
      self.test_class = Connex("http://google")
   
   def test_positive(self):
      self.assertEqual(self.test_class.check_connection(),200)

   def test_negative_values(self):
      self.assertNotEqual(self.test_class.check_connection(),404)

   def test_negative(self):
      
        # error message in case if test case got failed
      message = "given object is not instance of Connex."
        # assertIsInstance() to check if obj is instance of class
      self.assertIsInstance(self.test_class, Connex, message)


   def tearDown(self):
      # Deinit and cleanup should be done here
    pass       
if __name__=='__main__':
    unittest.main()