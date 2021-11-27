#tuples = collections which is ordered and unchangeble. It is used to group together. tuples cannot be modified

student = ('Nadia', 22, 'female')

print(student.count('Nadia'))
print(student.index('female'))


for x in student:
    print(x)

if 'Nadia' in student:
    print('Nadia is here!')