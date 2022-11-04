import random
from timeit import timeit

import numpy as np
# numbers = np.array([2, 3, 5, 7, 11])
#
# print(numbers)
#
# array = np.array([[1, 2, 3], [4, 5, 6]])
# print(array)
# array = ([[1, 2, 3], [4, 5, 6]])
# print(array)
#
# array = np.array([x for x in range(0, 20, 2)])
# print(array)
#
# array = np.array([[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]])
# print(array)
#
# integers = np.array([[1, 2, 3], [4, 5, 6]])
# print(integers)
#
# floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.7]).reshape(3,2)
# print(floats)
#
# float = floats.dtype
# print(float)
#
# float = floats.itemsize
# print(float)

a = np.array([[2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 3, 5, 7, 9]])
for row in a:
    for column in row:
        print(column, end=' ')
    print()

a = a.ndim
print(a)
#
# p = integers.shape
# print(p)


# array = np.full((2, 3), 15)
# print(array)
#
# array = np.ones((3, 2), dtype=int)
# print(array)
#
# array = np.zeros(8)
# print(array)
#
#
# array = np.ones(10)
# print(array)

# array = np.arange(10, 1, -2)
# print(array)
#
#
# array = np.arange(1, 81, 3).reshape(3, 9)
# print(array)
#
# array = np.linspace(0.0, 1.0, num=4)
# print(array)
#
# array = np.arange(1, 21).reshape(4, 5)
# print(array)

# array = np.arange(1, 100001).reshape(4, 25000)
# print(array)
# print()
#
# array = np.arange(1, 100001).reshape(100, 1000)
# print(array)

# array = np.arange(2, 41, 2).reshape(4, 5)
# print(array)
import random
import time

start_time = time.time()
# number_rolls = [random.randrange(1, 7) for number in range(0, 6000000)]
# print(number_rolls, "--- %s seconds ---" % (time.time() - start_time))

# rolls_array = np.random.randint(1, 7, 60_000_000)
# print(rolls_array, "--- %s seconds ---" % (time.time() - start_time))

# array = sum([index for index in range(10000000)])
# print(array, "--- %s seconds ---" % (time.time() - start_time))

# array = np.arange(10000000).sum()
# print(array, "--- %s seconds ---" % (time.time() - start_time))

# numbers = np.arange(1, 6)
# print(numbers)

# numbers = numbers * 2
# print(numbers)
# numbers = numbers ** 3
# print(numbers)
# print()
#
# numbers += 10
# print(numbers)
#
# numbers2 = np.linspace(1.1, 5.5, 5)
# print(numbers2)
#
# numbers = numbers * numbers2
# print(numbers)

# numbers = np.arange(10, 16)
# print(numbers)
# numbers = numbers >= 13
# print(numbers)
# numbers = numbers <= 12
# print(numbers)

# comp = numbers == numbers2
# print(comp)
# comp = numbers >= numbers2
# print(comp)


# numb = np.arange(1, 60000) ** 2
# print(numb, (time.time() - start_time))

# number = [index ** 2 for index in range(1, 60000)]
# print(number, (time.time() - start_time))

# grades = np.array([[87, 96, 70], [100, 87, 90],
#                  [94, 77, 90], [100, 81, 82]]).mean(axis=1)
#
# grade = sorted(grades)
# print(grade)

# grade = np.random.randint(60, 101, 12).reshape(3, 4)
# grades = grade.mean(axis=0)
# grades2 = grade.mean(axis=1)
# mean = grade.mean()
# print(mean)
# print(grade)
# print()
# print(grades)
# print()
# print(grade)
# print()
# print(grades2)
#
# numbers = np.array([1, 4, 9, 16, 25, 36])
# number = np.sqrt(numbers)
# print(number)
#
# number2 = np.arange(1, 7) * 10
# print(number2)
# add_array = np.add(numbers, number2)
# print(add_array)
#
# mul = np.multiply(number2, 8)
# print(mul)
#
# arr_num = np.array(number2).reshape(2, 3)
# print(arr_num)
#
# numbe4 = np.random.randint(10, 23, 2)
# print(numbe4)

# numb = np.arange(1, 6)
# cube = np.power(numb, 3)
# print(cube)

grades = np.array([[87, 96, 70], [100, 87, 90],
                   [94, 77, 90], [100, 81, 82]])
print(grades)
# print()
#
#
# print(grades[1])
# print()
# print(grades[[1, 3]])
# print()
# print(grades[2, 0])
# print()
# print(grades[:])
# print()
# print(grades[:, 2])
# print(grades[:, 1:2])
# print(grades[:, 2:3])
# print(grades[:, 0:1])

# loft = np.arange(1, 16).reshape(3, 5)
# print(loft)
# print()
# print(f'Second row = {loft[1]}')
# print()
# print(f'First and Third row = {loft[[0, 2]]}')
# print()
# print(f'The middle three columns = {loft[:, 1:4]}')


# first = np.arange(1, 6)
# print(first)
# print()
# new = first.view()
# print(new)
#
# print(id(new))
# print(id(first))
#
# first[1] += 10
# print(first)
# new[0] *= 10
# print(new)
# print(first)

# digit = np.arange(1, 6)
# print(digit)
# print()
# nomba = digit[0:3]
# print(digit)
# print(nomba)
# digit[2] *= 5
# print(digit)
# print(nomba)
# nomba[0] -= 1
# print(digit)
# print(nomba)


# kiki = np.arange(1, 11, 2)
# # print(kiki)
# print(id(kiki))
# lola = kiki.copy()
# print(id(lola))
# print(kiki)
# print(lola)
# kiki[2] *= kiki[1]
# print(kiki)
# print(lola)
# lola[2] += lola[4]
# print(kiki)
# print(lola)

# numb = np.arange(50, 60).reshape(2, 5)
# print(numb)
#
# number = numb.reshape(1, 10)
# print(numb)
# print(number)
# print(numb)
#
# flattened = numb.flatten()
# print(flattened)
# flattened[0] *= 20
# print(flattened)
# numb[0, 4] = 75
# print(numb)
# print(numb.T)
# print(numb)
# numb[1, 0] = 63
# print(numb)
# print(numb.T)
# print(flattened)


# numbs = np.arange(50, 60).reshape(2, 5)
# print(numbs)
# raveled = numbs.ravel()
# print(raveled)
# raveled[3] = 90
# print(numbs)
# print(raveled)
# print(numbs.T)
# print(numbs)


# grade = np.arange(1, 7).reshape(2, 3)
# print(grade)
# grade = np.hstack((grade, grade))
# print(grade)
# grade = np.vstack((grade, grade))
# print(grade)


import pandas as py

# idanwo = py.Series([87, 100, 94, 89, 91, 78])
# print(idanwo)
#
# print(idanwo.count())
# print(idanwo.mean())
# print(idanwo.max())
# print(idanwo.min())
# print(idanwo.std())
# print(idanwo.sum())
# print(idanwo.describe())
#
#
#
#
# # number = py.Series(98.6, range(3))
# # print(number)
#
#
# grades = py.Series([87, 100, 94, 89, 91, 78], index=['Sade', 'Raphael', 'Samson', 'Joy', 'Kimbally', 'Kounde'])
# print(grades)
#

result = py.Series({'Willy': 82, 'Dan': 90, "Sow": 30, 'Jade': 62})
# print(result)

lone = result['Sow']
# print(lone)

# esi = result.Kiki
# print(esi)

esis = result.values
# print(esis)

# name = py.Series(['Sade', 'Raphael', 'Samson', 'Joy', 'Kimbally', 'Kounde'])
# print(name)
#
# aaas = name.str.endswith('b')
# print(aaas)

# temp = np.random.randint(60, 101, 5)
# print(temp)
# temperature = py.Series(temp)
# print(temperature)
# temp_lowest = temperature.min()
# print(temp_lowest)
# temp_maximum = temperature.max()
# print(temp_maximum)
# average_temp = temperature.mean()
# print(average_temp)
# describe = temperature.describe()
# print(describe)
#
# grades_pack = (
#     {'Ade': [83, 73, 90, 100], 'Sola': [37, 64, 27, 72], 'Sade': [47, 50, 93, 28], 'Raphael': [82, 73, 29, 91],
#      'Samson': [83, 73, 92, 61], 'Joy': [83, 40, 73, 55], 'Kimbally': [39, 74, 50, 89], 'Kounde': [100, 74, 65, 92]})
# grades = py.DataFrame(grades_pack)
# # print(grades)
#
# grades.index = ['Test 1', 'Test 2', 'Test 3', 'Test 4']
# print(grades)
#
# raph = grades['Raphael']
# print(f'Raphael result = {raph}')
#
# raph2 = grades.Sade
#
# print(f"Sade's results = {raph2}")
#
# result = grades.loc['Test 3']
# print(result)
#
# resul = grades.iloc[3]
# print(resul)
#
# new_result = grades.loc['Test 1': 'Test 4']
# print(new_result)

# jerry = grades.iloc[0:3]
# print(jerry)

# ind_result = grades.loc[['Test 1', 'Test 4']]
# print(ind_result)

# ind_result2 = grades.iloc[[1, 2]]
# print(ind_result2)
#
# spe_result = grades.loc['Test 1': 'Test 3', ['Sade', 'Joy', 'Kimbally']]
# print(spe_result)
#
# sp_result = grades.iloc[[0, 3], 3:]
# print(sp_result)

# above_70 = grades[grades >= 70]
# print(above_70)
#
# next_grade = grades[(grades >= 40) & (grades < 50)]
# print(next_grade)
#
# Raphael = grades.at['Test 4', 'Raphael']
# print(Raphael)
#
# sade = grades.iat[2, 2]
# print(sade)
#
# grade_change = grades.at['Test 1', 'Sola'] = 89
# print(grade_change)
# print(grades)
#
# grade_change2 = grades.iat[3, 2] = 50
# print(grade_change2)
# print(grades)
#
# grade = grades.describe()
# print(grade)
#
# results = grades.sum()
# # print(results)
#
#
# results2 = grades.mean()
# print(results2)
# sort_result = sorted(results2, reverse=True)
# print(sort_result)

# total_avg = results2.mean()
# print(total_avg)

# other_wise = grades.T
# print(other_wise)

# samson = grades.at['Test 3', 'Raphael'] = 82
# print(samson)
# print(other_wise)
# print(grades.T)
# print(grades)

# print(gra

# arrange_grade = grades.sort_values(by='Test 4', axis=1, ascending=False)
# print(arrange_grade)
# sade = grades.iat[0, 2] = 72
# one_result = grades.iloc[0].sort_values(ascending=False)des.T.mean())
# #
# # arrange = grades.sort_index(ascending=False)
# # print(arrange)
# #
# # arrange2 = grades.sort_index(axis=1)
# # print(arrange2)
# print(one_result)
#
#
# # print(sade)
# print(grades)
# print(one_result)