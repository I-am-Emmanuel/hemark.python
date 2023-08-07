def palindrome(word: str):
    newindex = [index for index in word.lower()[::-1] or word.upper()[::-1]]
    forward_index = [index for index in word[:].lower() or word[:].upper()]
    if newindex == forward_index:
        return True
    else:
        return False


print(palindrome(word='Mad'))

# file = ['rid', 'fish', 'doll', 89, 1000, 8201, [93, 78]]
# new_file = [None] * len(file)
# index = -1
#
# for item in file:
#     new_file[index] = item
#     index -= 1
#
# file = new_file
# print(file)

# word_1 = input('Enter your first word:: ')
# word_2 = input('Enter your second word:: ')
# haming = 0
#
# for index in word_1:
#     if word_1.count(index) != word_2.count(index):
#         print('They are not anagram!')
#         break
# else:
#     print('They are anagram!')
#     word2_index = 0
#     for index in word_1:
#         if index != word_2[word2_index]: haming += 1
#
#         word2_index += 1
#     print('The haming difference is', haming)
