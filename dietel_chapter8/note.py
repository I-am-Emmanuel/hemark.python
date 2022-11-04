# print(f'{58:c}{45:c}{41:c}')
#
# print(f'[{"Amanda":>10}]\n[{"Amanda":^10}]\n[{"Amanda":<10}]')
#
# print(f'[{27:+10d}]')
#
# print(f'[{-27:10d}]')
#
# print(f'{12345678:,d}')
#
# print(f'{123456.78:,.2f}')
#
# first_e = '{:.2f}'.format(17.489)
# print(first_e)
#
# jola = '{0} {0} {1}'.format('Happy', 'Birthday')
# print(jola)
#
# her_name = '{last} {first}'.format(first='Amanda', last='Gray')
# print(her_name)
#
# print('[{0:>10}]\n[{1:^10}]\n[{0:<10}]'.format('Amanda', 'Randy'))
#
# print('{:>10,.2f}\n{:+10,.2f}'.format(10240.473, -3210.9521))
#
# a = 'Happy'
# b = 'birthday'
# a += ' ' + b
# print(a)
#
# name = 'Emmanuel'
# name1 = 'Olaifa'
#
# name += ' ' + name1
#
# symbol = '='
# symbol *= len(name)
# print(f'{symbol}\n{name}\n{symbol}')
#
# jab = "        I'm waiting for the day I will leave my country to another Nation in this world     "
# print(jab)
# print(jab.lstrip())
# print(jab.strip())

# my_book = 'new general maths'
#
# print(my_book.capitalize())
# print(my_book.title())
#
sentence = 'to be or not to be that is the question'
#
# letters = sentence.split(', ')
# print(letters)
#
# for word in sentence.split():
    # if word.startswith('t'):
        # print(word, end='  ')
# print()
#
# val = '1\t2\t3\t4\t5'
# print(val)
# val_1 = val.replace('\t', ',')
# print(val_1)
# val_2 = val_1.replace(',', ' --> ')
# print(val_2)
#
# # SPLITING STRINGS
#
letter = 'A, B, C, D, E'
letters = letter.split(', ')
# print(letters)
# letters_2 = letter.split(', ', 3)
# print(letters_2)
letter_3 = ','.join(letters),
print(letter_3)

new_list = ','.join([str(index) for index in range(10)])
print(new_list)
#
# 'Amanda: 89, 97, 92'
# grades = 'Amanda: 89, 97 ,: , 92'.partition(': ')
# print(grades)
#
# 'Amanda: 89, 97, 92'
# grades = 'Amanda: 89, 97,: , 92'.rpartition(': ')
# print(grades)
#
# lines = "This is line 1\nThis is line 2\nThis is line 3"
# # print(lines)
# lines = lines.splitlines()
# print(lines)
#
# word = 'Pamela White'
# word = ', '.join(reversed(word.split()))
# print(word)
#
# # RAW STRING
#
# sst = r'//Holla//'
# print(sst)
#
# words = 'Pamela White Jungle mela'
# word = words.split()
# word.reverse()
# word.sort()
# print(word)
#
# # MATCHING LITERAL CHARACTERS
#
import re
#
# pattern = '02383'
#
# correct = 'Match' if re.fullmatch(pattern, '02383') else 'No Match'
# print(correct)
#
# correct = 'Match' if re.fullmatch(pattern, '00193') else 'No Match'
# print(correct)
#
# # Meta characters
#
# Zip = 'Valid' if re.fullmatch(r'\d{5}', '88231') else 'No Valid'
# print(Zip)
#
# zips = 'Valid' if re.fullmatch(r'\d{5}', '9876') else 'Invalid'
# print(zips)
#
# # Custom Characters
# name = 'Valid' if re.fullmatch('[A-Z][a-z]*', 'Bong') else 'Invalid'
# print(name)
#
# name_2 = 'Valid' if re.fullmatch('[A-Z][a-z]*', 'olaoye') else 'Invalid'
# print(name_2)
#
# name_ca = 'Valid' if re.fullmatch('[^A-Z]', 'd') else 'Invalid'
#
# print(name_ca)
#
# name_ca2 = 'Valid' if re.fullmatch('[^a-z]', 'D') else 'Invalid'
#
# print(name_ca2)
#
# name_char = 'Match' if re.fullmatch('[*+$]', '!') else 'No Match'
#
# print(name_char)
#
# add_char = 'Valid' if re.fullmatch('[A-Z][a-z]+', 'Wally') else 'Invalid'
# print(add_char)
#
# # The ? quantifier matches zero or one occurrence of a subexpression:
# tag = 'Valid' if re.fullmatch('Lab?elled', 'Laelled') else 'Invalid'
# print(tag)
#
# tage = 'Valid' if re.fullmatch('Labelled?', 'Labelle') else 'Invalid'
# print(tage)
#
# # Matching with (n, ) quantifier
#
# my_numb = 'Match' if re.fullmatch(r'\d{3,}', '94020') else 'No Match'
# print(my_numb)
#
# my_numbs = 'Match' if re.fullmatch(r'\d{4,6}', '2893') else 'No Match'
# print(my_numbs)
#
# my_other_numbs = 'Match' if re.fullmatch(r'\d{3,7}', '7723') else 'No Match'
# print(my_other_numbs)
#
# street = r'\d+ [A-Z][a-z]* [A-Z][a-z]*'
# streeta = 'Match' if re.fullmatch(street, '123 Kalomo Hollimat') else 'No Match'
# print(streeta)
# streetz = 'Match' if re.fullmatch(street, '991Kalomo Hollimat') else 'No Match'
# print(streetz)
#
# let = re.sub(r'\t', ', ', '1\t2\t3\t4\t5')
# print(let)
#
# hole = re.sub(r'\t', ', ', '1\t2\t3\t4\t5', count=3)
# print(hole)
#
spli = re.split(r',\s*', '1, 2, 3,4, 5,6,7,8')
print(spli)
#
# drill = re.split(r',\s*', '1, 2, 3,4, 5,6,7,8', maxsplit=2)
# print(drill)
#
# replace = re.sub(r'\t+', ', ', 'A\tB\t\tC\t\t\tD')
# print(replace)
#
# street = re.split(r'\$+', '123$Main$$Street')
# print(street)
#
# result = re.search('IS', 'Fun is Coin')
# new_result = result.group() if result else 'Not found'
# print(new_result)
#
# result_2 = re.search('fun@!', 'Playing is fun@!g')
# new_result_2 = result_2.group() if result_2 else 'Not found'
# print(new_result_2)
#
# result_3 = re.search('alawadare', 'Alawadare alawadare ani oni kerikeri ni', re.IGNORECASE)
# new_result_3 = result_3.group() if result_3 else 'Not found'
# print(new_result_3)
#
# result_4 = re.search('^lovers', 'LOVERS will never forgive', re.IGNORECASE)
# new_result_4 = result_4.group() if result_4 else 'Not found'
# print(new_result_4)
#
# result_5 = re.search("^Ajanaku", "bAba r'erin ka sope a r'erin, Ajanaku koja mo ri nkan firi")
# new_result_5 = result_5.group() if result_5 else 'Not found'
# print(new_result_5)
#
# result_6 = re.search('sing$', 'Come over and sing')
# new_result_6 = result_6.group() if result_6 else 'Not Found'
# print(new_result_6)
#
# contact = 'Wally White, Home: 555-555-1234, Work: 555-555-4321'
# contact_number = re.findall(r'\d{3}-\d{3}-\d{4}', contact)
# print(contact_number)
#
# for numbers in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
#     print(numbers.group())
#
# text = 'Hopeson John, e-mail: hope12@gmail.com'
# pattern = r'([A-z][a-z]+ [A-z][a-z]+), e-mail: (\w+@\w+\.\w{3})'
# result_yes = re.search(pattern, text)
# result_8 = result_yes.groups()
# best_way = result_yes.group()
# print(result_8)
# print(best_way)

# text = 'Charlie Cyan, e-mail: demo1@deitel.com'
# pattern = r'([A-Z][a-z]+ [A-Z][a-z]+), e-mail: (\w+@\w+\.\w{3})'
# result = re.search(pattern, text)
# rezult = result.groups()
# best = result.group(2)
# print(rezult)
# print(best)

# numberb = '5 + 10'
# patt = re.search(r'(\d+) ([-+*/]) (\d)', '5 + 10')
# result = patt.groups()
# res = patt.group(1)
# rex = patt.group(2)
# rey = patt.group(3)
# print(result)
# print(res)
# print(rex)
# print(rey)

