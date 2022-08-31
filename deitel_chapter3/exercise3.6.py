print("Welcome to your simple medical diagnosis computer test")

questions1 = str(input("What is your problem?: "))
questions2 = str(input("Have you had this problem before(Yes or no)?: "))

if questions2.lower() == 'yes' or questions2.upper() == "Yes":
    print("Well, you have it again")
else:
    print("Well, You have it now")
