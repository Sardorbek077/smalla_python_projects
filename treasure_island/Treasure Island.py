print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
******************************************************************************
''')

print('Welcome treasure Island. \nYour mission is to find the treasure.')
choice1 = input('You\'re at a crossroad, where do you want to go? \n Type "left" or "right".\n').lower()

if choice1 == 'left':
    choice2 = input('You\'ve come to al lake. '
                    'There is an Island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.').lower()

    if choice2 == "wait":
        choice3 = input("You arrive at the Island unharmed. "
                        "There is house with 3 doors. One Red, "
                        "one Yellow and one Green. "
                        'Which colour do you choose? ').lower()
        if choice3 == 'red':
            print('It\'s a room full fire. Game Over')
        if choice3 == 'yellow':
            print('You found the treasure. You Win!')
        if choice3 == 'green':
            print('You entered a room of beasts. Game Over')
    else:
        print('You got attacked by angry trout. Game Over.')
else:
    print("You fell in to a hole. Game Over!")
