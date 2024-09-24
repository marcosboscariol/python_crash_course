# If Statement

# Simple Example
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


# Conditional Tests

# Checking for Equality
car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')


# Checking for Inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")


# Numerical Comparison
age = 18

print(age == 18)
print(age < 18)
print(age > 18)


# Checking Multiple Conditions

# Using and to Check Multipla Conditions
age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >= 21)


# Using or to Check Multipla Conditions
age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21)


# Checking Whether a Value us Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f'{user.title()}, you can post.')


# Simple if Statement
age = 19

if age >= 18:
    print('You are old enough to vote.')


# if-else Statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


# The if-elif-else Chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")


#
