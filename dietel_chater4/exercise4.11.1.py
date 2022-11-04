import random


def modified_guess_and_win():
    numbers = 1001
    rand = random.randint(1, numbers)
    number = 0
    count = 0
    while number != rand:
        count += 1
        try:
            number = int(input('Enter your guess number between 1 to 1000: '))
        except ValueError:
            print('Your input should be number only')
        if number == rand:
            print('Congratulations, you guessed right.')
            count = 0
            question = str(input('Will you like to continue your game?(Yes or No): '))
            try:
                if question.upper() == 'Yes' or question.lower() == 'yes':
                    new_number = number // 2
                    if new_number != 1:
                        rand = random.randint(1, number)
                elif question.upper() == 'No' or question.lower() == 'no':
                    return 'Thanks for playing'
            except ValueError:
                print('Your input is wrong')
            # elif question.upper() or question.lower() != 'yes' or 'Yes' and question.upper() or question.lower() != 'No' or 'no':
            #     try:
            #         raise ValueError("Your input is wrong")
            #     except ValueError as e:
            #         print(e)
            # continue
        elif number == str:
            print('uygyig')
        elif number < rand:
            print('Your number is lower than the number.')
        elif number > rand:
            print('Your number is too high, Keep trying.')
        if count <= 10 and number != rand:
            print('Either you know the secret or you got lucky!')
        if count > 10 and number != rand:
            print('You should be able to do better! Why should it take no more than 10 guesses?')


print(modified_guess_and_win())
