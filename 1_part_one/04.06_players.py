players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0: 3])
print(players[: 4])
print(players[2:])
print(players[-3:])


print('Here are the names:')
for names in players[:3]:
    print(names.title())
