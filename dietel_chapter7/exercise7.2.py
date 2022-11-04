import numpy as ar
number = ar.arange(0, 4).reshape(2, 2)
print(number)
print()
cube = number ** 3
print(cube)
print()
add = ar.add(number, 7)
print(add)
print()
multi = ar.multiply(number, 2)
print(multi)