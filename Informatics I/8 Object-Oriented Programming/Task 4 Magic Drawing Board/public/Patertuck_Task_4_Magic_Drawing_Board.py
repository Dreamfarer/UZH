#!/usr/bin/env python3

class MagicDrawingBoard:
    def __init__(self, x=int, y=int):

        if not (isinstance(x, int) or isinstance(y, int)):
            raise Warning("Invalid Input Type for MagicDrawingBoard, needs to be a tuple of 2 integers")

        if x < 1 or y < 1:
            raise Warning("Invalid Dimensions for Drawing Board")

        self.__x = x
        self.__y = y
        self.__picture = []
        self.reset()

    def pixel(self, coordinates):

        if coordinates[0] < 1 or coordinates[1] < 1 or coordinates[0] > self.__x or coordinates[1] > self.__y:
            raise Warning("Coordinates out of range of drawing board")

        self.__picture[coordinates[1]] = self.__picture[coordinates[1]][:coordinates[0]] + "1" + \
                                         self.__picture[coordinates[1]][coordinates[0] + 1:]

    # Returns a string of the drawing board
    def img(self):
        string = str()

        for line in self.__picture:
            string += line + '\n'
        return string.strip()

    def reset(self):
        self.__picture = list()

        for _ in range(0, self.__y):
            self.__picture.append("0" * self.__x)

    def rect(self, cord1, cord2):

        # raise Warning for invalid cord1 and cord2 types
        if not (isinstance(cord1[0], int) or isinstance(cord1[1], int) or
                isinstance(cord2[0], int) or isinstance(cord2[1], int)):
            raise Warning("Coordinates for rectangle must be a tuple of integers")

        # Raise Warning for 0 or negative coordinates
        if cord1[0] < 0 or cord1[1] < 0:
            raise Warning("Coordinates for rectangle must be bigger than 0!")

        # raise Warning for invalid square input
        if cord1[0] >= cord2[0] or cord1[1] >= cord2[1]:
            raise Warning("Invalid Square Input! Second coordinate needs to be to the bottom right of the first "
                          "coordinate.")

        # Raise Warning for square being bigger than the magic board
        if cord2[0] > self.__x or cord2[1] > self.__y:
            raise Warning("Square Input bigger than Magic Board")

        for line in range(cord1[1], cord2[1]):
            self.__picture[line] = self.__picture[line][:cord1[0]] + "1" * (cord2[0] - cord1[0]) + \
                                   self.__picture[line][cord2[0]:]


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
db = MagicDrawingBoard(6, 4)  # instantiation of a specific size
db.pixel((1,1)) # draw at one coordinate
db.rect((2, 2), (3, 4))  # draw a rectangle
img = db.img()  # return the drawn image
print(img)
db.reset() # reset the field again
img = db.img()
print("")
print(img)
