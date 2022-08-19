print("Enter any number and I will tell you which is the smallest of all")
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
number3 = int(input("Enter your third number: "))

minimum = number2
if number1 < number2:
    minimum = number1
if number3 < minimum:
    minimum = number3
print(minimum, "is the smallest number of all.")

loft = min(73, 92, 0.1, 88)
print(loft, "is the smallest of all")