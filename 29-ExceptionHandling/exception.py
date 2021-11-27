# exception = events detected during excecution that interrupts the flow of a program.

'''

numerator = int(input('Enter a number to divide: '))
denominator = int(input('Enter a number to divide by: '))
result = numerator / denominator

print(result)

Here, exceptions will occur because if the user enters the numerator as 5 and denominator as 0, it will interrupt the program because 5 divided by 0 is impossible. So, an exceptions occurs. To prevent this, we use try and catch method to prevent user from making absurd choices.


'''


try:
    numerator = int(input('Enter a number you want to divide: '))
    denominator = int(input('Enter a number you want to divide by: '))
    result = numerator / denominator
    
except ZeroDivisionError as e:  #e is giving the error of what the user inputed that caused an interruption
    print(e)
    print("You can't divide by zero")
except ValueError as e:
    print(e)
    print('Enter only numbers please')
except Exception as e:
    print(e)
    print('Something went wrong')

else:
    print(result)

finally: #finally is used in filehandling.
    print('This will always execute')