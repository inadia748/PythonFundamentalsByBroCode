# kwargs = parameter that will pack all the arguments into a dictionary. It is useful so that a function can accept a varying number of keyword arguments


def hello(**kwargs):
    print('Hello, '+ kwargs['first'] + " " +kwargs['middle']+" "+ kwargs['last'])

hello(first = 'Sis', middle = 'Gal', last= 'Code')


def hello1(**kwargs):
    print('Hello', end = ', ')
    for key, value in kwargs.items():
        print(value, end = ' ')


hello1(first = 'Nadia', middle = 'Laila', last = 'Islam')
