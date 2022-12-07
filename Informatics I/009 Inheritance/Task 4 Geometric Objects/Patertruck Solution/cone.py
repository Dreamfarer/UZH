from geometric_object import GeometricObject


class Cone(GeometricObject):

    def __init__(self, radius=float, vertical_height=float, slant_height=float, color=str, filled=bool):
        super().__init__(color=color, filled=filled)
        
        # turns the radius, vertical height and slant_height into floats if they are valid int
        if type(radius) == int:
            self.__radius = float(radius)
        else:
            self.__radius = radius

        if type(vertical_height) == int:
            self.__vertical_height = float(vertical_height)
        else:
            self.__vertical_height = vertical_height

        if type(slant_height) == int:
            self.__slant_height = float(slant_height)
        else:
            self.__slant_height = slant_height

        # error for invalid input type
        if type(self.__radius) != float or type(self.__slant_height) != float or type(self.__vertical_height) != float:
            raise Warning("Invalid input type")

    def get_radius(self):
        radius = float()
        radius = self.__radius
        return radius

    def get_vertical_height(self):
        vertical_height = float()
        vertical_height = self.__vertical_height
        return vertical_height

    def get_slant_height(self):
        slant_height = float()
        slant_height = self.__slant_height
        return slant_height

    def get_area(self):
        return round(3.14 * (self.__radius * self.__radius) + (3.14 * self.__radius * self.__slant_height), 2)

    def get_volume(self):
        return round((1 / 3) * 3.14 * (self.__radius ** 2) * self.__vertical_height, 2)
