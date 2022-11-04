
print('Enter your any word and I will turn it into pig-Latin language for you')
text = input('Enter your word:: ')
prefix = 'ay'
vowels = 'a', 'e', 'i', 'o', 'u'
for letter in text.split():
    if letter.startswith(vowels):
        new_word = text + 'ay'
        print(new_word)
    else:
        index = letter.strip(letter[1:])
        rind = letter.lstrip(letter[:1])
        new_word = rind + index + 'ay'
        print(new_word)


# new = text.strip(text[:1])
# new_1 = text.strip(text[1:])
# if text.startswith(vowels):
#     news = text + prefix
#     print(news)
# else:
#     news = new + new_1 + prefix
#     print(news)


