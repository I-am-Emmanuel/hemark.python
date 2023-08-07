def calculate_vowels(sentence):

    vowels = 'aeiou'
    count = 0
    for i in vowels:
        for j in sentence:
            if i == j:
                count += 1

    return f'There are {count} vowels in your sentence altogether'


print(calculate_vowels('John is a good boy'))
