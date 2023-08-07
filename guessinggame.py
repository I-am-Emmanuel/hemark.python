import sys

from random import randint
answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        # print(answer)
        guess = int(input(f'Enter your guessed number between {sys.argv[1]} and {sys.argv[2]}:: '))
        if int(sys.argv[1]) - 1 < guess < int(sys.argv[2]) + 1:
            if guess == answer:
                print('You are a genius!')
                break
        else:
            print(f'I want number between {sys.argv[1]} and {sys.argv[2]}!!')
            continue
    except ValueError:
        print('Bozzo, I want a number!!!')