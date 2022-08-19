print("Enter an integer and I tell you if it is and odd or even")

number = int(input("Enter your number: "))
if number % 2 == 0:
    print(number, "is an even number")
if number % 2 == 1:
    print(number, "is an odd number")
