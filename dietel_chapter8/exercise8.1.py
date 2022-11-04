import re
new_number = '{:10,.2f}'.format(29993.931)
number = re.sub(r'\s', '*', new_number)
print(number)


number = eval(input('Enter your the amount:: '))
result_1 = '{:>10,.2f}'.format(number)
result_1 = re.sub(r'\s', '*', result_1)
print(result_1)
