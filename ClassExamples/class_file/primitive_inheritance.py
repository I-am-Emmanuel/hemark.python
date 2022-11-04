# class Doubleit(int):
#     def __new__(cls, value):
#         return super().__new__(cls, value * 2)
#
#
# d = Doubleit(4)
#
#
# class MyList(list):
#     def __setitem__(self, index, value):
#         print('No problem')
#
#     def __getitem__(self, item):
#         print("I can't get anything")
#
#
# l = MyList('Hello')
# l.append(1)
# l[0] = 54
# print(l)
# print(d)
# d += 6
# print(d)


class Doubleit(int):
    def __new__(cls, value):
        return super().__new__(cls, value * 2)


d = Doubleit(4)


class MyList(list):
    def __setitem__(self, index, value):
        print('Called')
        if index < 1:
            raise IndexError('Index can neither be negative nor zero')
        super().__setitem__(index - 1, value)

    def __getitem__(self, index):
        if index < 1:
            raise IndexError('Index can neither be negative nor zero')
        return super().__getitem__(index - 1)


l = MyList('Hello')
# l = MyList
# print(l)
# l.append(1)
l[1] = 54
print(l[5])
