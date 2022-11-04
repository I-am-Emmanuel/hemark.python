# def square(number):
#     """Calculate the square of a number"""
#     return number ** 2
#
#
# print(square(9))
# print(square(2.5))
# print(square(17))
# print("The square of 10 is", square(10))
import math

# def square_root(number):
#     """Calculate the square root of a number."""
#     # return math.sqrt(number)
#     root = 0.5
#     return number ** root


# print(square_root(81))


# def maximum(value1, value2, value3):
#     """Getting the maximum value of an object."""
#     maximum = value1
#     if value2 > value1:
#         maximum = value2
#     elif value3 > maximum:
#         maximum = value3
#     return maximum
#
#
# print("The maximum value of your number is", maximum(92, 88, 17))
# print(maximum("Doc_strings", "Dungo-park", "Dandruff"))
# print(maximum(-9.3, -33, -0.2))

# my_list = [72, 99, 100, 0.9, 473]
# new_list = max(my_list)
# print(new_list)
#
# fruit = "orange"
# maxim = max(fruit)
# print(maxim)
#
import random

frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0


# for roll in range(6_000_000):
#     face = random.randrange(1, 7)
#
#     if face == 1:
#         frequency1 += 1
#     elif face == 2:
#         frequency2 += 1
#     elif face == 3:
#         frequency3 += 1
#     elif face == 4:
#         frequency4 += 1
#     elif face == 5:
#         frequency5 += 1
#     elif face == 6:
#         frequency6 += 1
#
# print(f'Face{"Frequency":>13}')
# print(f'{1:>4}{frequency1:>13}')
# print(f'{2:>4}{frequency2:>13}')
# print(f'{3:>4}{frequency3:>13}')
# print(f'{4:>4}{frequency4:>13}')
# print(f'{5:>4}{frequency5:13}')
# print(f'{6:>4}{frequency6:>13}')

def roll_dice():
    """Roll two dice and return their values as a tuple"""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1, die2


def display_dice(dice):
    die1, die2 = dice
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')


die_values = roll_dice()
display_dice(die_values)
sum_of_dice = sum(die_values)

if sum_of_dice in (7, 11):
    game_status = 'WON'
elif sum_of_dice in (2, 3, 12):
    game_status = 'LOST'
else:
    game_status = 'CONTINUE'
    my_point = sum_of_dice
    print('My point is', my_point)

while game_status == 'CONTINUE':
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)

    if sum_of_dice == my_point:
        game_status = 'WON'
    elif sum_of_dice == 7:
        game_status = 'LOST'

if game_status == 'WON':
    print('Player wins')
else:
    print('Player loses')

# student = ('Tunde', [78, 92, 82, 100, 56])
# name, grades = student
# print(f'Student Name:{name}, Grades:{grades} ')
# print(f'{name}: {grades}')
#
# def cube(x):
#     """Calculate the cube of x."""
#     return x ** 3
#
#
# print('The cube of 5 is', cube(x=5))
#
# from decimal import Decimal
# from math import factorial
# 
# hole = int(math.factorial(76))
# print(hole)
#
import statistics


# def variance():
#     """Calculating the average of some certain numbers"""
#     numbers = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]
#     lst = []
#     square_lst = []
#     average = sum(numbers) / len(numbers)
#
#     for value in numbers:
#         lst.append(value - average)
#     for values in lst:
#         square_lst.append(values ** 2)
#     new_lst = sum(square_lst) / len(square_lst)
#
#     return new_lst
#
#
# print(variance())

# def standard_dev():
#     calculate = statistics.stdev([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])
#     calculate2 = statistics.variance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])
#     return f'{calculate:.6f} is the result of the standard deviation  and {calculate2} is the result of the variance'
#
#
# print(standard_dev())
#
# def variance(*args):
#     """Calculating the average of some certain numbers"""
#     # numbers = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]
#     lst = []
#     square_lst = []
#     average = sum(args) / len(args)
#
#     for value in args:
#         lst.append(value - average)
#     for values in lst:
#         square_lst.append(values ** 2)
#     new_lst = sum(square_lst) / len(square_lst)
#
#     return new_lst
#
#
# print(variance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2]))


def std_deviation():
    """Calculating the average of some certain numbers"""
    numbers = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]
    lst = []
    square_lst = []
    average = sum(numbers) / len(numbers)

    for value in numbers:
        lst.append(value - average)
    for values in lst:
        square_lst.append(values ** 2)
    new_lst = sum(square_lst) / len(square_lst)

    standard_deviation = new_lst ** 0.5

    return f'{standard_deviation:.2f}'


print(std_deviation())
