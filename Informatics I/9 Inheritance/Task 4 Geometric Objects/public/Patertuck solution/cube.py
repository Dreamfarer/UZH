from geometric_object import GeometricObject


class Cube(GeometricObject):
    def __init__(self, side_length, color, filled):
        super().__init__(color=color, filled=filled)

        # turns the side length into float if it is an int
        if type(side_length) == int:
            self.__side_length = float(side_length)
        else:
            self.__side_length = side_length

        if type(self.__side_length) != float:
            raise Warning("Side length must be float or int")

    def get_side_length(self):
        side_length = float()
        side_length = self.__side_length
        return side_length

    def set_side_length(self, side_length):
        self.__side_length = side_length

    def get_area(self):
        return round(6 * self.__side_length * self.__side_length, 2)

    def get_volume(self):
        return round(self.__side_length ** 3, 2)
