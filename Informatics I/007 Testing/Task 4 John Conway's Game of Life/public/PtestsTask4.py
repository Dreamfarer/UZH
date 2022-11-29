#!/usr/bin/env python3
from unittest import TestCase
from script import evolve


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
    
    
        
    # def test_empty_world(self):
    #     world = ()
    #     actual = evolve(world, 4)
    #     expected = "Warning, empty tuple"
    #     self.assertEquals(expected, actual,f"Expected {expected} but instead {actual}")
    
    
    
    
    
    #Tests to check if evolve does the right thing    
    
    
    def test_evolve_step4(self):
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
        self.assertEquals(expected, actual,f"Expected {expected} but instead {actual}")
        
        
    def test_evolve_step1(self):
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
        self.assertEquals(expected, actual,f"Expected {expected} but instead {actual}")
        
    def test_evolve_step2(self):
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
        self.assertEquals(expected, actual,f"Expected {expected} but instead {actual}")
        
        
    def test_evolve_step3(self):
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
        self.assertEquals(expected, actual,f"Expected {expected} but instead {actual}")

    def test_evolve_1(self):
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
        self.assertEquals(expected, actual,f"Expected {expected} but instead {actual}")


    def test_evolve_2(self):
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
        self.assertEquals(expected, actual,f"Expected {expected} but instead {actual}")
        
        
    def test_evolve_3(self):
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
        self.assertEquals(expected, actual,f"Expected {expected} but instead {actual}")

























# #Tests to check if input is valid
#     def test_evolve_invalid_input1(self):
#         world = (
#             "--------------",
#             "|            |",
#             "|   ###      |",
#             "|   *        |",
#             "|    #       |",
#             "|            |",
#             "--------------"
#         )
        
#         self.assertRaises(Warning("Invalid char"), evolve, world)
        
        
#     def test_evolve_invalid_input2(self):
#         world = (
#             "-------------",
#             "|            |",
#             "|   ###      |",
#             "|   #        |",
#             "|    #       |",
#             "|            |",
#             "--------------"
#         )
#         actual = evolve(world, 4)
#         self.assertRaises(Warning("Unequal length"), evolve, world)
        
        
#     def test_evolve_invalid_input3(self):
#         world = (
#             "--------------",
#             "--------------"
#         )
#         actual = evolve(world, 4)
        
#         self.assertRaises(Warning("Not sensible size"), evolve, world)
    
#     def test_evolve_invalid_input4(self):
#         world = (
#             "--",
#             "||",
#             "||",
#             "--"
#         )
#         actual = evolve(world, 4)
        
#         self.assertRaises(Warning("Not sensible size"), evolve, world)
        
#     def test_evolve_invalid_input5(self):
#         world = (
#             "--------------",
#             "|            |",
#             "|   ###      |",
#             "|   #        |",
#             "|    #       |",
#             "|            |",
#             "--------------"
#         )
#         actual = evolve(world, -1)
        
#         self.assertRaises(Warning("negative int input"), evolve, world)
        
    
    
    
    
    
    
    
    
        
        
    
    
    
      