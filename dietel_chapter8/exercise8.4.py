# text = 'hungry lion is coming'
# for letter in text.split():
#     rev = ' '.join(reversed(letter))
#     print(rev, end=' ')

text = 'the jungle is not enough for the lion king to rule'
rev = []

for word in text.split():
    rev.append(word)
# print(sorted(rev))

for i in sorted(rev):
    print(i, end=' ')
# print(rev)
# lowest = rev[0]
# final = []
# temp = []
# for i in rev:
#     for j in rev[1:]:
#         if i < j:
#
#             j = i
#         temp.append(j)
# print(temp)