from classes.Shape import Shape
from classes.Circle import Circle
from classes.Square import Square

for area in [Square(3), Circle(3)]:
    print(area.area())
