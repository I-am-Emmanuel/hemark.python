def sumlst(x):
    assert isinstance(x, list), 'You should pass in a list'
    numbers = 0
    for index in x:
        numbers += index
    return numbers


b = 9, 10
c = [9, 10, 32]
d = (8, 9, 10)
print(sumlst(x=d))
