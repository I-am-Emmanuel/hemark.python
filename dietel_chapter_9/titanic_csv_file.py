import pandas as pd

titanic = pd.read_csv('https://vincentarelbundock.github.io/' +
                      'Rdatasets/csv/carData/TitanicSurvival.csv')

# print(pd.set_option('precision', 2))
print(titanic.head())
# print(titanic.tail())

# titanic.columns = ['name', 'survived', 'sex', 'age', 'class']
# print(titanic.head())
# print(titanic.tail())
print()
# print(titanic.describe())
print()
# print((titanic.survived == 'yes').describe())



