import statistics

print("Enter any ten numbers and I will give you the two largest of them")

first_number = 0
second_number = 0
third_number = 0
fourth_number = 0
fifth_number = 0
sixth_number = 0
seventh_number = 0
eight_number = 0
ninth_number = 0
tenth_number = 0
for numbers in range(10):
    number = int(input("Enter your numbers: "))
    if numbers in ([0]):
        first_number += number
    if numbers in ([1]):
        second_number += number
    if numbers in ([2]):
        third_number += number
    if numbers in ([3]):
        fourth_number += number
    if numbers in ([4]):
        fifth_number += number
    if numbers in ([5]):
        sixth_number += number
    if numbers in ([6]):
        seventh_number += number
    if numbers in ([7]):
        eight_number += number
    if numbers in ([8]):
        ninth_number += number
    if numbers in ([9]):
        tenth_number += number

    inputs = first_number, second_number, third_number, fourth_number, fifth_number, sixth_number, seventh_number, + \
        eight_number, ninth_number, tenth_number
    ascend = sorted(inputs)
    first_largest = ascend[-1]
    second_largest = ascend[-2]

print(f'{first_largest} is the first largest number')
print(f'{second_largest} is the second largest number')
