#nested functions call = function calls inside other functions calls innermost function calls are resolved first returned value is used as an argument for the next function.


num = input('Enter a whole positive number: ')
num = float(num)
num = abs(num)
num = round(num)     
print(num)

#the above code can be written in a following way:
print(round(abs(float(input('Enter a whole positive number: ')))))