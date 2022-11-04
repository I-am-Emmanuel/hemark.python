import json


grades_dict = {'grade_book':
                   [{'student_id': 1, 'name': 'Red', 'grade': 'A'},
                    {'student_id': 2, 'name': 'Green', 'grade': 'B'},
                    {'student_id': 3, 'name': 'White', 'grade': 'A'}]}
with open('grades.txt', 'w') as grades:
    json.dump(grades_dict, grades)

with open('grades.txt', 'r') as grades:
    grades_dict = json.dumps(json.load(grades), indent=4)
print(grades_dict)



