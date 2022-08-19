print("Enter any number and I will give you the product, addition,"
      " the smallest, the largest, and the difference in them.")
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
total_input = 3

addition = first_number + second_number + third_number
subtraction = first_number - second_number - second_number
product = first_number * second_number * third_number
average = (first_number + second_number + third_number) / total_input

smallest = first_number
if second_number < first_number:
    smallest = second_number
if third_number < smallest:
    smallest = third_number

largest = first_number
if second_number > first_number:
    second_number = largest
if third_number > largest:
    largest = third_number

print("The sum of your numbers is", addition)
print("The difference of your numbers is", subtraction)
print("The product of your number is", product)
print("The average of your number is", average)
print("The smallest of your numbers is", smallest)
print("The largest of your numbers is ", largest)
