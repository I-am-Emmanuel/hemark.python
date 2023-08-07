def word_problem(question: str):
    figures = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    signs = {
        'minus': f'{45:c}',
        'plus': f'{43:c}',
        'divided_by': '/',
        'times': '{:c}'.format(42)
    }
    for word in question.split():
        if word in signs.keys():
            number1, sign, number2 = question.partition(word)
            # number1 = number1.strip()
    for fig, value in figures.items():
        if fig == number1.strip():
            result = value
    for k, v in signs.items():
        if k == sign.strip():
            result2 = v

    for fig, value in figures.items():
        if fig == number2.strip():
            result3 = value

    # numb = 'result2'.join(result3)

    res = eval(str(result) + result2 + str(result3))

    #         raise ValueError('I dont have your input in my data')
    #     return f'{fig}: {value}'
    return res


print(word_problem('five divided_by two'))
# signs = {
#         'minus': f'{45:c}',
#         'plus': f'{43:c}',
#         'divided by': '{:c}'.format(47),
#         'times': '{:c}'.format(42)
#     }
#
# for k, v in signs.items():
#     if 'minus' in signs:
#         return 7 + 9
# question = 'five plus two'
# for word in question.split():
#     if word in signs:
#         number1, sign, number2 = question.partition(word)
# print(sign)
# print(word_problem('five + two'))
# print('add' in signs.keys())
