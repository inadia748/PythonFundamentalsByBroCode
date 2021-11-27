#dictionary = A changeable, unordered collection of unique key: value pairs. They are fast because they use hashing, allows us to access a value quickly.  They are mutable.

capitals = {'USA': 'Washington D.C',
            'Bangladesh': 'Dhaka',
           'China': 'Beijing',
           'Russia': 'Moscow',
           }

print(capitals["Russia"])
#print(capitals['Germany']), it will give error
print(capitals.get('Germany')) #if Germany is present in the dictionaries
print(capitals.keys())
print(capitals.values())
print(capitals)
print(capitals.items())


capitals.update({'Germay' :'Berlin'})
capitals.update({'USA': 'Miami'})
capitals.pop('China')


for key, value in capitals.items():
    print(key, value)


capitals.clear()
print(capitals)