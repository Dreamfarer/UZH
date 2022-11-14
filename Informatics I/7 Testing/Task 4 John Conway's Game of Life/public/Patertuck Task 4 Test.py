#!/usr/bin/env python3
from unittest import TestCase
from Patertuck_Task_4_Game_of_Life import evolve


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

    def test_glider(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
                        "--------------",
                        "| ###        |",
                        "| #          |",
                        "|  #         |",
                        "|            |",
                        "|            |",
                        "--------------"
                    ), 5)
        actual = evolve(field, 4)
        self.assertEqual(actual, expected)

    def test_world_is_tuple_of_strings(self):
        with self.assertRaises(Warning):
            evolve((5, 5, 3), 5)

    def test_world_wrong_character1(self):
        field = (
            "--X-----------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 5)

    def test_world_wrong_character2(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #   L     |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 5)

    def test_world_wrong_character3(self):
        field = (
            "--------------",
            "|    -       |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 5)

    def test_world_wrong_character4(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #       | |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 5)

    def test_world_wrong_character5(self):
        field = (
            "--------------",
            "             |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 5)

    def test_different_lengths1(self):
        field = (
            "---------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 5)

    def test_different_lengths2(self):
        field = (
            "--------------",
            "|            |",
            "|  ##      |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 5)

    def test_different_lengths3(self):
        field = (
            "---------------",
            "|            |",
            "|  ###  #     |",
            "|  #         |",
            "|   #        |",
            "|          #  |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 5)

    def test_different_lengths4(self):
        field = (
            "---------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 5)

    def test_smaller_than_3_by_3(self):
        field = (
            "--",
            "||",
            "--"
        )
        with self.assertRaises(Warning):
            evolve(field, 5)

    def test_steps_positive_int1(self):
        field = (
            "--------------",
            "|            |",
            "|  ##        |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, -3)

    def test_steps_positive_int2(self):
        field = (
            "--------------",
            "|            |",
            "|  ##        |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, "5")

    def test_empty_world(self):
        field = ()
        with self.assertRaises(Warning):
            evolve(field, "5")

    def test_empty_world2(self):
        field = (
            "-----",
            "-----"
        )
        with self.assertRaises(Warning):
            evolve(field, 5)

    def test_wrong_input(self):
        field = (
            "---",
            "|X|",
            "---"
        )
        with self.assertRaises(Warning):
            evolve(field, "5")



