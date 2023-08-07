numbs = [2, 3, 100, 20, 12, 60, 1, 8, 65, 5]


def max_sum(numb: list) -> int:
    index = 0
    index2 = len(numbs)
    new_num = 0
    count = 0
    new_numbs = 0

    while count != len(numb) // 2:
        new_numbs += numbs[index]
        new_num += numbs[index2 - 1]
        index += 1
        index2 -= 1
        count += 1
    if new_numbs > new_num:
        return new_numbs
    else:
        return new_num


print(max_sum(numb=numbs))

numbs = [2, 3, 100, 20, 12, 60, 1, 8, 65, 5]


def first_four(number: list) -> int:
    index = 0
    index2 = 1
    count = 0
    temp1 = 0
    temp2 = 0

    while index2 != len(number):
        temp1 += number[index]
        temp2 += number[index2]
        index += 1
        index2 += 1
        count += 1
        if count == 4:
            if temp1 > temp2:
                new_temp = temp1
            else:
                new_temp = temp2

