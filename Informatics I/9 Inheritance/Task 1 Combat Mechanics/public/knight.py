#!/usr/bin/env python3

# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from public.character import Character

class Knight(Character):

    # Ovveride attack
    def attack(self, other):
        assert isinstance(other, Character)
        assert self is not other

        if not self.is_alive():
            raise Warning("Character is dead!")

        # Deal 20% less physical damage to the opponent
        other._take_physical_damage(round(self._get_caused_dmg(other) * 0.80))

    # Ovveride physical defense
    def _take_physical_damage(self, amount):
        assert isinstance(amount, int)
        assert amount >= 0

        # Reduce received physical damage by 25%
        self._health_cur = max(0, round(self._health_cur - amount * 0.75))
