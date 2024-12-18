#Exercise 1: First name aplphabetically
name = input("My name is ")
sister = input("My sister's name is ")

if name < sister:
    print(f'{name} comes first alphabetically.')
else:
    print(f'{sister} comes first alphabetically.')


#Exercise 2: Lowest of 3
x = int(input("Pick a number one through ten "))
y = int(input("Pick a number one through ten "))
z = int(input("Pick a number one through ten "))

if x < (y and z):
    print(f'The lowest number is {x}')
elif y < (x and z):
    print(f'The lowest number is {y}')
elif z < (x and y):
    print(f'The lowest number is {z}')

#Exercise 3:
age = int(input('How old are you? '))

if age >= 13 and age <= 19:
          print('You are a teenager!')
else:
    print('You are not a teenager!')
