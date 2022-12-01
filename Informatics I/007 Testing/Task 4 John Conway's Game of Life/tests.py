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
    def test_evolve_1_perytron(self):
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
    
    def test_evolve_2_perytron(self):
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
    def test_unequal_line_lengths_perytron(self):
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
    def test_smaller_than_3x3_perytron(self):
        world = (
            "--",
            "--"
        )
        self.assertRaises(Warning, evolve, world, 2)

    # Wrong position of characters
    def test_invalid_character_placement_1_perytron(self):
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
    def test_invalid_character_placement_2_perytron(self):
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
    def test_not_tuple_perytron(self):
        self.assertRaises(Warning, evolve, None, 2)

    # Invalid steps
    def test_not_integer_perytron(self):
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
    def test_invalid_characters_perytron(self):
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
    def test_empty_world_perytron(self):
        world = ()
        self.assertRaises(Warning, evolve, world, 2)

    # def test_empty_world_paul(self):
    #     world = ()
    #     actual = evolve(world, 4)
    #     expected = "Warning, empty tuple"
    #     self.assertEquals(expected, actual,f"Expected {expected} but instead {actual}")

    # Tests to check if evolve does the right thing

    def test_evolve_step4_paul(self):
        world = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #        |",
            "|    #       |",
            "|            |",
            "--------------"
        )
        actual = evolve(world, 4)
        expected = (
            (
                "--------------",
                "|  ###       |",
                "|  #         |",
                "|   #        |",
                "|            |",
                "|            |",
                "--------------"
            ),
            5
        )
        self.assertEquals(expected, actual, f"Expected {expected} but instead {actual}")

    def test_evolve_step1_paul(self):
        world = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #        |",
            "|    #       |",
            "|            |",
            "--------------"
        )
        actual = evolve(world, 1)
        expected = (
            (
                "--------------",
                "|    #       |",
                "|   ##       |",
                "|   # #      |",
                "|            |",
                "|            |",
                "--------------"
            ),
            5
        )
        self.assertEquals(expected, actual, f"Expected {expected} but instead {actual}")

    def test_evolve_step2_paul(self):
        world = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #        |",
            "|    #       |",
            "|            |",
            "--------------"
        )
        actual = evolve(world, 2)
        expected = (
            (
                "--------------",
                "|   ##       |",
                "|   # #      |",
                "|   #        |",
                "|            |",
                "|            |",
                "--------------"
            ),
            5
        )
        self.assertEquals(expected, actual, f"Expected {expected} but instead {actual}")

    def test_evolve_step3_paul(self):
        world = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #        |",
            "|    #       |",
            "|            |",
            "--------------"
        )
        actual = evolve(world, 3)
        expected = (
            (
                "--------------",
                "|   ##       |",
                "|  ##        |",
                "|    #       |",
                "|            |",
                "|            |",
                "--------------"
            ),
            5
        )
        self.assertEquals(expected, actual, f"Expected {expected} but instead {actual}")

    def test_evolve_1_paul(self):
        topass = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        actual = evolve(topass, 4)
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
        self.assertEquals(expected, actual, f"Expected {expected} but instead {actual}")

    def test_evolve_2_paul(self):
        topass = (
            "--------------",
            "|            |",
            "|            |",
            "--------------"
        )
        actual = evolve(topass, 4)
        expected = (
            (
                "--------------",
                "|            |",
                "|            |",
                "--------------"
            ),
            0
        )
        self.assertEquals(expected, actual, f"Expected {expected} but instead {actual}")

    def test_evolve_3_paul(self):
        topass = (
            "--------------",
            "|#           |",
            "|            |",
            "--------------"
        )
        actual = evolve(topass, 4)
        expected = (
            (
                "--------------",
                "|            |",
                "|            |",
                "--------------"
            ),
            0
        )
        self.assertEquals(expected, actual, f"Expected {expected} but instead {actual}")



    def test_glider_patertuck(self):
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

    def test_world_is_tuple_of_strings_patertuck(self):
        with self.assertRaises(Warning):
            evolve((5, 5, 3), 5)

    def test_world_wrong_character1_patertuck(self):
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

    def test_world_wrong_character2_patertuck(self):
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

    def test_world_wrong_character3_patertuck(self):
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

    def test_world_wrong_character4_patertuck(self):
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

    def test_world_wrong_character5_patertuck(self):
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

    def test_different_lengths1_patertuck(self):
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

    def test_different_lengths2_patertuck(self):
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

    def test_different_lengths3_patertuck(self):
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

    def test_different_lengths4_patertuck(self):
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

    def test_smaller_than_3_by_3_patertuck(self):
        field = (
            "--",
            "||",
            "--"
        )
        with self.assertRaises(Warning):
            evolve(field, 5)

    def test_steps_positive_int1_patertuck(self):
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

    def test_steps_positive_int2_patertuck(self):
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

    def test_empty_world_patertuck(self):
        field = ()
        with self.assertRaises(Warning):
            evolve(field, "5")

    def test_empty_world2_patertuck(self):
        field = (
            "-----",
            "-----"
        )
        with self.assertRaises(Warning):
            evolve(field, 5)

    def test_wrong_input_patertuck(self):
        field = (
            "---",
            "|X|",
            "---"
        )
        with self.assertRaises(Warning):
            evolve(field, "5")

