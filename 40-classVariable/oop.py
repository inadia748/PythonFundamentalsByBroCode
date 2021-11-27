from car import Car


car_1 = Car('Chevy', 'Corvet', 2009, 'blue')
car_2 = Car('Ford', 'Mustang', '2002', 'red')

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()


print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()

print(car_1.wheels)
print(car_2.wheels)

car_2.wheels = 2     
print(car_2.wheels)


print(Car) #accessing the main class without creating objects(example:-car_1, car_2 etc)
print(Car.wheels)



#changing the properties in main class

Car.wheels = 3

print(car_1.wheels)
print(car_2.wheels) # we already defined for car_2.wheels = 2, specifically.