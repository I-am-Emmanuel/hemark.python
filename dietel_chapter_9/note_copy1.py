accounts = open('accounts.txt', 'r')
temp_file = open('temp_fie.txt', 'w')

with accounts, temp_file:
    for records in accounts:
        accounts, name, balance = records.split()
        if accounts != '300':
            temp_file.write(records)
        else:
            new_record = ' '.join([accounts, 'Williams', balance])
            temp_file.write(new_record + '\n')
import os

os.remove('accounts.txt')
os.rename('temp_fie.txt', 'accounts.txt')