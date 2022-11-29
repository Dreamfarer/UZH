#!/usr/bin/env python3

from public.character import Character

class Mage(Character):

    def attack(self, other: Character) -> None:
        assert isinstance(other, Character)
        assert self is not other

        if not self.is_alive():
            raise Warning("Character is dead!")

        other._take_magical_damage(self._get_caused_dmg(other))

    def _get_caused_dmg(self, other: Character) -> int:
        return round(super()._get_caused_dmg(other) * 1.25)

    def _take_physical_damage(self, amount: int) -> None:
        super()._take_physical_damage(round(amount * 1.5))

    def _take_magical_damage(self, amount: int) -> None:
        super()._take_magical_damage(round(amount * 1.5))
