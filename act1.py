import random

def guess_the_number():
    number = random.randint(1, 100)
    guess = int(input("Guess a number between 1 and 100: "))

    while guess != number:
        if guess < number:
            print("Too low. Guess again.")
        else:
            print("Too high. Guess again.")
        guess = int(input("Guess again: "))

    print("Congratulations! You guessed the number correctly.")

guess_the_number()

