import random


def two_numbers():
    number1 = random.randint(1, 30)
    number2 = random.randint(1, 5)
    return number1, number2


def question_and_answer(two_numbers):
    question = 0
    numbers = two_numbers()
    number1, number2 = numbers
    answer = number2 * number1
    good_responses = ['Very good', 'Very nice', 'Correct, Keep it up']
    other_responses = ['No! Please try again', 'Wrong, try once more', 'No, Keep trying']

    while answer != -1:
        try:
            question = int(input(f'How much is {number2} times {number1}?:: '))

        except ValueError:
            print('You need to enter a number')

        if question != answer:
            response = random.choice(other_responses)
            print(response)

        if question == answer:
            response = random.choice(good_responses)
            print(response)
            question_and_answer(two_numbers)


print(question_and_answer(two_numbers))
