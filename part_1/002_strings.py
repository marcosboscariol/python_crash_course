# Method: An action that Python can perform on a piece of data.

name = 'ada loveplace'
print(name.title())
print(name.lower())
print(name.upper())

first_name = 'marcos'
last_name = 'boscariol'
full_name = f'{first_name} {last_name}'
print(f'Hello, {full_name.title()}!')

# Add a tab
print('\tPython')

# Add newline
print('Languages:\nPython\nC\nJava')

# Remove whitespaces
favorite_language = '   Python   '
print(favorite_language.rstrip().lstrip())

favorite_language = favorite_language.rstrip().lstrip()
print(favorite_language)

# Remove prefix
url = 'https://nostarch.com'
print(url.removeprefix('https://'))
