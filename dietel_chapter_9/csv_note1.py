import csv
#
# with open('accounts.csv', mode='w', newline='') as accounts:
#     writer = csv.writer(accounts)
#     writer.writerow([100, 'Jones', 24.98])
#     writer.writerow([200, 'Doe', 345.67])
#     writer.writerow([300, 'White', 0.00])
#     writer.writerow([400, 'Stone', -42.16])
#     writer.writerow([500, 'Rich', 224.62])


# with open('accounts.csv', mode='r', newline='') as accounts:
#     print(f'{"Account":<10} {"Name":<10} {"Balance":>10}')
#     reader = csv.reader(accounts)
#     for record in reader:
#         accounts, name, balance = record
#         print(f'{accounts:<10}{name:<10}{balance:>10}')


# with open('grades.csv', mode='w', newline='') as grades:
#     writer = csv.writer(grades)
#     writer.writerow([1, 'Red', 'A'])
#     writer.writerow([2, "Green", 'B'])
#     writer.writerow([3, 'White', 'A'])

with open('grades.csv', mode='r', newline='') as grades:
    print(f'{"Number":<10}{"Name":<10}{"Grade":>10}')
    reader = csv.reader(grades)
    for results in reader:
        number, name, grade = results
        print(f'{number:<10}{name:<10}{grade:>10}')

