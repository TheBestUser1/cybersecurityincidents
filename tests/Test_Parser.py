import sys
import os
import unittest


PARENT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.realpath(__file__))
sys.path.append(PARENT_DIR)

from Parser import *

class ParserTest1(unittest.TestCase):
    def setUp(self):
        self.test_method = Parser.extractDomain
    
    def test_negative(self):
        container = "www.filelist.io"
        key = self.test_method(container)
        message = f"www is not {container}"
        self.assertIn(key,container,message)
    

if __name__=='__main__':
    unittest.main()
    