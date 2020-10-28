class shape:

    def __init__(self, colour):
        self.__colour = colour

    def get_colour(self):
        return self.__colour


class Rectangle(shape):

    def __init__(self, colour, height, width):
        shape.__init__(self, colour)
        self.width = width
        self.height = height

    def calculate_area(self):
        self.area = self.width * self.height
        return self.area

    @property
    def colour(self):
        return shape.get_colour(self)

class Triangle(shape):

    def __init__(self, colour, height, width):
        shape.__init__(self, colour)
        self.width = width
        self.height = height

    def calculate_area(self):
        self.area = self.width * self.height / 2

        return self.area

    @property
    def colour(self):
        return shape.get_colour(self)
    

rec1 = Rectangle("red", 4, 5)
print(rec1.colour)
print(rec1.calculate_area())
tri1 = Triangle("blue", 6, 8)
print(tri1.colour)
print(tri1.calculate_area()) 