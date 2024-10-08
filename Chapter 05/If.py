cars = ['audi', 'bmw', 'honda', 'civic']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car1 = 'GT4'
car2 = 'bmw'

if car1 in cars:
    print('The car is in the house!')
elif car2 in cars:
    print(f"{car1} is not in the house, {car2} is in the house!")
else:
    print("Nither found in the car.")

if car1 in cars:
    print('The car is in the house!')
if car1 not in cars:
    print("The car is not in the house!")