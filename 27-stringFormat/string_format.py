#string format = optional method that gives user more control when displaying the output

animal = 'cow'
item = 'moon'

print('The ' + animal + ' jumped over the '+ item)

print("The {} jumped over the {}".format(animal, item))
print("The {} jumped over the {}".format(item, animal))

#positional arguments, see the indexes in format(animal, items)
print("The {0} jumped over the {1}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))

print("The {0} jumped over the {0}".format(animal, item))


#keyword arguments
print("The {device} flies over the {object}".format(device='spaceship', object='planet of Uranus'))

print("The {device} flies over the {device}".format(device='spaceship', object='planet of Uranus'))



text = "The {} jumps over the {}"
print(text.format(animal, item))


name = 'Nadia'
print('Hello, my name is {}'.format(name))
print('Hello, my name is {:10}.Nice to meet you'.format(name)) #you are adding a padding of 10 spaces
print('Hello, my name is {:<10}.Nice to meet you'.format(name)) #you are adding a padding of 10 spaces (left aligned)
print('Hello, my name is {:>10}.Nice to meet you'.format(name)) #you are adding a padding of 10 spaces (right aligned)
print('Hello, my name is {:^10}.Nice to meet you'.format(name)) #you are adding a padding of 10 spaces(center aligned)



number = 3.14159
mynumber = 1000

print('The number pi is {:.2f}'.format(number))
print('The number pi is {:.3f}'.format(number))
print('The number is {:,}'.format(mynumber))
print('The selected number is {selected:,}'.format(selected = 2000))
print('The number is binary: {:b}'.format(mynumber)) #binary repersentation of mynumber
print('The number is octal {:o}'.format(mynumber)) #octal representation of mynumber
print('The number is hexadecimal {:X}'.format(mynumber)) #octal representation of mynumber


