from decimal import Decimal
import doctest


class Account:
    """Account class for maintaining a bank account balance."""

    def __init__(self, name, balance):
        """Initialize an account object

        >>> account_1 = Account('Joe Biden', Decimal('70.83'))
        >>> account_1.name
        'Joe Biden'
        >>> account_1.balance
        Decimal('70.83')

        'The balance argument must be greater than zero'
        >>> account_2 = Account('Sikiru Ayinde', Decimal('0.00'))
        >>> account_2.name
        'Sikiru Ayinde'
        >>> account_2.balance
        Decimal('0.00')
        """

        if balance < Decimal('0.00'):
            raise ValueError('Initial balance should be > 0.00')
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money to the account
        >>> account_2 = Account('Sikiru Ayinde', Decimal('0.00') )
        >>> account_2.deposit(Decimal('2000'))
        >>> account_2.balance
        Decimal('2000.00')

        >>> account_3 = Account('John Lobo', Decimal('0.29'))
        >>> account_3.deposit(Decimal('1.00'))
        >>> account_3.balance
        Decimal('1.29')

        """

        if amount <= Decimal('0.00'):
            raise ValueError('Amount should be > 0.00')
        self.balance += amount

    def withdrawal(self, amount):
        """Withdraw money from the account
        >>> account_2 = Account('Sikiru Ayinde', Decimal('0.00'))
        >>> account_2.deposit(Decimal('8500.00'))
        >>> account_2.withdrawal(Decimal('5000.00'))
        >>> account_2.balance
        Decimal('3500.00')
        """
        if self.balance < amount:
            raise ValueError('Your amount should not be > balance')
        elif amount < Decimal('0.00'):
            raise ValueError('Your amount must be a positive value')
        self.balance -= amount


if __name__ == '__main__':
    doctest.testmod(verbose=True)
