import random


def guess_and_win():
    rand = random.randint(1, 1000)
    number = 0
    while number != rand:
        number = int(input('Enter your guess number between 1 to 1000: '))
        if number == rand:
            print('Congratulations, you guessed right.')
            if number == rand:
                question = str(input('Will you like to continue your game?(Yes or No): '))
                if question.upper() == 'Yes' or question.lower() == 'yes':
                    rand = random.randint(1, 1001)
                else:
                    return 'Thanks for playing'
        elif number < rand:
            print('Your number is lower than the number.')
        elif number > rand:
            print('Your number is too high, Keep trying.')


print(guess_and_win())
