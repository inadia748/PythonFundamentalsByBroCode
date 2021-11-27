#String Methods


#1- Length of a string

name = 'Nadia'
print(len(name))

#2- Find characters of a string
print(name.find('d'))

#3- Capitalize the string, Capitalize will only capitalize the first leter of a string.
print(name.capitalize())


#4- Upper will make string uppercase
print(name.upper())

#5- lower will make string lowercase
print(name.lower())

#6- isdigit() will check if all the characters in a string is present or not
print(name.isdigit())

age_instring = '835'
print(age_instring.isdigit())


#7- isalpha() will check if string contains only alphabetical letters
print(name.isalpha())
print('Nadia Islam'.isalpha()) # because the string 'Nadia Islam' contains a space, isaplha() will only consider alphabetical letters and not space


#8- count() will count how many characters are in the string
print(name.count('a'))
print('Nadia Islam'.count('m'))


#9- replace() will replace characters 
print(name.replace('N', 'R'))

print(name * 3)