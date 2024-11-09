from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area_calculator(self):
        pass



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area_calculator(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
    def area_calculator(self):
        return self.width * self.heigth


class calcArea (Shape):
    def area_calculator(self):
        return self.area_calculator()



circle_1 = Circle(3)
print(calcArea.area_calculator(circle_1))