# lamda function = function written in 1 line using lamdda keyword. Can accept any number of arguments, but only has one expression. (think of it as a shortcut). It is useful if needed for a short period of time, throw-away.


# lamda parameters: expression

double = lambda x: x*2
multiply = lambda x, y: x*y
add  = lambda x, y, z: x + y + z              
full_name = lambda first_name, last_name: first_name + last_name 
age_check = lambda age: True if age >= 18 else False

print(age_check(18))

'''
def double(x):
    return x * x

print(double(5))
'''

double(5)

print(multiply(5,6))
print(add(1, 8, 2))
print(full_name('Nadia', 'Islam'))
