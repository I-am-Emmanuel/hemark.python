calendar = {'January': 31, 'February': 28, 'March': 31}
# print(calendar)
# for month, days in calendar.items():
#     print(f'{month} has {days} days')
# print(len(calendar))
# if calendar:
#     print('Calendar is not empty')
# else:
#     print('Calendar is empty')
# # calendar.clear()
# if calendar:
#     print('Calendar is not empty')
# else:
#     print('Calendar is empty')
#
# print(calendar['January'])
# calendar['April'] = 30
# print(calendar)
# calendar['Alagbado'] = 71
# print(calendar)
# del calendar['Alagbado']
# print(calendar)

# calendar.pop('Alagbado')
# print(calendar)
# print(calendar.get('Alagbado'))
# print(calendar)
# print(calendar.get('Alagbado'))
# print('April' in calendar)
# print('January' not in calendar)
# print('Alagbado' not in calendar)
# calendar['May'] = 38
# print(calendar)
# calendar['May'] = 31
# print(calendar)
# calendar['may'] = 31
# print(calendar)
#
# for month, days in calendar.items():
#     print(month, end=' ')
# print()
#
# for month in calendar.keys():
#     print(month, end=' ')
#
# for numbers in calendar.values():
#     print(numbers)

# osu = calendar.items()
# for days, month in osu:
#     print(days, month, end=' ')
# print()
#
# calendar.pop('may')
# print(calendar)
# for month, days in osu:
#     print(month, days)

# print(list(calendar.items()))
#
# for month in sorted(calendar.keys()):
#     print(month, end=' ')
#
import random
#
# grade_book = {
#     'Susan': [92, 85, 100],
#     'Eduardo': [83, 95, 79],
#     'Azizi': [91, 89, 82],
#     'Pantipa': [97, 91, 92]
# }
#
# total_score = 0
# count = 0
#
# for name, scores in grade_book.items():
#     total = sum(scores)
#     print(f'Average for {name} is {total/len(scores):.2f}')
#     count += len(scores)
#     total_score += total
# print(f'Total Class Average is {total_score/count:.2f}')

# text = ('this is sample text with several words '
#         'this is more sample text with some different words')
# word_count = {}
#
# for word in text.split():
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# print(f"WORD {'COUNT':>12}")
#
# for word, count in sorted(word_count.items()):
#
#     print(f'{word:<12} {count}')
#     unique = len(word_count)
# print(f'The Unique word = {unique}')

from collections import Counter

#
# text = ('this is sample text with several words '
#         'this is more sample text with some different words')
#
# counter = Counter(text.split())
#
# print(f"{'WORD':<12}{'COUNT'}")
#
# for words, count in sorted(counter.items()):
#     print(f'{words:<12} {count}')
#
# print(f'Numbers of unique keys is {len(counter.keys())} ')


# numbers = [random.randrange(1, 6) for index in range(50)]
# print(numbers)
# count = Counter(numbers)
#
# for key, values in sorted(count.items()):
#     print(f'{key:<10}{values}')

# country = {}
#
# country.update({'Germany': 'gr'})
# country.update(Nigeria= 'ger')
# country.update(Nigeria= 'ngr')
# country.update({'Nigeria': 'ng'})
# print(country)
# country.pop('Germany')
# del country['Nigeria']
# print(country)
# country['Ghana'] = 'Ghn'
# print(country)
#
# month = {'January': 1, 'February': 2, 'March': 3, 'April': 4}
# print(month)
# month_two = {number: months for months, number in month.items()}
# print(month_two)

# grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}
#
# average_result = {name: sum(grade) / len(grade) for name, grade in grades.items()}
# print(average_result)
#
# number = {numb: numb ** 3 for numb in range(1, 6)}
# print(number)
#
# # SETS
# fruits = {'Mango', 'Pine-apple', 'Guava', 'Tangerine', 'Mango', 'Apple', 'Lemon', 'Banana'}
# print(fruits)
# print(sorted(fruits))
# print(len(fruits))
#
# check = 'Lime' in fruits
# print(check)
#
# for fruit in fruits:
#     print(fruit.upper(), end='  ')
# print()
#
# numbers = list(range(10)) + list(range(5))
# print(numbers)
# #
# number = set(numbers)
# print(number)
#
text = 'to be or not to be that is the question'
#
# new_text = set(text.split())
# print(new_text)
# sort_text = sorted(new_text)
# for sort in sort_text:
#     print(sort, end=' ')
# print()
#
# sub = {1, 3, 5}.issubset({3, 5, 1})
# print(sub)
#
# subs = set('abc def ghi').issuperset('hi')
# print(subs)


# MATHEMATICAL SETS OPERATORS
# diff = {10, 20, 30} - {5, 10, 15, 20}
# print(diff)
#
# new_diff = {10, 20, 30} ^ {5, 10, 15, 20}
# new_diffs = {10, 20, 30}.symmetric_difference({5, 10, 15, 20})
# print(sorted(new_diff))
# print(new_diffs)
#
# hum = {10, 20, 30} | {5, 10, 15, 20}
# print(sorted(hum))
# # {5, 10, 15, 20, 30}
#
#
# jo = {10, 20, 30} & {5, 10, 15, 20}
# print(sorted(jo))
#
#
# # Mutable sets
#
# lok = {10, 20, 30}
# lok = {5, 10, 15, 20}
# print(sorted(lok))
#
# lok.update(range(5, 20, 2))
# print(lok)

# import statistics
# x = [44, 55, 57, 85, 65, 60, 50, 42, 38]
# m = statistics.pstdev(x)
# p = statistics.stdev(x)
# print(m)
# print(p)


calend = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September',
          10: 'October',
          11: 'November', 12: 'December'}


def bring_calendar(cal: dict) -> str:
    rand = random.randint(1, 18)
    for key, val in cal.items():
        if rand in cal:
            if rand == key:
                return val
        else:
            return 'Not valid'


print(bring_calendar(calend))
# result = {x for x, m }

# print(rand)
