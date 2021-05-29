import random


# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess a number betwee 1 and {x}: '))
#         print(guess)
#         if guess < random_number:
#             print('Sorry, you were too low.')
#         elif guess > random_number:
#             print('Sorry, you were too high.')

#     print(f'Way to go! That number was for sure {random_number}.')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = random.randint(low, high)
        feedback = input(
            f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'I guessed your number. It was {guess}. My power should be feared.')


computer_guess(10)
