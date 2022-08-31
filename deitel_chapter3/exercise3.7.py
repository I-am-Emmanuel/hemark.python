print("My square and cube tables")
print(' ')

print(f'Numbers  Square   Cubes')
for numbers in range(0, 6):
    square = numbers ** 2
    cubes = numbers ** 3

    print(f'{numbers:>2}{square:>10}{cubes:>10}')
