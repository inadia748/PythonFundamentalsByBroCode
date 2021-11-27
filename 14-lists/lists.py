#list = used to store multiple items in a single variable
#list are mutable

food = ['pizza', 'hamburger', 'hotdog', 'spagetti', 'pudding']

print(food)
print(food[0])
print(food[3])
print(food[4])

food[0] = 'biryani'

for x in food:
    print(x, end = ' ')



#1. Add element at the end of the list

food.append('icecream')

#2. remove an element from the list
food.remove('hotdog')

#3. remove an element from the end of a list
food.pop()

#4. insert an element on a positon
food.insert(0, 'cake')

print(food)

#5. sort will sort it alphabettically
food.sort()
print(food)

#6. clear will remove everyting from the list
food.clear()
print(food)