import os

path = 'C:\\Users\\Lisa mona\\Desktop\\HTMLCSS\\Flipkart'

if os.path.exists(path):
    print('That location exists:')
    if os.path.isfile(path):
        print('That is a file')
    elif os.path.isdir(path):
        print('That is a directory')
else:
    print("The location does not exist")