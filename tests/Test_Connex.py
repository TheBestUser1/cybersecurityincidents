import sys
import os
import unittest


PARENT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.realpath(__file__))
sys.path.append(PARENT_DIR)

from Connex import *

class AddTest(unittest.TestCase):
   def setUp(self):
      # initialization code for the testcase/testsuite can be added here
    self.test_class = Connex("https://www.google.com")

   def test_addition(self):    
    self.assertEqual(self.test_class.check_connection(),200)
    self.assertNotEqual(self.test_class.check_connection(), 404)

   def test_negative_values(self):
    self.assertNotEqual(self.test_class.check_connection(), 404) 

   def tearDown(self):
      # Deinit and cleanup should be done here
    pass   
    
if __name__=='__main__':
    unittest.main()