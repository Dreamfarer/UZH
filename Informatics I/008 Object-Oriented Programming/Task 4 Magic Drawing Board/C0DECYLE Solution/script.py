#!/usr/bin/env python3

from typing import Tuple, List

class MagicDrawingBoard:

    def __init__(self, width: int, height: int):
        self.__invalid_dimensions_test(width, height)
        self.__width: int = width
        self.__height: int = height
        self.__board: List[List[str]] = [["0"] * width for i in range(height)]

    def pixel(self, position: Tuple[int, int]) -> None:
        self.__out_of_bounds_test(position)
        self.__draw(position)

    def rect(self, left_top: Tuple[int, int], right_bottom: Tuple[int, int]) -> None:
        self.__out_of_bounds_test(left_top)
        self.__out_of_bounds_test((right_bottom[0] - 1, right_bottom[1] - 1))
        self.__not_positive_difference_test(left_top, right_bottom)
        for y in range(left_top[1], right_bottom[1]):
            for x in range(left_top[0], right_bottom[0]):
                self.__draw((x, y))

    def img(self) -> str:
        return "\n".join(["".join(row) for row in self.__board])

    def reset(self) -> None:
        for y in range(self.__height):
            for x in range(self.__width):
                self.__draw((x, y), "0")

    def __invalid_dimensions_test(self, width: int, height: int) -> None:
        if width < 1 or height < 1:
            raise Warning("invalid dimensions")

    def __out_of_bounds_test(self, position: Tuple[int, int]) -> None:
        if position[0] < 0 or position[0] >= self.__width or position[1] < 0 or position[1] >= self.__height:
            raise Warning("position out of bounds")

    def __not_positive_difference_test(self, left_top: Tuple[int, int], right_bottom: Tuple[int, int]) -> None:
        if right_bottom[0] <= left_top[0] or right_bottom[1] <= left_top[1]:
            raise Warning("not positive difference")

    def __draw(self, position: Tuple[int, int], value: str = "1") -> None:
        self.__board[position[1]][position[0]] = value

