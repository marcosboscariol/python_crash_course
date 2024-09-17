bycicles = ['trek', 'cannondale', 'redline', 'specialized']
print(bycicles)

# Accessing a Element in a list
print(bycicles[0])
print(bycicles[0].title())
print(bycicles[-1])

# Using Individual Values from a List
message = f'My first bycicle was a {bycicles[2].title()}.'
print(message)

# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements in a List

# Append
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
