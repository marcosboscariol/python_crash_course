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
