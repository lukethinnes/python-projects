import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number betwee 1 and {x}: '))
        print(guess)
        if guess < random_number:
            print('Sorry, you were too low.')
        elif guess > random_number:
            print('Sorry, you were too high.')

    print(f'Way to go! That number was for sure {random_number}.')


guess(10)
