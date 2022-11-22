#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from public.knight import Knight
from public.mage import Mage
from public.rogue import Rogue

def attack(c1, c2):
    print("{} attacks {} ".format(c1, c2), end="")

    if not c2.is_alive():
        print("{} is beating a dead horse!".format(c1.get_name()))
        return

    life_before = c2.get_health()[0]
    c1.attack(c2)
    life_after = c2.get_health()[0]
    dmg = life_before-life_after

    print("and hits for {} damage. ".format(dmg), end="")

    if c2.is_alive():
        life = c2.get_health()
        perc = round(100 * life[0] / life[1], 1)
        print("{} still has {} ({}%) health".format(c2.get_name(), life[0], perc))
    else:
        print("{} died!".format(c2.get_name()))

k = Knight("Arthur", 12)
m = Mage("Gandalf", 12)
r = Rogue("Shades", 11)

attack(r, m)
attack(m, r)
attack(k, m)

attack(r, m)
attack(m, k)
attack(k, m) # Gandalf dies
attack(r, m)  # Shades is attacking a dead character

while r.is_alive() and k.is_alive():
    attack(r, k)
    if k.is_alive():
        attack(k, r)

winner = r.get_name() if r.is_alive() else k.get_name()
print("{} wins the battle!".format(winner)) # Arthur
