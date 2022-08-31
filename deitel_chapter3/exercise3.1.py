print("Enter any number between 1 - 50 ten times and,"
      " lets see number of times you can guess right")


correct = 0
wrong = 0
for numbers in range(10):
    number = int(input("Enter your number between 1 - 50: "))

    if number == 1 or number == 2 or number == 26 or number == 47 or number == 38:
        correct += 1
    else:
        wrong += 1

print(f'{correct} of your inputs are correct')
print(f'Sorry {wrong} inputs are wrong!')

if correct > 3:
    print("Congratulations, You won!!!")
else:
    print("Better luck next time, You may try again later")
