import string
print("The bruce force approach")

decode = input("What would you like to decode? ")

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase

for i in range(1, 27):
    lower_case_code = lower_letters[i:] + lower_letters[:i]
    upper_letters_code = upper_letters[i:] + upper_letters[:i]

    letters = lower_letters + upper_letters
    letters_code = upper_letters_code + lower_case_code

    bruce_force = decode.translate(str.maketrans(letters_code, letters))

    print(bruce_force)