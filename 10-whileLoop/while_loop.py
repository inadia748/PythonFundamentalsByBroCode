#while loop = a statement that will execute it 's block of code as long as it 's conditions remain true.


'''
while 1 == 1:
    print('Help! I am stuck in a loop')

'''

name = ''

while len(name) == 0:
    name = input('Enter your name: ')

print('Hello ' + name)


#Another way of the above code:
name = None

while not name:
    name = input('Enter your name: ')
print('Hello, '+ name)