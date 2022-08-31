# if 1:
#     print("Non zero values are true, so this will print")
# if 0:
#     print("Zero is false, so this values will not print")
# if 4:
#     print("nuau")
#
# a = b = 7
# print('a =', a, '\nb =', b)

for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 0 else '>', end='')
print()