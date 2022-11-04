import random


def two_numbers():
    number1 = random.randint(1, 30)
    number2 = random.randint(1, 30)
    return number1, number2


def question_and_answer(two_numbers, new_count=None):
    question = 0
    count = 0
    numbers = two_numbers()
    number1, number2 = numbers
    answer = number2 * number1

    while answer != -1:
        try:
            question = int(input(f'How much is {number2} times {number1}?: '))

        except ValueError:
            print('You need to enter a number')

        count += 1
        if question != answer and count == 1:
            print('Please try again')
        elif question != answer and count == 2:
            print('Wrong. Try once more!')
        elif question != answer and count == 3:
            print('No. Keep trying')

        if question == answer:
            print('Very good')
            question_and_answer(two_numbers, new_count)
            new_count += 1
        if two_numbers == answer and new_count >= 1:
            print('Very nice')


print(question_and_answer(two_numbers, new_count=0))

#     new_question += 1
# if new_question == 1:
#     print('Nice work!')
#     question_and_answer()

# if question == answer:
#     new_number = two_numbers()
#     new_number1, new_number2 = new_number
#     new_answer = new_number

# return question_and_answer()


# def answers():
#     numbers = two_numbers()
#     number1, number2 = numbers
#     answer = number2 * number1
#     while question_and_answer():
#         print('Nice work')

#
# print(answers())

# question = 0
# count = 0
# # while question != answer:
# while answer != -1:
#     question = int(input(f'How much is {number2} times {number1}?: '))
#     count += 1
#     if question != answer and count == 1:
#         print('No. Please try again')
#     elif question != answer and count == 2:
#         print('Wrong. Try once more!')
#     elif question != answer and count >= 3:
#         print('No. Keep trying')
#     elif question == answer:
#         print('Very good')
#         new_count = +1
#         if question == answer:
#             int(input(f'How much is {number2} times {number1}?: '))
#
#             # new_rand1 = random.randint(1, 30)
#             # new_rand2 = random.randint(1, 30)
#             #     question = int(input(f'How much is {new_rand1} times {new_rand2}?: '))
#
#
#             if question == answer and count >= 2:
#                 print('Nice work!')
#             elif question == answer and count >= 3:
#                 print('keep up the good work!')
#


# print(multiplication_table_machine_for_senior_classes())
