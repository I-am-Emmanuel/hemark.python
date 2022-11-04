text = 'He who jump is she who swim he who swim is he who jump whether you jump or you run you ' \
       'are still going to swim cos that is the rule in navy training'

word_count = {}
counts = 0
for word in text.upper().split() and text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in sorted(word_count.items()):
    if count > 1:
        counts += 1
    print(f'{word:<8} {count}')
print(f'The number of duplicated words in this dictionary is {counts}')


