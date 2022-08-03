import random
random_number: int = random.randint(0, 10)
count = 1
while (count <= 3):
    guess_number: int = int(input("Guess a number: "))
    if guess_number == random_number:
        print("Congratulations!!!\nYou got it right")
        break
    elif guess_number > random_number:
        print("The number is too high, kindly try again")
    elif guess_number < random_number:
        print("The number is too low, please try again")

    count += 1
else:
    print("Your trial is exhausted")
