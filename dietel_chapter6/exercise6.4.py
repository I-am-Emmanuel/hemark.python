numb1 = {1, 2, 4, 8, 16} | {1, 4, 16, 64, 256}  # {1,2,4,8,16,64,256}
print(numb1)

numb2 = {1, 2, 4, 8, 16} & {1, 4, 16, 64, 256}  # {1,4,16}
print(numb2)

numb3 = {1, 2, 4, 8, 16} - {1, 4, 16, 64, 256}  # {2,8}
print(numb3)

numb4 = {1, 2, 4, 8, 16} ^ {1, 4, 16, 64, 256}  # {2,8,64,256}
print(numb4)
numb5 = {1, 2, 4, 8, 16} >= {1, 4, 16, 64, 256} # False
print(numb5)