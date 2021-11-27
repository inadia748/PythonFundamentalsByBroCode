import os
import shutil

path = 'test.txt'

try:
    #os.remove(path) #remove a file
    #os.rmdir(path) #this to remove an empty directory
    shutil.rmtree(path) #it will remove a folder along with its contents

except FileNotFoundError:
    print('The file was not found')
except PermissionError:
    print('You do not have persion to delete that')
except OSError:
    print('You cannot elete that using that function')
else:
    print(path+ " was deleted")