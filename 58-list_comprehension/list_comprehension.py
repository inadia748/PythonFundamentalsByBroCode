# list comprehension = a way to create a new list with less syntax. Can mimic certain lambda functions, easier to read.







# create an empty list, create a loop and define what each loop iteration should do.

squares = []

for i in range(1, 11):
    squares.append(i * i)
print(squares)


squares2 = [i * i for i in range(1,11)]
print(squares2)


students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = []

for i in students:
    if i > 60:
        print(i)
        passed_students.append(i)
print(passed_students)

#  list = [expression for item in iterable]
passed_students2 = list(filter(lambda x: x > 60, students))
print(passed_students2)



#  list = [expression for item in iterable if conditional]
# list = [expression (if/else) for in iterable]
passed_students3 = [i for i in students if i > 60]
print(passed_students3)

passed_students4 = [i if i>60 else 'Failed!' for i in students]
print(passed_students4)