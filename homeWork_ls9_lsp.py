from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius **2)


class Rectangle(Shape):

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def area(self):
        return self.heigth * self.width


def result (shape):
    print(f'Площа: {shape.area()}')

circ_1 = Circle(5)
rec_1 = Rectangle(10, 4)

result(circ_1)
result(rec_1)