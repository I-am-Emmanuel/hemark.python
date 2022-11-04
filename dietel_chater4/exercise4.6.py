def average_num(number: list):
    average = sum(number) / len(number)
    return average


print(average_num(number=[6, 77, 12, 98]))


def average_arbit(*args):
    average = sum(args) / len(args)
    return average


print(average_arbit(7, 77, 43, 21))
