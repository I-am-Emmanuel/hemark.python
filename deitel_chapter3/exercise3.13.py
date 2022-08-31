print("Enter any number and I give you its factor")

numbers = int(input("Enter your number: "))

for number in range(1, numbers + 1):
    if numbers % number == 0:
        print(f'{number:>5}', end='')

