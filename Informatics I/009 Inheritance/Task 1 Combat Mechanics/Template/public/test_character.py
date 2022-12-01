#!/usr/bin/env python3

# This is the unit test suite that has been created for the
# Character class. Investigate the different tests to learn
# about testing strategies and use it as documentation.

from unittest import TestCase
from public.character import Character

class TestCharacter(TestCase):

    def test_getters(self):
        sut = Character("C", 1)
        self.assertEqual("C", sut.get_name())
        self.assertEqual(1, sut.get_lvl())
        self.assertEqual((50, 50), sut.get_health())

    def test_repr(self):
        actual = repr(Character("C", 1))
        expected = "C (Character, 1, 50/50)"
        self.assertEqual(expected, actual)

    def test_invalid_name(self):
        with self.assertRaises(AssertionError):
            Character("", 1)

    def test_invalid_level(self):
        with self.assertRaises(AssertionError):
            Character("C", 0)

    def test_correct_health_scaling(self):
        sut = Character("C", 2)
        self.assertEqual((100, 100), sut.get_health())

    def test_take_physical_damage(self):
        sut = MockCharacter("C", 2)
        sut.physical_dmg(13)
        self.assertEqual((87, 100), sut.get_health())

    def test_take_magical_damage(self):
        sut = MockCharacter("C", 2)
        sut.magical_dmg(27)
        self.assertEqual((73, 100), sut.get_health())

    def test_attack_is_delegated(self):
        sut = Character("C", 1)
        other = MockCharacter("C", 1)
        sut.attack(other)
        self.assertEqual([10], other.physical_taken)

    def test_attacker_does_not_get_dmg(self):
        sut = MockCharacter("C", 1)
        sut.attack(Character("D", 1))
        self.assertEqual([], sut.physical_taken)

    def test_dmg_is_correct(self):
        sut = MockCharacter("C", 1)
        actual = sut.get_caused_dmg(Character("o", 1))
        expected = 10
        self.assertEqual(expected, actual)

    def test_dmg_scaling(self):
        sut = MockCharacter("C", 2)
        actual = sut.get_caused_dmg(Character("o", 2))
        expected = 20
        self.assertEqual(expected, actual)

    def test_dmg_lvl_diff_neg(self):
        sut = MockCharacter("C", 3)
        actual = sut.get_caused_dmg(Character("o", 4))
        expected = 29
        self.assertEqual(expected, actual)

    def test_dmg_lvl_diff_pos(self):
        sut = MockCharacter("C", 4)
        actual = sut.get_caused_dmg(Character("o", 2))
        expected = 42
        self.assertEqual(expected, actual)

    def test_dmg_lvl_huge_diff(self):
        sut = MockCharacter("C", 1)
        actual = sut.get_caused_dmg(Character("o", 100))
        expected = 1
        self.assertEqual(expected, actual)

    def test_taken_physical_dmg_must_be_int(self):
        with self.assertRaises(AssertionError):
            MockCharacter("C", 1).physical_dmg(12.3)

    def test_taken_physical_dmg_must_be_positive(self):
        with self.assertRaises(AssertionError):
            MockCharacter("C", 1).physical_dmg(-1)

    def test_taken_magical_dmg_must_be_int(self):
        with self.assertRaises(AssertionError):
            MockCharacter("C", 1).magical_dmg(12.3)

    def test_taken_magical_dmg_must_be_positive(self):
        with self.assertRaises(AssertionError):
            MockCharacter("C", 1).magical_dmg(-1)

    def test_no_negative_health_physical(self):
        sut = MockCharacter("C", 1)
        sut.physical_dmg(100)
        self.assertEqual((0, 50), sut.get_health())

    def test_no_negative_health_magical(self):
        sut = MockCharacter("C", 1)
        sut.magical_dmg(100)
        self.assertEqual((0, 50), sut.get_health())

    def test_is_alive(self):
        sut = MockCharacter("C", 1)
        self.assertTrue(sut.is_alive())
        sut.physical_dmg(100)
        self.assertFalse(sut.is_alive())

    def test_dead_chars_cannot_attack(self):
        sut = MockCharacter("C", 1)
        sut.physical_dmg(100)
        with self.assertRaises(Warning):
            sut.attack(Character("B", 2))

    def test_chars_cannot_attack_themselves(self):
        sut = Character("C", 1)
        with self.assertRaises(AssertionError):
            sut.attack(sut)

    def test_chars_cannot_attack_non_characters(self):
        sut = Character("C", 1)
        with self.assertRaises(AssertionError):
            sut.attack(1)


class MockCharacter(Character):
    """This mock class is used to expose protected methods for testing and
    also to capture the damage taken to simplify test assertions."""

    def __init__(self, name, lvl):
        super().__init__(name, lvl)
        self.physical_taken = []
        self.magical_taken = []

    def get_caused_dmg(self, other):
        return self._get_caused_dmg(other)

    def _take_physical_damage(self, amount):
        self.physical_taken.append(amount)
        super()._take_physical_damage(amount)

    def _take_magical_damage(self, amount):
        self.magical_taken.append(amount)
        super()._take_magical_damage(amount)

    def physical_dmg(self, amount):
        self._take_physical_damage(amount)

    def magical_dmg(self, amount):
        self._take_magical_damage(amount)
