from .account import Account
from decimal import Decimal
# import doctest

account_1 = Account('Joe Dan', Decimal('923.02'))
print(account_1.name)


Decimal('923.02')




if __name__ == '__main__':
    doctest.testmod(verbose=True)
