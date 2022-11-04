from dataclasses import dataclass, field


@dataclass(order=True)
class Persons:
    __slots__ = ['name', 'age', 'height']
    sort_with: tuple = field(init=False, repr=False)
    name: str
    age: int
    height: int
    # height: int = field(default=0)
    # children: list = field(default_factory=lambda: [])

    def __post_init__(self):
        self.sort_with = (self.height, self.age)

    def get_age(self):
        return self.age


p1 = Persons(name='Hadiza', age=21, height=10)
p2 = Persons(name='Victor', age=20, height=15)

p1.name = 'Banke'
print(p1)
