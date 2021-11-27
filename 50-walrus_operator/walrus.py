#walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

happy = True
print(happy)


# We can write the above code by using walrus operator
print(happy := True)

'''
foods = list()
while True:
    food = input('What food do you like?: ')
    if food =='quit':
        break
    foods.append(food)  
'''

#Another way of writing the above code:

foods = list()

while food := input('What food do you like to eat?: ') != 'quit':
    foods.append(food)

