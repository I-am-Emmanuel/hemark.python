import random

def guessing_game(question, answer):
    
    if 0 < question < 11:
        if question == answer:
            print('You are a genius')
            return True
    else:
        print('Bozzo, I said number between 1 and 10!')
        return False

if __name__ == '__main__':
                    
    answer = random.randint(1, 11)
    while True:
        try:
            question = int(input('Enter your guessed number between 1 - 10:: '))
            if guessing_game(question, answer):
                break    
        except ValueError as errormessage:
            print('I want a number, Silly!')
            continue
            
def simple_add(num=0):
    try:
        if num:
            return int(num) + 5
        elif num == 0:
            return int(num) + 5
        else:
            return 'Please enter a number'
    except ValueError as errormessage:
        return errormessage


# from translate import Translator

# trans = Translator(to_lang='ja')

# try:
#     # with open('./english.txt', 'w') as file1:
#     #     english = file1.write('I love you and won\'t jilt you!')
#     with open('./test.txt', 'r') as file2:
#         eng_text = file2.read()
#         japanese = trans.translate(eng_text)
#         with open('./translated.txt', 'a', encoding='utf-8') as file3:
#             file3.write(f'\n{japanese}')
#             print('Translation successful!')
# except FileNotFoundError as errormessage:
#     print('File not found')
# except IOError as errormessage:
#     print(str(errormessage))
# try:
#     with open('../poly/morph.txt', 'r') as object2:
#         w_file = object2.read()
#         print(w_file)
# except FileNotFoundError as errormessage:
#     print('File not found in this path!')
#     print(str(errormessage))
# except IOError as errormessage:
#     print(str(errormessage))

# with open('../poly/morph.txt', 'w') as object1:
#     print(object1.write('Let\'s show love to everyone!'))

# with open('new_file\sad.txt', 'w') as n_file:
#     text = n_file.write('I feel sad cos she broke my heart')
#     print(text)

# with open('test.txt', 'a') as my_file:
#     print(my_file.write('\nI will love you forever :)'))
    # print(text)

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
