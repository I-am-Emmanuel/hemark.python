print('Enter a sentence and I tell you the words that ends with letter ed')
words = 'ed'
sentence = input('Enter your sentence:: ')
for word in sentence.split():
    if word.endswith(words):
        print(word, end=' ')

