"""
Perform unittest on a single function of the main code.
Testing: valid, invalid, inexistent, and empty input.
"""

import unittest
import sys
import os
sys.path.append('..')
from pypackage.openairquality import list_csv


class TestCsvCreation(unittest.TestCase):
    """Perform unittest on the list_csv function."""

    def setUp(self):
        """Set the environment:
           create a temporary empty file.
        """
        self.temporary_file = "/tmp/emptyfile"
        f = open(self.temporary_file, 'w')
        f.close()

    def test_valid_file(self):
        """Pass to list_csv a valid csv file."""
        e_list = list_csv("eu.csv")
        self.assertTrue(e_list)

    def test_no_file(self):
        """Pass to list_csv an inexistent file."""
        e_list = list_csv("/tmp/idonotexist")
        self.assertFalse(e_list)

    def test_invalid_file(self):
        """Pass to list_csv a jpg invalid file."""
        e_list = list_csv("ibelieveinmyself.jpg")
        self.assertFalse(e_list)

    def test_empty_file(self):
        """Pass to list_csv an empty file."""
        e_list = list_csv(self.temporary_file)
        self.assertFalse(e_list)

    def tearDown(self):
        """Remove the temporary file."""
        os.remove(self.temporary_file)
