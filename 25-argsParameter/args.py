#  *args = parameter that will pack all arguments into a tuple. It is useful so that a function can accept a varying amount of arguments.

def add(*stuff):
    sum = 0
    stuff = list(stuff) #converting tuple to a list so that you can modify the argument(stuff)
    stuff[0] = 10 # originally stuff[0] = 1, since you converted to a list and made it stuff[0] = 10
    for i in stuff:
        sum+=i
    return sum    


print(add(1,2,3))
print(add(1, 2, 3, 4, 5, 6))


def mult(*num):
    mul = 1
    for i in num:
        mul *= i
    return mul       


print(mult(2, 5))
print(mult(2, 3, 5))