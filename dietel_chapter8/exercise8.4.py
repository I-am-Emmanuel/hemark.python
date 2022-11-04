text = 'hungry lion is coming'
for letter in text.split():
    rev = ' '.join(reversed(letter))
    print(rev, end=' ')



