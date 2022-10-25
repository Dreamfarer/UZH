#!/usr/bin/env python3

from unittest import TestCase
from public.script import process_data
import os

INPUT_FILE = "public/my_data.txt"
OUTPUT_FILE = "public/my_data_processed.txt"

class PublicTestSuite(TestCase):

    # This function is called before each test to remove any existing output file
    def setUp(self):
        if os.path.exists(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)

    def test_example_file(self):
        process_data(INPUT_FILE, OUTPUT_FILE)
        expected = "Firstname,Lastname\nBeat,Meier\n,\nBarbara,Suter\nRoland,Berger"
        if os.path.exists(OUTPUT_FILE):
            with open(OUTPUT_FILE, "r") as f:
                actual = f.read()
            self.assertEqual(expected, actual)
        else:
            self.fail("No output file exists")

    def test_non_existing_file(self):
        actual = process_data("public/non_existing_file.txt", OUTPUT_FILE)
        expected = False
        self.assertEqual(expected, actual)

