listA = []
listB = []
for number in range(1, 10, 2):
    listA += [number]
for number in range(8, 15, 3):
    listB += [number]
new_list = listA + listB
new_list = sorted(new_list)
for idx in range(len(new_list)):
    print(f'{idx}: {new_list[idx]:>5}')
#
#
# def square_number():
#     cube = []
#     cube_list = []
#     for number in range(0, 13):
#         cube += [number]
#     for numbers in (cube[0:]):
#         cube_list.append(numbers ** 3)
#     return f'{cube_list}'
#
#
# print(f'Index {"Value":>3}  Bar')
# list = [21, 18, 40]
# for number in range(len(list)):
#     multi = list[number] * '*'
#     print(f'{number:>3}: {list[number]:>5} {multi:>5}')

numbers = [19, 3, 15, 7, 11]

print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8} Bar')

for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8} {"*" * value}')

#
# list = [82, 99, 100, 231]
# for index, value in enumerate

# names = ['Amanda', 'Sam', 'David', 'JohnBull']
# for index, value in enumerate(names):
#     print(f'{index}: {value}')
#
# names2 = ['Amanda', 'Sam', 'David', 'JohnBull']
# for index in range(len(names2)):
#     print(f'{index}: {names2:>5}')

# listb = []
# numbe = list(range(1, 19))
# for numbers in numb[:]:
#     listb.append([numb % 2 == 0])
# numbe[1:len(numbe):2]
# numb = numbe[1::2]
# numbe[5:10] = [0] * len(numbe[5:10])
# numbe[5:] = []
# numbe[:] = []
# print(numbe)

# def modify_element(listb):
#     for index in range(len(listb)):
#         listb[index] **= 2
#
#     return listb
#
#
# numbers = [10, 23, 29, 32, 44]
#
# print(modify_element(numbers))

# def reverse_word(letter):
#     for index in word:
#         letter = index[::-1]
#     return letter
#
#
# word = ['Hello Binance']
#
# print(reverse_word(letter=word))


# list = ['shola', 'Ogundipe', 'Anuoluwa']
# Ajagbe = sorted(list)
# list.sort()
# print(Ajagbe)
# print(list)
#
# Go = 'Adamolekun'
# for ind in Go[::-1]:
#     print(ind, end='')

#
# numbers = [3, 7, 1, 4, 2, 8, 5, 6]
# five = 5
# if five in numbers:
#     print(f'Found {five} at index number {numbers.index(6)}')

# house = ['Bungalow', 'Skyscraper', 'Bed-room flat', 'Ile dojukoju']
# print(house)
#
# house.reverse()
# print(house)
# house.sort()
# print(house)
# house.clear()
# print(house)
#
# responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 9, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]
# for index in range(1, 10):
#     print(f'{index} appears {responses.count(index)} times in responses')
# responses.sort()
# print(responses)
# responses.remove(8)
# print(responses)

# Modupe = responses[:]
# print(Modupe)
#
# list2 = [item for item in range(1, 6)]
# print(list2)
# list1 = []
# for index in range(1, 6):
#     list1 += [index]
# print(list1)
# lst3 = []
# for index in range(1, 6):
#     index **= 3
#     lst3 += [index]
#
# print(lst3)
#
# lis4 = [item ** 3 for item in range(1, 6)]
# print(lis4)
#
# list5 = []
# for index in range(1, 11):
#     if index % 2 == 0:
#         index **= 3
#         list5 += [index]
# print(list5)
#
# list5 = [index for index in range(1, 11) if index % 2 == 0]
# print(list5)
# numb =
# new_lst = []
# for index in range(1, 6):
#
#     new_lst += ((index, index ** 3),)
#     new_lst.append((index, index ** 3),)
# print(new_lst)

# new_list = [(item, item ** 3) for item in range(1, 6)]
# print(new_list)
#
# list_multiples = []
# for index in range(1, 30):
#     if index % 3 == 0:
#         list_multiples += [index]
# print(list_multiples)
#
# list_multiples1 = []
# for index in range(3, 30, 3):
#     list_multiples1 += [index]
# print(list_multiples)
#
# list_multiples = [index for index in range(1, 30) if index % 3 == 0]
# print(list_multiples)
#
# list_multiples3 = [index for index in range(3, 30, 3)]
# print(list_multiples3)

# numb = [19, 21, 1, 30, 92, 27, 18, 17, 11]
# for number in (index ** 2 for index in numb if index % 2 != 0):
#     print(number, end='  ')

# loop = (index ** 2 for index in numb if index % 2 != 0)
# print(loop)
#
# Ajanaku = list(index ** 3 for index in [10, 3, 7, 1, 9, 4, 2] if index % 2 == 0)
# print(Ajanaku)

# numbers = [2, 13, 19, 11, 17, 22, 82]


# def odd_values(index):
#     return index % 2 != 0
#
# #
# print(list(filter(odd_values, numbers)))
# # print([index for index in numbers if odd_values(index)])
# print(list(filter(lambda index: index % 2 != 0, numbers)))

# numbers = [3, 12, 14, 23, 29]

# print(list(map(lambda index: index ** 2, numbers)))
# print([index ** 2 for index in numbers])

# print(list(map(lambda index: index ** 2,
# filter(lambda index: index % 2 != 0, numbers))))
# print(numbers)
# print([index ** 2 for index in numbers if index % 2 != 0])


# farenheit = [47, 32, 212]
#
# print(list(map(lambda index: (index, (index - 32) * 5 / 9), farenheit)))
# colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']
# print(min(colors, key=lambda index: index.lower()))
#
# print(max(colors, key=lambda index: index.upper()))
#
# numbers = [11, 12, 13, 15, 16, 17, 18]
# new_number = [index ** 2 for index in reversed(numbers)]
# print(new_number)

# print(list(map(lambda index: index ** 2,
# filter(lambda index: index in numbers, reversed(numbers)))))

# names = ['Anuoluwa', 'Amole', 'Arindin', 'Ijongbon', 'Alaboyun']
# grades = [4.8, 2.1, 1.04, 3.6, 3.8]
# for name, grade in zip(names, grades):
#     print(f'Name: {name}; CGPA: {grade}')

# foods = ['Cookies', 'pizza', 'Grapes',
#          'apples', 'steak', 'Bacon']
#
# print(min(foods, key=lambda index: index.lower()))

# a = [[77, 68, 86, 73],  # first student's grades
#      [96, 87, 89, 81],  # second student's grades
#      [70, 90, 86, 81]]  # third student's grades
# for row in a:
#     for index in row:
#         print(index, end=' ')
#     print()
#
# for index, row in enumerate(a):
#     for index2, column in enumerate(row):
#         print(f'a{[index]}{[index2]}={column} ', end=' ')
#     print()

# sales = []
# for row in range(len(sales)):
#     for index in range(len(sales[row])):
#         sales[row][index] = 0
#
# a = [[2, 3], [2, 2]]
# for row in range(len(a)):
#     for index in range(len(a[row])):
#         a[row][index] = row + index
#         print(a[row][index], end=' ')
#     print()


# a = [[77, 68, 86, 73], [96, 87, 89, 81]]
# total = 0
# items = 0
# for row in a:
#     for column in row:
#         total += column
#         items += 1
#
# print(total / items, end=' ')
#
# ite = 0
# total2 = 0
# for row in a:
#     ite += len(row)
#     total2 += sum(row)
#
# print(total2 / ite)

# import matplotlib.pyplot as plt
# import numpy as np
# import random
# import seaborn as sns

# rolls = [random.randrange(1, 7) for i in range(600)]
# values, frequencies = np.unique(rolls, return_counts=True)
#
# title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
# sns.set_style('whitegrid')
# axes = sns.barplot(x=values, y=frequencies, palette='bright')
# print(axes)

