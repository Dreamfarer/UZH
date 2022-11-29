#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from public.cone import Cone
from public.cube import Cube

# Create first cone object
cone_1 = Cone(2, 4, 2, "red", True)
# Create another cone object
cone_2 = Cone(5.64, 4.2, 8.7, "black", False)
# Create a cube object
cube = Cube(7.2, "white", True)

print(f"Color of the cube object is: {cube.get_color()}")
# Update cube color
cube.set_color("yellow")
# See if the color of cube object is changed
print(f"Color of the cube object is: {cube.get_color()}")

# See the area and volume of the cone_1
print(
    f"cone_1 area is: {cone_1.get_area()} cone_2 volume is: {cone_1.get_volume()}")
