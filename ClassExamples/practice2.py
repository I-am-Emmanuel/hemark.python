# # a: list = [6, 72, 18, 2, 9]    #  , "Love"]
# # list_of_list = [[1, 2, 3], ["a", "b", "c"]]
# # list = (("Hello"))
# # print(a[:])
# # print(list_of_list)
# # print(list)
# # List = "hello".rjust(10) * 3
# # print(List)
# # print(a + list_of_list)
# """
# p = ("forge", "bell", "rat", 8, 2, 9, 1, 19, 12, 10)
# print(p[3])
# print(p[-3])
# print(p[3:])
# print(p[1::2])
# print(p[::-2])
#
# hobby = ["NoiseMaking", "Mark", "Simon", "Tobias", "Mike", "Ander", 2, 9, 0, 19]
# print(hobby[3::2])
#
# hobby = "Noise Making"
# print(hobby[3::2])"""
#
# """friend = ["a", [1, 2, 3], "z"]
# print(friend[1][2])
# # print(friend[0], [1, 1], [2])
# print(friend[1][2], friend[0], friend[2])
# print(friend[0] or [1, 2] or [2])
#
# mutable List
# Love = [0, 90, 27]
# Love[0] = "Banke"
# print(Love)
#
# Animal = ["Hen", "Ram", "Goat", "Tiger"]
# print(Animal)
#
# import random
#
# number = list(range(1, 17))
# print(number)
# random.shuffle(number)
# print(number)
# print(random.choice(number))
#
# number.append([72, 73, 88])
# print(number)
# number.extend([99, "Olamide", "Adebayo"])
# print(number)
# number += ["Joy", "Love", "Wisdom"]
# print(number)
# number.insert(2, 0.0)
# print(number)
# number.insert(-3, "Happiness")
# print(number)
# number.pop()  # Remove the last number
# print(number)
# last_number = number.pop()
# print(number)
# number.pop(8)
# print(number)
# # number.remove(11)
# # print(number)
# print("Count", number.count("Olamide"))
# print(number)
# number.extend(["Olashiregun", "Olamide", "Olarinde", "Olamide", "Olashiregun", 72, 16, 6, 14])
# print(number)
# print("Count", number.count("Olashiregun"))
# print("    ")
# # number.remove("Olashiregun")
# # print(number)
# # del number
# # print(number)
# # number.clear()
# # print(number)
#
# digit = number
# print("Digit", digit)
# print("number", number)"""
#
#
# #
# # jug = [6, 2, 3, [0, 2], 9]
# # mat = jug[:]
# # print(mat)
# # print(jug)
# # mat[3][1] = 3
# # print(mat)
# # print(jug)
# # mat[3].append(8)
# # print(mat)
# # print(jug)
# #
# # jug.reverse()
# # print(jug)
# #
# lam = "Let's go play the match"
# lam_list = lam.split()
# print(lam)
# lam_list.reverse()
# print(lam_list)
# print(lam[::-1])
#
# # def fun(lst=[]):
# #     lst.append(2)
# #     return lst
# #
# #
# # print(fun())
# # print(fun())
# # print(fun([7, 8, 9]))
#
#
# # def func(lst=None):
# #     if lst is None:
# #         lst = []
# #     lst.append(98)
# #     return lst
# #
# #
# # print(func())
#
# def numb(*args):
#     total = 0
#     for number in args:
#         total += number
#     print(total)
#
#
# numb(9, 82, 100)
#
# def func(**hall):
#     print(hall)
#
#
# func(a = 12, b = 14, c = 16)


# def add(a: float, b: float):
#     try:
#         return a / b
#     except:
#         print("Can't divide with zero")
#         return None
#
#
# print(add(1, 0))

# def add(a: float, b: float):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Can't divide with zero")
#         return None
#
#
# print(add(1, 0))


# def add(a: float, b: float):
#     try:
#         c = a + 'b'
#         return a / b
#     except ZeroDivisionError:
#         print("Can't divide with zero")
#         return None
#     except TypeError:
#         print('Type error')
#
#
# print(add(1, 0))

# def add(a: float, b: float):
#     try:
#         # c = a + 'b'
#         print(name)
#         return a / b
#     except ZeroDivisionError:
#         print("Can't divide with zero")
#         return None
#     except (TypeError, NameError):
#         print('Type error')
#
#
# print(add(1, 0))

# def add(a: float, b: float):
#     try:
#         # c = a + 'b'
#         name = int('great')
#         return a / b
#     except ZeroDivisionError:
#         print("Can't divide with zero")
#         return None
#     except (TypeError, NameError):
#         print('Type error')
#     except ValueError:
#         print('Value Error')
#
#
# print(add(1, 0))

# def add(a: float, b: float):
#     try:
#
#         file = open('file.txt', mode='r', encoding='utf-8')
#         print(file.read())
#         print('About to close')
#         file.close()
#         return a / b
#     except ZeroDivisionError:
#         print("Can't divide with zero")
#         return None
#     except (TypeError, NameError):
#         print('Type error')
#     except ValueError:
#         print('Value Error')
#     except IndexError:
#         print('Index Error')
#     finally:
#         print('About to close')
#         file.close()
#
#
# print(add(1, 0))


# with open('temp_file.txt', mode='w', encoding='utf-8') as file_object:
#     print(file_object.tell())
#     file_object.write('Life is good with Anu')
#     print(file_object.tell())
#     file_object.write('Life is good with Anu')
#

#
# with open('temp_file.txt', mode='w', encoding='utf-8') as file_object:
#     print(file_object.tell())
#     file_object.write('Life is good with Anu\n')
#     # file_object.seek(10)
#     print(file_object.tell())
#     file_object.write('Life is good with Anu\n')
#     file_object.writelines(['Life\n', 'is\n', 'good\n'])
#
# with open('temp_file.txt', 'r', encoding='utf-8') as file:
#     # print(file.read())
#     # print(file.readline())
#     # print(file.readlines())
#     for idx, line in enumerate(file.readlines(), start=1):
#         print(f'{idx}. {line.upper()}')
#
# from pathlib import Path
# # #
# path = Path('folder/sub-folder/text.txt')
#
#
# path.parent.mkdir(parents=True, exist_ok=True)
#
# path.touch(exist_ok=True)
#
#
# print(path.resolve())
#
# with path.open(mode='a') as files:
#     files.write('Hello')
#
# class Human:
#     pass
#
#
# ada = Human()
#
# ada.age = 14
# print(f"Ada's age is {ada.age}")

# class Human:
#     name = 'Modupe'
#
#     def get_name(self):
#         return self.name
#
#
# hi = Human
# print(hi.name)
#
# class Human:
#     name = 'Basiru'
#
#     def set_name(self, name):
#         self.name = name
#
#
# hi = Human
# hi.set_name = 'Shola'
# print(f'{hi.set_name}\n{hi.name}')

# class Human:
#     def __init__(self, name='', age=0):
#         self.name = name
#         self.age = age
#
#         # def get_name(self):
#         #     return self.name, self.age
#
#
# oruko = Human('Jolaoye', 12)
# print(oruko.name, oruko.age)

# numbers = 8372093
# print(f'{numbers:,d}')
