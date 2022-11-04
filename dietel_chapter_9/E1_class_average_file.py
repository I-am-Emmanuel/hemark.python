
with open('grades.txt', 'w') as grades:
    try:
        grade_question = int(input('How many grades do you want to input:: '))
        for ind in range(grade_question):
            grade = [int(input('Enter your student score:: '))]
            for index in grade:
                grades.writelines([f'{index}\n'])
    except ValueError:
        print('Your input should be number!')




#
#
# with open('grades.txt', 'w') as grades:
#     try:
#         grade_question = int(input('How many grades do you want to input:: '))
#         for ind in range(grade_question):
#             grade = [int(input('Enter your student score:: '))]
#             for index in grade:
#                 grades.writelines([f'{index}\n'])
#     except ValueError:
#         print('Your input should be number!')




