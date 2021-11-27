'''
1. Module can be run as a standalone program.
2. Module can be imported and used by other modules


Python interpreter sets 'special variables', one of which is __name__, then Python will execute the code within __main__

'''

# Python interpreter sets 'special vairables', one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it 's the initial module being run.

# Before Python runs a file, before it sets through any code, it sets a few special variable and '__name__' is one of those special variable. When a python file is run directly, it sets the '__name__' variable and then runs the file.



# 1 One way to see the code and run in second_module.py
'''
print("First Module 's Name: {}".format(__name__))


def main():
    print("First Module 's Name: {}".format(__name__))
    


if __name__ == '__main__':
    main()
'''



#2) Second way to run this code and check in second_modules.py

'''
if __name__ == '__main__':
    print('Run Directly')
else:
    print('Run From import')
'''



# 3) Third way to run this code and check in second_modules.py

print('This will always be run')

def main():
    print("First Module 's Main Method ")

if __name__ == '__main__':
    main()





'''
###############################
IMPORTANT
##############################

The code is taken from Corey Schafer 's Youtube Channel in Python.

'''