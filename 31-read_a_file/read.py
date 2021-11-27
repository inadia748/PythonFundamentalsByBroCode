

with open('test.txt') as file:
    print(file.read())

print(file.closed)


#if the file is misspelled, there will be an interuption so we use try and catch method.
try:
    with open('test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print('That file was not found')