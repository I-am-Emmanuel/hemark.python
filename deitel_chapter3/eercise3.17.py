print('Pattern of different shapes')

print("(a)")
for numbers in range(1, 11):
    asteric = numbers * '*'
    print(asteric)
print("")
print()


print("(b)")
for number in range(10, 0, -1):
    asteric_b = '*' * number
    print(asteric_b)




print("(c)")
for number in range(10, 0, -1):
    asteric_c = '*' * number
    print(asteric_c.rjust(10))


print("(d)")
for number in range(1, 11):
    asteric_d = '*' * number
    print(asteric_d.rjust(10))
