# import re
#
# #
# letter = ['mango', 'kill,go, lit, hill, man']
# # slice1 = letter[0]
# # slc = re.split(r',\s*', slice1)
# new_word = re.search(letter[0][:], letter[1])
# new_word = new_word.group() if new_word else 'Not found'
# # print(new_word)
# token = 'md8kgwco'
# word = 'softwaredevelopment'
# # for index in word.split():
# # slice = index.split(', ')
# # print(index.split(,))
# street = re.split(r'\token+', '123$Main$$Street')
# # print(street)
# join = word + token
#
# split = join.split('_ ', 3)
# letter_3 = '_ '.join(split)
# print(letter_3)


# print(split)

def str_challenge(lst: list) -> str:
    string = lst[0]
    dictionary = lst[1]
    dictionary_list = dictionary.split(",")

    found_words = []
    for word in dictionary_list:
        if ~string.find(word):
            found_words.append(word)

    return string

# ["baseball", "a,ball,cat,rake,base,se,duro"] => [a, ball, cat..]
