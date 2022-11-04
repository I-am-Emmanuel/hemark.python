def reverse_func(lst):
    numb = lst
    index = -1
    arrange = [None] * len(numb)

    for item in numb:
        arrange[index] = item
        index -= 1
    numb = arrange
    return numb


print(reverse_func(lst=[-1, 2, -5, 100, -9, 20]))


def sort_func(lst):

    nas = lst
    arrange = sorted(nas)
    return arrange


# print(sort_func(list=[8, 92, 10,74, 32]))
print(sort_func([8, 29, 100, 32, 83]))
print(reverse_func([83, 'gas', 89, {'key': [82]}]))



