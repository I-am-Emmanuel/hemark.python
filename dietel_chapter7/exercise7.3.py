import numpy as ar

even_arr = ar.arange(2, 19, 2).reshape(3, 3)
print(even_arr)
print()
other_numb = ar.arange(9, 0, -1).reshape(3, 3)
print(other_numb)
print()
multiple = even_arr * other_numb
print(multiple)