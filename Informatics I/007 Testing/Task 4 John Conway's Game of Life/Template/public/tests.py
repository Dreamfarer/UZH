#!/usr/bin/env python3
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

    def test_invalid_world_type(self):
        with self.assertRaises(Warning):
            evolve(2,2)

    def test_invalid_world_dimensions(self):
        with self.assertRaises(Warning):
            evolve((
                "---",
                "---"
            ), 2)

    def test_invalid_world_row_length(self):
        with self.assertRaises(Warning):
            evolve((
                "-----------",
                "|            |",
                "--------",
            ),2)

    def test_invalid_char_in_world(self):
        with self.assertRaises(Warning):
            evolve((
                "----",
                "|A |",
                "|  |",
                "----",
            ),2)

    def test_invalid_position_of_horizontal_bounds_in_world(self):
        with self.assertRaises(Warning):
            evolve((
                "-----",
                "| - |",
                "|   |",
                "-----",
            ),2)

    def test_invalid_position_of_vertical_bounds_in_world(self):
        with self.assertRaises(Warning):
            evolve((
                "-----",
                "|   |",
                "|   |",
                "--|--",
            ), 2)

    def test_invalid_position_of_alive_cell_in_world(self):
        with self.assertRaises(Warning):
            evolve((
                "-#---",
                "|   |",
                "|   |",
                "-----",
            ), 2)

    def test_invalid_position_of_alive_cell_in_world_other(self):
        with self.assertRaises(Warning):
            evolve((
                "-----",
                "|   |",
                "|   #",
                "-----",
            ), 2)

    def test_invalid_position_of_dead_cell_in_world(self):
        with self.assertRaises(Warning):
            evolve((
                "--- -",
                "|   |",
                "|   |",
                "-----",
            ), 2)

    def test_invalid_position_of_dead_cell_in_world_other(self):
        with self.assertRaises(Warning):
            evolve((
                "-----",
                "    |",
                "|   |",
                "-----",
            ), 2)

    def test_invalid_steps_type(self):
        with self.assertRaises(Warning):
            evolve((
                "-----",
                "|   |",
                "|   |",
                "-----",
            ), "2")

    def test_invalid_non_positive_steps(self):
        with self.assertRaises(Warning):
            evolve((
                "-----",
                "|   |",
                "|   |",
                "-----",
            ), -3)

    def test_invalid_zero_steps(self):
        with self.assertRaises(Warning):
            evolve((
                "-----",
                "|   |",
                "|   |",
                "-----",
            ), 0)

    """
    def test_valid_zero_steps(self):
        boilerplate = (
            "-----",
            "| # |",
            "|  #|",
            "-----",
        )
        self.assertEqual((boilerplate, 2), evolve(boilerplate, 0))
    """

    def test_valid_glider(self):
        boilerplate = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        result = (
            "--------------",
            "| ###        |",
            "| #          |",
            "|  #         |",
            "|            |",
            "|            |",
            "--------------"
        )
        self.assertEqual((result, 5), evolve(boilerplate, 4))

