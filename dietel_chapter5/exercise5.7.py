def sorted_list(country: list):
    country = sorted(country)
    country = min(country, key=lambda index: index.upper())

    return country


print(sorted_list(country=['Australia', 'Germany', 'Israel', 'Scotland', 'Italy', 'America', 'Nigeria']))


def duplicate_int(numbers: list):
    numbers = [index for index in numbers if index >= 54]
    return numbers


print(duplicate_int(numbers=[82, 10, 99, 100, 58, 22]))
