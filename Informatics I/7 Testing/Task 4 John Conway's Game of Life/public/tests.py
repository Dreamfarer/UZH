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

    def test_evolve1(self):
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
                "| ###        |",
                "| #          |",
                "|  #         |",
                "|            |",
                "|            |",
                "--------------"
            ),
            5
        )
        #self.assert...

