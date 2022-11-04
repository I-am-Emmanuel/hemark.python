# with open('accounts.txt', mode='w') as accounts:
#     accounts.write('100 Jones 24.98\n')
#     accounts.write('200 Doe 345.67\n')
#     accounts.write('300 Alberto 721.70\n')
#     accounts.write('400 Simon 00.17\n')
#     accounts.write('500 Kate 1000.33\n')
#     accounts.write('600 Long-staff -340.39\n')

with open('accounts.txt', mode='r') as accounts:
    print(f'{"Accounts":10}{"Name":<10}{"Balance":>10}')
    for record in accounts:
        accounts, name, balance = record.split()
        print(f'{accounts:10} {name:<10}{balance:>10}')






