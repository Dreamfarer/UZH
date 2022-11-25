#!/usr/bin/env python3

from public.character import Character

class Knight(Character):

    def _get_caused_dmg(self, other: Character) -> int:
        return round(super()._get_caused_dmg(other) * 0.8)

    def _take_physical_damage(self, amount: int) -> None:
        super()._take_physical_damage(round(amount * 0.75))
