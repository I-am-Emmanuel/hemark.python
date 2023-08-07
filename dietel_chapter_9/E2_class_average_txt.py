from pathlib import Path
with open('grades.txt', 'r') as grades:
    grade = (grades.read())
    student_grade = {}
    for ind in grade.split():
        if ind in student_grade:
            student_grade[ind] = 1
            for word, count in student_grade.items():
                print(f'{word:<}{count:>10}')

    print(len(student_grade))

# with Path.open('/task-folder/10002.txt', 'w') as files:
    # print(f'Individual grades = {grade}\nTotal = \nGrade count = {count}\nAverage = ')



    # for index in grade:
    #     grad = []
    #     grad += ([index])
    #     # count = sum(grad)
    #     print(sum(i(grad)))
        # print()
        # print(count)

    # for line in grades.readlines():
    #     grade = []
    #     grade += [line]
    #     # average =
    #     count = len(grade)
    #     print(count)
        # print(grade)
        # total = sum(grade)
        # print(f'Individual grades = {line}\nTotal = {total}\nGrade count = {count}\nAverage = {average}')

