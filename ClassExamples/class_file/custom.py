class Customclass:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num

    def __lt__(self, other):
        return self.num < other.num


c1 = Customclass(7)
c2 = Customclass(8)

print(c1 + c2)
print(c1 * c2)
print(c1 < c2)
