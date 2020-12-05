import car
"""При использовании методов, из модуля импортированного целиком, 
    перед ними неободимо указывать название импортированного модуля."""

my_new_car = car.Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
