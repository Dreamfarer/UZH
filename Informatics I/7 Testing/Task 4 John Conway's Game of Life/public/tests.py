###############################################################################
# TESTING IN VS CODE
#   First off, you need to navigate your terminal to the current task's folder.
# Copy the following command into the terminal below:
# cd "Informatics I/7 Testing/Task 4 John Conway's Game of Life/"
#   To run the unit tests, copy the following line into the terminal below:
# python -m unittest public/tests.py
###############################################################################

from unittest import TestCase
from public.script import evolve

# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class EvolveTestSuite(TestCase):

    ###########################################################################
    # TEST RESULT
    ###########################################################################
    def test_evolve_1(self):
        world = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        actual = evolve(world, 4)
        expected = (
            (
                "--------------",
                "| ###        |",
                "| #          |",
                "|  #         |",
                "|            |",
                "|            |",
                "--------------"
            ),
            5
        )
        self.assertEqual(expected, actual)
    
    def test_evolve_2(self):
        world = (
            "---",
            "|#|",
            "---",
        )
        actual = evolve(world, 4)
        expected = (
            (
                "---",
                "| |",
                "---",
            ),
            0
        )
        self.assertEqual(expected, actual)

    ###########################################################################
    # CATCH INVALID INPUTS
    ###########################################################################
    
    # Unequal line lengths
    def test_unequal_line_lengths(self):
        world = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #        |",
            "|   ",
            "|            |",
            "--------------"
        )
        self.assertRaises(Warning, evolve, world, 2)
    
    # Smaller than 3x3
    def test_smaller_than_3x3(self):
        world = (
            "--",
            "--"
        )
        self.assertRaises(Warning, evolve, world, 2)

    # Wrong position of characters
    def test_invalid_character_placement_1(self):
        world = (
            "-----|--------",
            "-            |",
            "-   ###      |",
            "|   #        |",
            "|            -",
            "|            |",
            "--------|-----"
        )
        self.assertRaises(Warning, evolve, world, 2)
    
    # Wrong position of characters
    def test_invalid_character_placement_2(self):
        world = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #     |   |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        self.assertRaises(Warning, evolve, world, 2)

    # Invalid state (type-wise)
    def test_not_tuple(self):
        self.assertRaises(Warning, evolve, None, 2)

    # Invalid steps
    def test_not_integer(self):
        world = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        self.assertRaises(Warning, evolve, world, -1)
    
    # Invalid steps
    def test_invalid_characters(self):
        world = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #     6   |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        self.assertRaises(Warning, evolve, world, 2)
    
    # Invalid steps
    def test_empty_world(self):
        world = ()
        self.assertRaises(Warning, evolve, world, 2)


