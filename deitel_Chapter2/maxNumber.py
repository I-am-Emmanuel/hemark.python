print("Enter three numbers and I tell you which is greatest")
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
number3 = int(input("Enter your third number: "))
maximum = number3
if number2 > number3:
    maximum = number2
if number1 > maximum:
    maximum = number1
print(maximum, "is the greatest of them")

loft = max(923, 882, 9911, 193, 100038)
print(loft, "is the greatest of all")