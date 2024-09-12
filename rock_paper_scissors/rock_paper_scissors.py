import random

computer_choice = random.choice([0, 1, 2])
user_respond = input('Do you want to play a game? Type "yes" or "no"\n')

if user_respond == 'yes':
    start = True
    while start:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
        if user_choice == 1 or user_choice == 0 or user_choice == 2:
            if user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
                print(f"Your choice {user_choice}\nComputer choice {computer_choice}")
                print('You Win!')
                start = input('Do you want to play a game again? Type "yes" or "no" ')
            elif user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 0 or user_choice == 0 and computer_choice == 1:
                print(f"Your choice {user_choice}\nComputer choice {computer_choice}")
                print('You Lose!')
                start = input('Do you want to play a game again? Type "yes" or "no" ')
            elif user_choice == computer_choice:
                print(f"Your choice {user_choice}\nComputer choice {computer_choice}")
                print('Draw!')
                start = input('Do you want to play a game again? Type "yes" or "no" ')
            else:
                print('Please choose number among 0, 1, and 2')
        if start == "yes":
            start = True
        else:
            print('Goodbye!')
            start = False
else:
    print("Good Luck!")

