import random

#1. Generating number ranging from 1 to 6

x = random.randint(1, 6)
print(x)


#2. Generating a number between 0 and 1
y = random.random()
print(y)


#3. Generating random choices

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)
print(z)


cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)
print(cards)
