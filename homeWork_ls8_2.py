from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def calculate_area(self, radius):
        self.radius = radius
        area = 3.14 * (self.radius ** 2)
        print(f"Площа даного кола {area}")

class Rectangle(Shape):

    def calculate_area(self, width, height):
        self.width = width
        self.height = height
        area = self.width * self.height
        print(f'Плща даного прямокутника {area}')


class Triangle(Shape):

    def calculate_area(self, storona, vysota):
        self.storona = storona
        self.vysota = vysota
        area = self.storona / 2 * self.vysota
        print(f'Площа трикутника {area}')

c1 = Circle()
r1 = Rectangle()
t1 = Triangle()

c1.calculate_area(15)
r1.calculate_area(5, 5)
t1.calculate_area(10, 12)

