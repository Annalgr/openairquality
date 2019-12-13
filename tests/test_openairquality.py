import unittest
import sys
sys.path.append('..')

from pypackage.openairquality import list_csv
import os

class TestCsvCreation(unittest.TestCase):


    def setUp(self):
        self.temporary_file = "/tmp/emptyfile"
        f = open (self.temporary_file, 'w')
        f.close()
        
        
    def test_no_file(self):
        e_list = list_csv("/tmp/idonotexist")
        self.assertFalse(e_list)


    def test_empty_file(self):
        e_list = list_csv(self.temporary_file)
        self.assertFalse(e_list)


    def tearDown(self):
        os.remove(self.temporary_file)
        
