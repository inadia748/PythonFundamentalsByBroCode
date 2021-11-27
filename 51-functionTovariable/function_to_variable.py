def hello():
    print('Hello')


print(hello) # it will give memory address of the function. Each time you run the program, it will give different memory address.


# so, to prevent that, assign a variable to 'hello' function, then the memory address remains same
hi = hello      
print(hi)

hi()
print()
hello()

print()
say = print         
say('Whoa! I cannot believe this works! ')