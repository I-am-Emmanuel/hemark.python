import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        # return (x, y)
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'{self.x}i + {self.y}j'

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __len__(self):
        return 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    # def __bool__(self):
    #     return True


v1 = Vector(2, 4)
v2 = Vector(3, 8)
v3 = (v1 + v2)

lstVector = [v1, v2, v3]
print(lstVector)
lstVector.sort()
print(lstVector)

print(v3)
