import math
count = 0
while count <= 3:
    numbers = int(input("Enter any digit and I will tell you if it is a prime number or not: "))
    if numbers == 1:
        print("This is not a prime number")
    elif numbers != 2 and numbers % 2 == 0:
        print("This is not a prime number")
    elif numbers != 5 and numbers % 5 == 0:
        print("This is not a prime number")
    elif numbers != 7 and numbers % 7 == 0:
        print("This is not a prime number")
    elif numbers != 3 and numbers % 3 == 0:
        print("This is not a prime number")
    else:
        print("This is a prime number")
    count +=1






