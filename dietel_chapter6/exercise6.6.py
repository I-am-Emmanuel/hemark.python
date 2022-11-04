def rem_duplicated_word(lst):
    word = sorted(lst.split())  # set(lst.lower().split())
    return f'{(set(word))}'


#

words = 'everybody love to go to paradise Even without knowing what is at stake to be there'
print(rem_duplicated_word(lst=words))
