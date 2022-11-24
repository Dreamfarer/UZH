from geometric_object import GeometricObject


class Cylinder(GeometricObject):

    def __init__(self, radius, height, color, filled):
        super().__init__(color=color, filled=filled)
        # turns the radius and height into float if they are ints
        if type(radius) == int:
            self.__radius = float(radius)
        else:
            self.__radius = radius

        if type(height) == int:
            self.__height = float(height)
        else:
            self.__height = height

        if type(self.__radius) != float or type(self.__height) != float:
            raise Warning("Invalid input type for radius or height")

    def get_radius(self):
        radius = float()
        radius = self.__radius
        return radius

    def get_height(self):
        height = float()
        height = self.__height
        return height

    def get_area(self):
        return round(2 * 3.14 * self.__radius * (self.__radius + self.__height), 2)

    def get_volume(self):
        return round(3.14 * self.__radius ** 2 * self.__height, 2)
