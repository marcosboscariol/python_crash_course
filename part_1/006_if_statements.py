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
