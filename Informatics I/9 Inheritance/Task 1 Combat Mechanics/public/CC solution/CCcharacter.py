#!/usr/bin/env python3

from __future__ import annotations
from typing import Tuple

class Character:

    def __init__(self, name: str, lvl: int):
        assert isinstance(name, str)
        assert isinstance(lvl, int)
        assert lvl > 0
        assert name
        self._name: str = name
        self._lvl: int = lvl
        self._health_max: int = lvl*50
        self._health_cur: int = self._health_max

    def __repr__(self):
        s = "{} ({}, {}, {}/{})"
        return s.format(self._name, type(self).__name__, self._lvl, self._health_cur, self._health_max)

    def get_name(self) -> str:
        return self._name

    def get_lvl(self) -> int:
        return self._lvl

    def get_health(self) -> Tuple[int, int]:
        return self._health_cur, self._health_max

    def attack(self, other: Character) -> None:
        assert isinstance(other, Character)
        assert self is not other

        if not self.is_alive():
            raise Warning("Character is dead!")

        other._take_physical_damage(self._get_caused_dmg(other))

    def _get_caused_dmg(self, other: Character) -> int:
        return max(1, self._lvl * 11 - other._lvl)

    def _take_physical_damage(self, amount: int) -> None:
        assert isinstance(amount, int)
        assert amount >= 0
        self._health_cur = max(0, self._health_cur - amount)

    def _take_magical_damage(self, amount: int) -> None:
        assert isinstance(amount, int)
        assert amount >= 0
        self._health_cur = max(0, self._health_cur - amount)

    def is_alive(self) -> bool:
        return self._health_cur > 0

