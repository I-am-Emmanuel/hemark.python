print("Enter two numbers and I will tell you how they relate")
first_digit = int(input("Enter your first number: "))
second_digit = int(input("Enter your second number: "))

if first_digit > second_digit:
    print(first_digit, "is greater than", second_digit)
if first_digit < second_digit:
    print(second_digit, "is greater than", first_digit)
if first_digit == second_digit:
    print(first_digit, "and", second_digit, "are the same\n", first_digit, "not greater than", second_digit, "\n",
          second_digit, "not lesser than", first_digit)
if first_digit != second_digit:
    print(first_digit, "not equal to", second_digit)
if second_digit != first_digit:
    print(second_digit, "not equal to", first_digit)
