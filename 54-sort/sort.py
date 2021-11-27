# sort() method = used with lists
# sort() function = used with iterables



# sorting in a list
students = ['Squidward', 'Sandy', 'Patrick', 'Spongebob', 'Mr.Krab']

students.sort()

for i in students:
    print(i)

students.sort(reverse = True)

print()

for i in students:
    print(i)


print()   
print('##########################')
print('Tuple') 

students2 = ('Squidward', 'Sandy', 'Patrick', 'Spongebob', 'Mr.Krab')

sorted_students = sorted(students2)

for i in sorted_students:
    print(i)

print('#############################')

sorted_students = sorted(students2, reverse=True)

for i in sorted_students:
    print(i)


print()

people = [
    ('SquidWard', 'F', 69),
    ('Sandy', 'A', 33),
    ('Patrick', 'D', 35),
    ('Spongebob', 'B', 20),
    ('Mr.Krab', 'C', 77)
]

people.sort()

for i in people:
    print(i)

grade = lambda grades:grades[1]
age = lambda ages:ages[2]

people.sort(key = age)

print()

for i in people:
    print(i)

people.sort(key = age, reverse=True)

print()   
for i in people:
    print(i)

print('########################')
print('Tuple')

people2 = (
    ('SquidWard', 'F', 69),
    ('Sandy', 'A', 33),
    ('Patrick', 'D', 35),
    ('Spongebob', 'B', 20),
    ('Mr.Krab', 'C', 77)
)

sorted_people = sorted(people2, key = age)

for i in sorted_people:
    print(i)