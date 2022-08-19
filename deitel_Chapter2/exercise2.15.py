print("")
print("Enter any three numbers and I will arrange them both in,"
      " ascending and descending order")

number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))
number_3 = int(input("Enter your third number: "))

smallest = number_1
if number_2 < number_1:
    smallest = number_2
if number_3 < smallest:
    smallest = number_3

smaller = number_1, number_2, number_3
if number_1 >= number_2 >= number_3:
    smaller = number_2
if number_2 >= number_3 >= number_1:
    smaller = number_3
if number_3 >= number_2 >= number_1:
    smaller = number_2
if number_2 >= number_1 >= number_3:
    smaller = number_1
if number_1 >= number_3 >= number_2:
    smaller = number_3
if number_3 >= number_1 >= number_2:
    smaller = number_1

small = number_1
if number_2 > number_1:
    small = number_2
if number_3 > small:
    small = number_3

print("This is your number in ascending order of size: ", smallest, smaller, small)
print("This is your number in descending order of size: ", small, smaller, smallest)



