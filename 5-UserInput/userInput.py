name = input('What is your name?')

print('Hello, '+ name)

print(type(name))


#userinput is always in string, so for a integer or a float, you have to typecase userinput

age = float(input('What is your age?')) #typecasting is used to convert userinput to integer 
age = age + 1
print(age)

print('You are ' + str(age) + ' years old')

height = float(input('What is your height(cm)?'))
print('You are ' + str(height) + 'cm tall')