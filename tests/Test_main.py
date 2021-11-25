import sys
import os
import unittest


PARENT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.realpath(__file__))
sys.path.append(PARENT_DIR)

from main import *

class MainTest1(unittest.TestCase):
    def setUp(self):
        self.test_class =Scrapper_Soup("WebScrapper")

    def test_regex(self):
        ErrorMessage = "Did not return right result for link format"
        url = "http://www.youtube.com"
        class_answer = self.test_class.check_for_formating(url)
        self.assertTrue(class_answer,ErrorMessage) 
    
    def test_class(self):
        message = "given object is not instance of Scrapper_Soup."
        # assertIsInstance() to check if obj is instance of class
        self.assertIsInstance(self.test_class, Scrapper_Soup, message)

    def test_singleton(self):
        message = "given object is not the same instantiated."
        self.assertRaises("This class is singleton", Scrapper_Soup("test"))
