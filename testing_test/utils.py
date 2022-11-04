def add(x, y):
    assert x >= 0 and y >= 0, 'numbers cannot be negative'
    assert isinstance(x, (int, float)) and isinstance(y, (int, float)), 'only numbers is allowed'

    return x + y


print(add(5, 9))
