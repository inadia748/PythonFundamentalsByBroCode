# map() = applies a function to each item in an iterable(list, tuple, etc).

# map(function, iterable)


store = [
    ('shirt', 20.00),
    ('pants', 25.00),
    ('jacket', 50.5),
    ('socks', 10.02)
]

to_euros = lambda data: (data[0], data[1] * 0.83)
to_bdt = lambda data: (data[0], data[1]* 80)

store_euros = list(map(to_euros, store))
store_bd = list(map(to_bdt, store))
print(store_euros)

for i in store_euros:
    print(i)