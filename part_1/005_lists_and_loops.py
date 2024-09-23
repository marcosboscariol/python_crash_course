# Looping Through an Entire List

# for Loopign
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'You did a great job, {magician.title()}!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print('Thank you everyone, that was a great magic show!')

# Making Numerical Lists

# Using range() Function
for value in range(1, 10):
    print(value)

numbers = list(range(1, 6))
print(numbers)

squares = []
for number in range(1, 11):
    squares.append(number**2)
print(squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(max(digits))
print(min(digits))
print(sum(digits))

# List comprehensions
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# Working with Part of a List

# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# Looping through a Slice
for player in players[:3]:
    print(player.title())

# Coppyinh a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

my_foods.append("cannoli")
friends_food.append("icecream")

print("My favorite foods are: ")
print(my_foods)
print("\nMy friend's favorite foods are: ")
print(friends_food)

# Tuples

# Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping through all values in a Tuple
for dimension in dimensions:
    print(dimension)

# Writing over a Tuple
dimensions = (200, 50)
print("\nOriginal dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nNew dimensions: ')
for dimension in dimensions:
    print(dimension)
