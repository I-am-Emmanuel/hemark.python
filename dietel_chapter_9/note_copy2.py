accounts = open('accounts.txt', 'r')
temp_file = open('temp_file.txt', 'w')

with accounts, temp_file:
    for record in accounts:
        accounts, name, balance = record.split()
        if name != 'Simon':
            temp_file.write(record)
        else:
            new_record = ' '.join([accounts, 'Walter', balance])
            temp_file.write(new_record + '\n')
import os
os.remove('accounts.txt')
os.rename('temp_file.txt', 'accounts.txt')