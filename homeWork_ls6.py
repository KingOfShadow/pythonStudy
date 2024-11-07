class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        if self.species == 'Cow':
            return (f'{self.name} say moooo')
        elif self.species == 'Dog':
            return (f'{self.name} say haw haw')
        elif self.species == 'Cat':
            return (f'{self.name} say meow')
        else:
            return (f'Sorry i`m dont understand who is {self.name}')


animal_1 = Animal('Boni', 'Cat', 4)
animal_2 = Animal('Cesar', 'Dog', 10)

print(animal_1.make_sound(), animal_2.make_sound())

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area (self):
        return (f'Площа прямокутника: {self.width * self.height}')

rec_1 = Rectangle(10, 2)
rec_2 = Rectangle(13, 5)

print(rec_1.calculate_area(), rec_2.calculate_area())