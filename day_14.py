import random


def compare(u_num):
    while True:
        computer_num = random.randrange(10)
        print(computer_num)
        if computer_num != u_num:
            if computer_num < u_num:
                return True, computer_num
            elif computer_num > u_num:
                return False, computer_num
        else:
            computer_num = random.randrange(10)


def play_game():
    start = True
    final = 0
    while start:
        user_num = int(input("Num: "))
        result = compare(user_num)
        if result == True:
            final += 1
            print(final, result)
        else:
            print(False, final)
            start = False


play_game()