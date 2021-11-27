# function is a block of code which is executed when it is called.



def hello(first_name = 'Stranger', last_name= 'Doe', age = 'Not-given'):
    print('Hello!, ' + first_name + ' '+ last_name)
    print('You are '+ str(age)+ ' old')
    print('Have a nice day')


hello('Nadia', 'Islam', 22)
hello('Sarah')
hello('Will')