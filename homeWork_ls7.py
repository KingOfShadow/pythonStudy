class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f'Це {self.make} {self.model} {self.year} року виробництва.')


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
    def start_engien(self):
        print(f'You {self.model} ready to go!')
    
    def display_info(self):
        super().display_info()
        print(f'Залий в бак {self.fuel_type}')

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

    def speedlimit(self):
        if self.max_speed >= 110:
            print(f'Slow down please')
            print(f'You exceeded the speed limit by {self.max_speed - 110}')
        else:
            print('all ok')

    def display_info(self):
        super().display_info()
        print(f'Твоя швидкість {self.max_speed}')

class Bicycle(Vehicle):
    def __init__(self, make, model, year, type = 'classic'):
        super().__init__(make, model, year)
        self.type = type

    def start_parking(self):
        print(f'You {self.type} bicycle parked')

    def display_info(self):
        super().display_info()
        print(f'Тип твого велосипеда: {self.type}')

car_1 = Car('BMW', 'Series 5', 1998, 'GAS')
moto_1 = Motorcycle('Yamaha', 'z350', 2024, 240)
bike_1 = Bicycle('Ardis', 'SuperPuer', '2005')

print(car_1.__dict__)
print('--------------------------')
print(moto_1.__dict__)
print('--------------------------')
print(bike_1.__dict__)


car_2 = Car('Mercedes', 'E320', 2006, 'Diesel')
moto_2 = Motorcycle('Suzuki', 'mb1231', 30032, 300)
bike_2 = Bicycle('Olpran', 'Sport 2', 2013, 'Sport')

car_1.display_info()
car_2.display_info()
moto_1.display_info()
moto_2.display_info()
bike_1.display_info()
bike_2.display_info()