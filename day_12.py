import random


def check_answer(user_guess, answer, turns):

    if user_guess > answer:
        print('Too High!')
        return turns - 1
    elif user_guess < answer:
        print('Too Low!')
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}. You Win!")


def set_difficulty():

    difficulty_level = input("Choose a difficulty. Type 'easy or 'hard': ").lower()
    if difficulty_level == "easy":
        attempts = 10
        return attempts
    else:
        attempts = 5
        return attempts


def game():

    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")

    random_num = random.randint(1, 100)
    turns = set_difficulty()

    while turns:

        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input('Please write your guessing number: '))

        turns = check_answer(guess, random_num, turns)

        if turns == 0:
            print("You run out of attempts. You Lose!")
            break

        (print("Guess again."))


game()
