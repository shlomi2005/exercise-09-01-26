from classes.Shape import Shape
import math


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi*self.radius ** 2, 2)
