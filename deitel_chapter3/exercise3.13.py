# import math
# print("Enter any number and I give you its factor")
#
# numbers = int(input("Enter your number: "))
#
# for number in range(1, numbers + 1):
#     if numbers % number == 0:
#         print(f'{number:>5}', end='')
#
#
# print("Enter any number and I give you its factorial")
#
# numbers = int(input("Enter your number: "))
#
# fact = math.factorial(numbers)
# print(fact)
#
#
#
# def fact_num(number: int):
#     factorial = 1
#     for index in range(1, number + 1, 1):
#         factorial *= index
#     return factorial
#
#
# print(fact_num(number=5))

print('Give me any number and I will tell you its factorial')


def input_factorial(factorial=1):

    number = int(input('Enter your number: '))
    for index in range(1, number + 1):
        factorial *= index
        # raise ValueError('Your input should be number greater than zero and a whole number')

    return f'The factorial of your number is {factorial}'


print(input_factorial())
