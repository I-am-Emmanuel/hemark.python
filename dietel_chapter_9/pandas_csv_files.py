import pandas as pd

df = pd.read_csv('accounts.csv', names=['Account', 'Name', 'Balance'])
print(df)
print()

grade = pd.read_csv('grades.csv', names=['Student_Id', 'Name', 'Grades'])
print(grade)

df.to_csv('accounts_from_dataframe.csv', index=False)
print(df)