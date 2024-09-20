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
