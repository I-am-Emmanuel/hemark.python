import decimal

print('Compound interest calculator2')

principal = decimal.Decimal(1000)
percentage = 100
rate = decimal.Decimal(7 / percentage)
print("Years", ""*3, "Interest Amount")
for years in range(1, 31):
    amount = principal * (1 + rate) ** years

    print(f'{years:>3}{amount:>14.2f}')

print('Compound interest calculator2')

principal = decimal.Decimal(input("Enter your principal: "))
percentage = 100
rate = decimal.Decimal(input("Enter your rate: "))
print("Years", ""*3, "Interest Amount")
for years in range(1, 4):
    amount = principal * (1 + rate/100) ** years
    final_amount = amount - principal

    print(f'{years:>3}{final_amount:>14.2f} {amount:>10}')

