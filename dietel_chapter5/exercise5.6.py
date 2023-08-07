def rotate(*args):
    return args


a, b, c = 'Doug', 22, 1984

print(rotate(a, c, a))
print(rotate(c, a, b))
print(rotate(a, b, c))
