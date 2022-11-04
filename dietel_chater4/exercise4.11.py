import random


def modify_guess_number():
    print('I have hidden some numbers within the range of 1 - 1000. One number per hundred i.e I hid a number '
          'between 1 and 99,\n '
          '100 and 200 and so on.... You guess according to each range of hundreds and the computer will tell you if '
          'you are close \n'
          'to the hidden number or not. It doesnt matter from which number you start your guess. Play wisely!!! ')
    print('')
    numbers = 0
    count = 0
    number_list = [32, 123, 292, 393, 481, 561, 671, 714, 836, 913]
    while numbers != -1:
        numbers = int(input('Enter your number: '))
        count += 1

        if numbers == number_list[0]:
            print('Congratulations you guess right')
            count = 0
            if numbers == number_list[0]:
                response = str(input('Will you continue your game(Yes or No)? '))
                if response.upper() == 'Yes' or response.lower() == 'yes':
                    continue
                else:
                    return 'Thanks for playing'
        elif numbers < number_list[0]:
            print('Your input is too low for the number in this range. Try again ')
        elif numbers <= 100 and number_list[0] < numbers < number_list[1]:
            print('Numbers too high for number in this range. Keep guessing')
        elif number_list[1] > numbers:
            print('Your input is too low for the number in this range')
        elif numbers == number_list[1]:
            print("Congratulations")
            count = 0
            if numbers == number_list[1]:
                response = str(input('Will you continue your game(Yes or No)? '))
                if response.upper() == 'Yes' or response.lower() == 'yes':
                    continue
                else:
                    return 'Thanks for playing'
        elif numbers <= 200 and number_list[1] < numbers < number_list[2]:
            print('Numbers too high for number in this range. Keep guessing')
        elif number_list[2] > numbers:
            print('Your input is too low for the number in this range. Keep trying')
        elif numbers == number_list[2]:
            print('Congratulations you guess right')
            count = 0
            if numbers == number_list[2]:
                response = str(input('Will you continue your game(Yes or No)? '))
                if response.upper() == 'Yes' or response.lower() == 'yes':
                    continue
                else:
                    return 'Thanks for playing'

        elif numbers <= 300 and number_list[2] < numbers < number_list[3]:
            print('Your guessed number is too high for numbers in this range')
        elif number_list[3] > numbers:
            print('Your input is too low for the number in this range. Keep trying')
        elif numbers == number_list[3]:
            print('Congratulations you guess right')
            count = 0
            if numbers == number_list[3]:
                response = str(input('Will you continue your game(Yes or No)? '))
                if response.upper() == 'Yes' or response.lower() == 'yes':
                    continue
                else:
                    return 'Thanks for playing'

        elif numbers <= 400 and number_list[3] < numbers < number_list[4]:
            print('Your guessed number is too high for numbers in this range')
        elif number_list[4] > numbers:
            print('Your input is too low for the number in this range. Keep trying')
        elif numbers == number_list[4]:
            print('Congratulations you guess right')
            count = 0
            if numbers == number_list[4]:
                response = str(input('Will you continue your game(Yes or No)? '))
                if response.upper() == 'Yes' or response.lower() == 'yes':
                    continue
                else:
                    return 'Thanks for playing'
        elif numbers <= 500 and number_list[4] < numbers < number_list[5]:
            print('Your guessed number is too high for numbers in this range')
        elif number_list[5] > numbers:
            print('Your input is too low for the number in this range. Keep trying')
        elif numbers == number_list[5]:
            print('Congratulations you guess right')
            count = 0
            if numbers == number_list[5]:
                response = str(input('Will you continue your game(Yes or No)? '))
                if response.upper() == 'Yes' or response.lower() == 'yes':
                    continue
                else:
                    return 'Thanks for playing'
        elif numbers <= 600 and number_list[5] < numbers < number_list[6]:
            print('Your guessed number is too high for numbers in this range')
        elif number_list[6] > numbers:
            print('Your input is too low for the number in this range. Keep trying')
        elif numbers == number_list[6]:
            print('Congratulations you guess right')
            if numbers == number_list[6]:
                response = str(input('Will you continue your game(Yes or No)? '))
                if response.upper() == 'Yes' or response.lower() == 'yes':
                    continue
                else:
                    return 'Thanks for playing'
        elif numbers <= 700 and number_list[6] < numbers < number_list[7]:
            print('Your guessed number is too high for numbers in this range')
        elif number_list[7] > numbers:
            print('Your input is too low for the number in this range. Keep trying')
        elif numbers == number_list[7]:
            print('Congratulations you guess right')
            count = 0
            if numbers == number_list[7]:
                response = str(input('Will you continue your game(Yes or No)? '))
                if response.upper() == 'Yes' or response.lower() == 'yes':
                    continue
                else:
                    return 'Thanks for playing'
        elif numbers <= 800 and number_list[7] < numbers < number_list[8]:
            print('Your guessed number is too high for numbers in this range')
        elif number_list[8] > numbers:
            print('Your input is too low for the number in this range. Keep trying')
        elif numbers == number_list[8]:
            print('Congratulations you guess right')
            count = 0
            if numbers == number_list[8]:
                response = str(input('Will you continue your game(Yes or No)? '))
                if response.upper() == 'Yes' or response.lower() == 'yes':
                    continue
                else:
                    return 'Thanks for playing'
        elif numbers <= 900 and number_list[8] < numbers < number_list[9]:
            print('Your guessed number is too high for numbers in this range')
        elif number_list[9] > numbers:
            print('Your input is too low for the number in this range. Keep trying')
        elif numbers == number_list[9]:
            print('Congratulations you guess right')
            count = 0
            if numbers == number_list[9]:
                response = str(input('Will you continue your game(Yes or No)? '))
                if response.upper() == 'Yes' or response.lower() == 'yes':
                    continue
                else:
                    return 'Thanks for playing'
        elif 1001 >= numbers > number_list[9]:
            print('Your guessed number is too high for numbers in this range')

        if count <= 10 and numbers != number_list[0:]:
            print("Either you know the secret or you got lucky!")
        if count <= 10 and numbers == number_list[0:]:
            count = 0
        elif count > 10 and numbers != number_list[0:]:
            print("You should be able to do better! Why should it take no more than 10 guesses? ")
        elif count > 10 and numbers == number_list[0:]:
            break


print(modify_guess_number())
