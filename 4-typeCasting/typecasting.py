#typecasting  converts the data type of a value to another data type.

x = 1 #int
y = 2.0 #float
z = '3' #string

print(x, type(x))
print(y, type(y))
print(z, type(z))


y = int(y)
print(x, type(x))
print(y, type(y))
print(z, type(z))

print(z * 3)

z = int(z)
print(z * 3)

x = float(x)
print(x * y)

#Concatenation in python can only concatenate string. So, inorder to concatenate an integer or a float, you have to convert integer and float to string.


print('X is: '+ str(x))
print('Y is: '+ str(y))
print('Z is '+ str(z))