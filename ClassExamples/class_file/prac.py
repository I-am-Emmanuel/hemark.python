# class Practice:
#     count = 0
#
#     def __init__(self, first):
#         self.first = first
#         Practice.count += 1
#
#     def play(self):
#         return f"Playing with{self.first}"
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#     @classmethod
#     def create(cls, name, modifier):
#         return cls(modifier + ' ' + name)
#
#     @staticmethod
#     def just_here():
#         return f"Just hanging out here!!!"
#
#
# p1 = Practice('Shola')
# p2 = Practice.create('Adigun', 'Mrs')
#
# print(p2.first)


# mro
#
# class A:
#     def do_this(self):
#         return 'From A'
#
#
# class B(A):
#     pass
#
#
# class C:
#     def do_this(self):
#         print('From C')
#
#
# class D(B, C):
#     pass
#
#
# print(D.mro())
# print(D.__mro__)
# help(D)


# ABSTRACT CLASS

import abc


# class Mammal(metaclass=abc.ABCMeta):
class Mammal(abc.ABC):
    @abc.abstractmethod
    def move(self):
        pass


class Person(Mammal):
    def move(self):
        pass


m1 = Person()
