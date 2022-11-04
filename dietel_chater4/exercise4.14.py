import random


def multiplication_table_app_for_junior_class():
    rand1 = random.randint(1, 20)
    rand2 = random.randint(1, 20)
    answer = rand1 * rand2
    question = 0
    while question != answer:
        question = int(input(f'How much is {rand1} times {rand2}?: '))
        if question == answer:
            return 'Very good!'

        elif question != answer:
            print('No, incorrect. Please try again!')


print(multiplication_table_app_for_junior_class())
