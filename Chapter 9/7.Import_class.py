#My_car.py file, import class
from car import Car

my_new_car = Car('audi', 'a8', 2024)
print(my_new_car.get_descriptive_name())

#Store multiple classes in a module
from car import ElectricCar, Car
my_leaf = ElectricCar('audi', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

