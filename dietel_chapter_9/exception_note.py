def division_exception():
    while True:
        try:
            number_1 = int(input('Enter your first number:: '))
            number_2 = int(input('Enter your second number:: '))
            result = number_1 / number_2
        except ValueError:
            print('You must enter a number!\n')
        except ZeroDivisionError:
            print('Denominator must not be zero!\n')
        else:
            return f'{number_1:2f} / {number_2:.2f} = {result}'
        break


print(division_exception())

# while True:
#     try:
#         number_1 = int(input('Enter your first number:: '))
#         number_2 = int(input('Enter your second number:: '))
#         result = number_1 / number_2
#     except ValueError:
#         print('You must enter two numbers!\n')
#     except ZeroDivisionError:
#         print('Denominator must not be zero!\n')
#     else:
#         print(f'{number_1:2f} / {number_2:.2f} = {result:.2f}')
#           break


def try_it(value):
    try:
        x = int(value)
    except ValueError:
        print(f'You must be sick for trying to convert {value} to an integer')
    else:
        print(f'int({value}) is {int(value)}')


print(try_it(value=83.72))
