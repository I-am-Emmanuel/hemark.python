grade: int = int(input("Enter your Score: "))
if grade >= 70:
    print("Your grade is A")
elif grade >= 60 and grade <= 69:
    print("Your grade is B")
elif 50 <= grade <= 59:
    print("Your grade is C")
elif 45 <= grade <= 49:
    print("Your grade is D")
elif grade <=44:
    print("Your grade is F")