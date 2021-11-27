# copyfile() = copies contents of a file.
# copy() = copyfile() + permission mode + destination can be directory.
# copy2() = copy() + copies metadata(file creation and modification time)

import shutil

shutil.copyfile('C:\\Users\\Lisa mona\\Desktop\\Python\\PythonWithBroCode\\32-write_a_file\\test.txt', 'copy.txt')


 # shutil.copyfile(source, destination)