
print("Arithmetic Calculator")

print("Input four numbers and I tell you the addition, product, smallest, largest, and average")
number_counter = 0
addition = 0
product = 1
first_number = 0
second_number = 0
third_number = 0
fourth_number = 0
for numbers in range(4):
    number = int(input("Enter your numbers: "))
    product *= number
    addition += number
    number_counter += 1
    average = addition / number_counter

    if numbers in ([0]):
        first_number += number
    if numbers in ([1]):
        second_number += number
    if numbers in ([2]):
        third_number += number
    if numbers in ([3]):
        fourth_number += number
    all_inputs = first_number, second_number, third_number, fourth_number
    smallest = min(all_inputs)
    largest = max(all_inputs)

print(f'{addition} is equal to the addition of your four numbers')
print(f'{product} is equal to the multiplication of your four numbers')
print(f'{average} is equal to the average of your four numbers')
print(f'{smallest} is the smallest of all your numbers')
print(f'{largest} is the largest of all your numbers' )