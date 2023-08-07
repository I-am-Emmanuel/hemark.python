def add_str(lst: list, k: int):
    new = []
    cont = []
    ind = 0
    deleter = 0
    for index in lst:
        new.append(index)
        del lst[deleter]
        # result = k - new[ind]
        for i in lst:
            # nuu = new[ind] + i
            # print(nuu)
            if k - new[ind] == i:
                print(i)
            #     cont.append(str(new[ind]) + '+' + str(i))
        ind += 1
    # return cont


print(add_str([14, 2, 67, 4, 6, 8], 8))

# def add_str(lst: list, k: int):
#     new = []
#     cont = []
#     ind = 0
#     for index in lst:
#
#
#     return new
#
#
# print(add_str([4, 2, 9, 4, 6, 8], 8))
