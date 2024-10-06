import random

print('Welcome to PyPassword Generator')
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input('How many numbers would you like?\n'))

letters = []
numbers = []
symbols = []
for i in range(65, 90):
    letters.extend(chr(i))

for i in range(97, 123):
    letters.append(chr(i))

for i in range(48, 58):
    numbers.append(int(chr(i)))

for i in range(33, 44):
    if chr(i) != "'" and chr(i) != '"':
        symbols.append(chr(i))

password = []

while num_numbers > 0:
    password.append(random.choice(numbers))
    num_numbers -= 1


while num_symbols > 0:
    password.append(random.choice(symbols))
    num_symbols -= 1


while num_letters > 0:
    password.append(random.choice(letters))
    num_letters -= 1


print('Your password is: ', end="")
for i in range(len(password)):
    choice = random.choice(password)
    print(str(choice), end=' ')
    password.remove(choice)
