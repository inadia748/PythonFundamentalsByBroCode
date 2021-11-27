#sets is a collection which is unordered, unindexed. They do not allow duplicate values. A set is faster than a list

utensils = {"fork", "spoon", "knife", "knife", "knife", 'chopsticks'}

utensils.add('napkins')
utensils.remove('knife')

for x in utensils:
    print(x)

#utensils.clear()

#print(utensils)


dishes = {'bowl', 'plate', 'cup', 'chopsticks'}

utensils.update(dishes)

print(utensils)

dinner_table = utensils.union(dishes)

print(dinner_table)


print(utensils.difference(dishes))  #what do utensils have that dishes does n't
print(dishes.difference(utensils)) #what does dishes have that utensils does n't

print(utensils)


print(utensils.intersection(dishes)) #what do they have in common