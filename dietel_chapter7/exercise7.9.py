import numpy as re
number = re.arange(1, 16).reshape(3, 5)
print(number)
print()
row2 = number[1]
print(row2)
print()
col5 = number[:, 4]
print(col5)
print()
row0_1 = number[:2]
print(row0_1)
print()
column2_4 = number[:, 1:4]
print(column2_4)
print()
row_1_column_4 = number[0, 3]
print(row_1_column_4)
print()
row1_row_2column = number[1:3, (0, 2, 4)]
print(row1_row_2column)