alien_0 = {
    'color': 'green',
    'points': 5
}

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

new_points = alien_0['points']

print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
print(f'You just earned {new_points} points!')

alien_0['color'] = 'yellow'

print(alien_0)

del alien_0['points']
print(alien_0)
