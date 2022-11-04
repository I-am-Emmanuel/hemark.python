from copy import deepcopy

print("Welcome to your Students grade calculator\nYou can only enter your students name at a time.")


def get_student_name_and_student_grades():
    class_average = 0
    big_list = []
    question = int(input('How many student did you have?:: '))
    for response in range(question):
        name = input('Enter your students name and press the enter key:: ')
        each_score = {}
        grade = []
        quest_2 = int(input('How many grades did you want to enter for this student?:: '))
        for index in range(quest_2):
            grade += [(int(input('Enter your students score:: ')))]
        each_score[name] = grade
        big_list.append(each_score)
    big_list_clone = deepcopy(big_list)
    all_grades_count = 0
    all_grades_total = 0
    for index, elem in enumerate(big_list_clone):
        for key, value in elem.items():
            total = sum(value)
            average = total / len(value)
            big_list[index]['total'] = total
            big_list[index]['average'] = average
            all_grades_total += total
            all_grades_count += len(value)
            class_average = all_grades_total / all_grades_count

    return f'{big_list}\nClass Average = {class_average}'


print(get_student_name_and_student_grades())
