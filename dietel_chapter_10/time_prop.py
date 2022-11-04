from timewithproperties import Time
import doctest

wake_up = Time(hour=6, minute=30)


if __name__ == '__main__':
    doctest.testmod(verbose=True)