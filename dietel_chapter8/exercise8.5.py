print('Enter a sentence and I tell you the words that begins with letter b')
words = 'b', 'B'
sentence = input('Enter your sentence:: ')
for word in sentence.split():
    if word.startswith(words):
        print(word, end=' ')

