try:
    grade: int = int(input("Enter your Score: "))
    if 70 <= grade <= 100:
        print("Your grade is A")
    elif 60 <= grade <= 69:
        print("Your grade is B")
    elif 50 <= grade <= 59:
        print("Your grade is C")
    elif 45 <= grade <= 49:
        print("Your grade is D")
    elif grade <= 44:
        print("Your grade is F")
except ValueError:
    print('Your input should be a number')

