def prime_number(number: int):
    for number in range(2, 1000):
        number = True
        for count in range(2, 500):
            if number % count == 0:
                number = False
    return number



print(prime_number(1000))
