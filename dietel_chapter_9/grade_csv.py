import pandas as pd

grade = pd.read_csv('grades.csv', names=['Student_Id', 'Name', 'Grade'])

print(grade)