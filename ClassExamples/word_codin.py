import string

#abc = string.ascii_lowercase

"""word = "love"
#k = 5

encoded = word.translate(str.maketrans(abc[:-5], abc[5:]))
print(encoded)"""


"""word = "qtvj"
k = 5
decode = word.translate(str.maketrans(abc[5:], abc[:-5]))
print(decode)"""
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
word = input("What would you like to encode?")
key = int(input("Your key?"))

lower_letters_code = lower_letters[key:] + lower_letters[:key]
upper_letters_code = upper_letters[key:] + upper_letters[:key]

letters = lower_letters + upper_letters
letters_code = lower_letters_code + upper_letters_code


encoded_word = word.translate(str.maketrans(letters, letters_code))
print(encoded_word)






