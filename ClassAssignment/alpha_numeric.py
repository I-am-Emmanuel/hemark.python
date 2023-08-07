alpha = ['uja823', 'hu92a', 'heallo832']

lo = sum([len([a for a in x if a.isdigit()]) for x in alpha])
print(lo)


def is_alpha_numeric(lst: list) -> int:
    count = 0
    for index in lst:
        for ind in index:
            if ind.isdigit():
                count += 1
            else:
                continue
    return count


print(is_alpha_numeric(alpha))
