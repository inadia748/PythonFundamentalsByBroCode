# slicing = create a substring by extracting elements from another string.

'''  
slicing can be done in two ways: 
a) indexing[]
b) slice()

indexing - [start: stop: step]
slicing - slice(start, stop, step)
'''


#slicing by indexing

name = 'Bro Code'

firstname = name[0:3]  # name[0:3], it will start from index 0 and end in index 2.

print(firstname)

print(name[:3])

lastname = name[4:8] # name[4:8], it will start from index 4 and end in index 8
print(lastname)
print(name[4:])

funky_name = name[0:8:2]
print(funky_name)

print(name[0:8:3])
print(name[::3])

reverse_name = name[::-1]
print(reverse_name)


#indexing from left to right starts from 0 to n
#indexing from right to left starts from -1 to -n
website1 = 'http://google.com'
slice = slice(7, -4)
print(website1[slice])
website2 = 'http://wikipedia.com'
print(website2[slice])

