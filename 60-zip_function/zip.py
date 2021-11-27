# zip(*iterables) = aggregate elements from two or more iterables(list, tuples, set, etc) creates a zip object with paired elements stored in tuples  for each element

usernames = ['Dude', 'Bro', 'Mister']
passwords = ['passw#rd', 'abc123', 'guest']


users = zip(usernames, passwords)

print(users)
print(type(users))

for i in users:
    print(i)


# converting zip objects to a list

users = list(zip(usernames, passwords))
print(users)
print(type(users))

#converting zip objects to dictionary
users = dict(zip(usernames, passwords))
print(users)
print(type(users))

for key, value in users.items():
    print(key+" : " +value)



login_dates = ['1/1/2021', '1/5/2021', '2/5/2020']

users = zip(usernames, passwords, login_dates)

for i in users:
    print(i)

