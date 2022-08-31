# product = 10
# while product <= 50:
#     product = product * 3
# print(product)
#
# my_number = 7
# while my_number < 1000:
#     my_number *= 7
# print(my_number)
#
# for character in 'Examination':
#     print(character, end=" ")
# print(" ")
# for character in 'Examination':
#     print(character)
#
# total = 0
# for number in [100, 20, 20]:
#     total += number
# print(total)
#
# totals = 0
# while totals <= 200:
#     totals += number
# print(totals)
#
# toy = 0
# new_toy = 0
# for numbers in [91, 80, 18, 21, 20, 19, 50, 10]:
#     toy += numbers
# print("Toy is", toy)
# while numbers == 210:
#     new_toy = toy + numbers
#     break
# print(new_toy)
#
# for numbers in range(47):
#     print(numbers, end=" ")
#
# grades = 10
# total_score = 0
# for scores in [39, 89, 93, 82, 100, 9, 72, 37, 88, 19]:
#     total_score += scores
#
#     average = total_score / grades
# print("The total scores of the grades = ", total_score)
# print("The average of the grades = ", average)
#
# total = 0  # sum of grades
# grade_counter = 0
# grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]  # list of 10 grades
#
# # processing phase
# for grade in grades:
#     total += grade  # add current grade to the running total
#     grade_counter += 1  # indicate that one more grade was processed
#
#     # termination phase
#     average = total / grade_counter
# print(f'Class average is {average}')
#
# number = 7
# numbers = 5
#
# print(f'{number} times {numbers} equals {number * numbers} ')
# print("Welcome to your average calculator")
# print(" ")
#
# total = 0
# grade_counter = 0
#
#
# grade = int(input("Enter your grades; but press -1 to get result: "))
# while grade != -1:
#     total += grade
#     grade_counter += 1
#     grade = int(input("Enter your grades; but press -1 to get result: "))
#
# if grade_counter != 0:
#     average = total / grade_counter
#     print(f'Class average is equal to {average:.2f}')
# else:
#     print("No grades were entered!")
#
# print("Welcome to your grade calculator")
#
# grade_pass = 0
# grade_fail = 0
#
# for students in range(10):
#     result = int(input("Enter the test result;(1 for pass and 2 for fail): "))
#     if result == 1:
#         grade_pass += 1
#     else:
#         grade_fail += 1
# print(f'{grade_pass} Passed')
# print(f'{grade_fail} Failed')
# if grade_pass >= 8:
#     print("Bonus to the instructor")
#
# for numbers in range(2, 101, 2):
#     print(numbers, end=" ")
#    # print(" ")
#
# for numbers in range(2, 101):
#     if numbers % 2 == 0:
#         print(numbers, end=" ")
#
import decimal
# rate = decimal.Decimal(0.05)
# principal = decimal.Decimal(1000.00)
# amount = 0
#
# for years in range(1, 11):
#     amount = principal * (1 + rate) ** years
#     print(f'{years:>2}{amount:>10.2f}')
#     print(f'{amount:10.2f}')
#
# tax = decimal.Decimal(6.25/100)
# amount = decimal.Decimal(37.45)
#
#
# total_bill = (amount * tax) + amount
#
# print(f'{total_bill:.2f}')

import statistics

scores = [62, 88, 91, 21, 28, 12, 91, 192, 211, 115]

scores = sorted(scores)
mean = statistics.mean(scores)
median = statistics.median(scores)
mode = statistics.mode(scores)

print(scores)
print(f'{mean:.1f} is the mean of the scores')
print(f'{median} is the median of the scores')
print(f'{mode} is the mode of the scores')

grade: int = 90

result = ("Passed" if grade >= 60 else "failed")
print(result)
