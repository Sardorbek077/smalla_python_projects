with open('my_file.txt') as file:
    contents = file.readlines()
    print(contents)

for i in contents:
    print(i)

# with open('my_file.txt', mode='a') as file:
#     file.write('I am the best')
