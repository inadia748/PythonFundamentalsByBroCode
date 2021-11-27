import os


#create a file 'test.txt' and write 'Hi there', we intend to move this file.
source = 'test.txt'

#pick a location in your desktop to move the source file. We selected a folder named 'Homeworks' for the destination and put a random file name, in our case we put 'moved.txt'
destination = 'C:\\Users\\Lisa mona\\Desktop\\Homeworks\\moved.txt'

#initially, moved.txt in Homeworks folder is not present.
try:
    # check to see if the moved.txt is present or not
    if os.path.exists(destination):
        print('There is already a file there')
    else:
        os.replace(source, destination)
        print(source+" was moved")

except FileNotFoundError:
    print(source+" was not found")





#creating another source and destination for moving a folder

#create a folder named 'folder'
source1 = 'folder'
destination1 = 'C:\\Users\\Lisa mona\\Desktop\\Homeworks\\folder'


try:
    
    if os.path.exists(destination1):
        print('There is already a folder there')
    else:
        os.replace(source1, destination1)
        print(source1+" was moved")

except FileNotFoundError:
    print(source1+" was not found")

