

print(2)


# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 _ C _ D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:

# 100,150,180
# The output of the program should be:

# 18,22,24


# c, h = 50, 30

# comma_separated = input('Enter your numbers:: ')
# for item in comma_separated.split(','):
#         Q = (2*c*int(item)/h)**0.5
#         print(round(Q), end=' ')


# # comma_separated = input('Enter your numbers:: ')
# Q = [round((2*c*int(item)/h)**0.5) for item in comma_separated.split(',')]
# #    
# print(Q)


# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# class String:
        

#         def getString(self):
#                 try:
#                     self.word = input('Enter anything like a word: ')
#                 except ValueError as e:
#                         print(e)

#         def printString(self):
#                 print(self.word.upper())


# object1 = String()
# object1.getString()
# object1.printString()
                

                
        




# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which
# contains every number.Suppose the following input is supplied to the program:

# 34,67,55,33,12,98
# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


# lst = []
# sequence = str(input('Enter your number: '))
# for index in sequence.split(','):
#         lst.append(str(index))
        

# print(tuple(lst))
# print(lst)



# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# while True:
#         try:
#                 integral = int(input('Enter a number: '))
#                 break
#         except ValueError as e:
#                 print(e)
    
# result = {item: item * item for item in range(1, integral + 1)}
# print(result)






# Write a program which can compute the factorial of a given numbers.The results should be printed in a 
# comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

# def factorial() -> int:
#         start = 1
                        
#         while True:

                        
#                 try:
#                         numb = int(input('Enter a number:: '))
                
#                 except ValueError:
#                         raise ValueError('This must be a number!')
                
                        
#                 for each_number in range(start, numb+1):
#                         start *= each_number

                 
#                 return start
        
# print(factorial())

# while True:
#         try:
#                 num = int(input("Enter a number: "))
#                 break
#         except ValueError as err:
#                 print(err)

# org = num
# fact = 1
# while num:
#     fact *= num
#     num = num - 1
# print(f'the factorial of {org} is {fact}')

# def generator_number(number):
#         current = 1
#         for i in range(current, number+1):
#                 current *= i
#                 yield current

# for item in generator_number(8):
#         print(item)
                

# def new(obj):
#         for item in obj:
#                 print(item)
# result = new(generator_number(8))

# result = lambda gen: g for g in gen, gengenerator_number(8)
# print(result)





# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence
# on a single line.

# for number in range(2000, 3201):
#     if number % 7 == 0 and number % 5 != 0:
#         print(number, end=', ')

# print(*(number for number in range(2000, 3201) if number % 7 == 0 and number % 5 != 0), sep=', ')





# def fibonacci_number(num):
#         first = 0
#         second = 1
#         for i in range(num):
#                 yield first
#                 temp = first
#                 first = second
#                 second = first + second
                 
# for x in fibonacci_number(21):
#         print(x)


# def fibonacci_number(number: int):
#         current = 0
#         for item in number:
#                 current += item
#         return current

# print(fibonacci_number(generator_number(5)))


        
# def print_all(param):
#         for item in param:
#                 if item % 3 == 0:
#                         print('goat')
#                 elif item % 2 == 0:
#                         print('bird')
#                 else:
#                         print(item)

# new = print_all(generator_number(1000))

# new

# for item in generator_number(10):
#         print(item)


# new_item = generator_number(10)
# print(new_item)

# from time import time
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# def performanceDecorator(function):
#     def funtionWrapper(*args, **kwargs):
#         time_1 = time()
#         result = function(*args, **kwargs)
#         time2 = time()
#         print(time2 - time_1)
#         return result
#     return funtionWrapper

# @performanceDecorator
# def duplicate_function1(lst:list):
#     duplicate = []
#     for eachItem in lst:
#         if lst.count(eachItem) > 1:
#             if eachItem not in duplicate:
#                 duplicate.append(eachItem)
#     # print(duplicate)

# duplicate_function1(some_list)

# @performanceDecorator
# def duplicate2(lst:list):
#     item = []
#     duplicate = []
#     for index in lst:
#         item.append(index) if index not in item else duplicate.append(index)
#     del item

# duplicate2(some_list)





# list_of_list = [[2,8, 9,2, 1], [8,2,8,9, 2, 0], [0, 2,9,2, 9]]
# ind = [index for index in range(0, len(list_of_list))]
# result = lambda param: [set(param[0]) & set(item) for item in param[1:]]
# print(result(param=list_of_list))
# lst = [5,4,3]
# print(list(map(lambda param: param**2, lst)))
# print(lst)

# a = [(8,2), (4,1), (9,9), (10,-1)]

# my_dict = [{numb:numb**2} for numb in [1,2,3]]
# print(my_dict)

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# new_duplicate = list(set([item for item in some_list if some_list.count(item) > 1]))
# print(new_duplicate) 

# new_duplicate = lambda items: list(set([item for item in items if items.count(item) > 1]))

# print(new_duplicate(items=some_list))

# print(index2(param=a))

# a.sort(key=lambda param: param[1])
# print(a)

# def sort_list(param:list) -> list:
#     tempList = []
#     # for item in param:
#     #     for index in item:
#     #         index
#     # for index in param:
#     #     pass

    
#     # for index in range(len(param)):
#     for item in param:
#         for nextItem in param[1:]:
#             # print(nextItem)
#             if nextItem[1] < item[1]:
#                 nextItem = item

    # tempList.append(nextItem)
        
            

    # return(tempList)
        # for index in 
        #     print(index)

# print(sort_list(param=a))


# import math
# numbers = [i for i in range(200112201)]

# @performanceDecorator
# def middle_number(items) :
#     length = len(items)
#     if length % 2 != 0:
#         mid_point = length / 2
#         return f'The middle number is {items[math.trunc(mid_point)]}'
    
#     else:
#         length = len(items) / 2
#         first_half = items[:int(length)]
#         second_half = items[int(length):]
        # return f'The middle numbers are {first_half[-1]} and {second_half[0]}'

# print(middle_number(items=numbers))

# middle_number(numbers)


# import pandas as pd
# def student_table():
#     "Welcome to Wesley Girl's School"
    
#     question = int(input("How many student's data did you want to input?: "))
#     count = 0
    
#     school_file = []
#     while count != question:
#         student_file = {}
#         first_name = input('Enter your first name: ')
#         last_name = input('Enter your last name: ')
#         age = int(input('Enter your age: '))
#         student_class = input('Enter your class: ')
#         student_file['first_name'] = first_name.capitalize()
#         student_file['last_name'] = last_name.capitalize()
#         student_file['age'] = age
#         student_file['class'] = student_class
#         count += 1

        
#         school_file.append(student_file)

#         question2 = input('Did you want to continue entering another student data?\nIf yes enter Y else enter N: ').capitalize()
#         if question2 != 'y'.capitalize() and count != question:
#             print('')
#             print('Okay, thanks for your input!. Since you wish to quit before the number of the data you \nsupplied exhausted, I wish you best of luck. Here is the current table below.')
#             print(" ")
#             break
            

#         elif question2 == 'y'.capitalize and count == question:
#             print('')
#             print('Your session is completed, you can input details more than the {question} number of student you gave, I wish you best of luck. Here is the current table below.')
#             print('')
#             break
        
    

#     return pd.DataFrame(school_file)

    

# print(student_table())










# import random
# for index in range(1, 101):
# hundred = range(100)
#     print(index)
# print()

# class SuperList(list):
#     def __len__(self):
#         return 45

#     # def __append__(self, )

# super_list1 = SuperList()
# # print(len(super_list1))
# super_list1.append(5)
# print(super_list1[0])

# print(len(super_list1))


# def removeDuplicates(nums):
#     if not nums:
#         return 0

#     k = 1  # Number of unique elements
#     n = len(nums)

#     for i in range(1, n):
#         print(i)
#         if nums[i] != nums[i - 1]:
#             nums[k] = nums[i]
#             k += 1

#     return k

# print(removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))

# def duplicate(k:list):
#     new_item = []
#     space_item = []
#     for i in range(len(k)):
#         item = k.pop()
#         if item not in new_item:
#             new_item.append(item)
#             new_item.sort()
#         space_item.append('_')
#     new_item += space_item

#     return(f'{len(new_item)}, nums = {(new_item)}')

# def duplicated_int(nums:list):
#     dup_numb = []
#     for item in nums:
#         if item not in dup_numb:
#             dup_numb.append(item)

#     return(f'{len(dup_numb)}, nums={dup_numb}')


# print(duplicated_int(nums=[0,0,1,1,1,2,2,3,3,4]))

# k = reversed([0,0,1,1,1,2,2,3,3,4])

# print(k)





# number1 = 23, 10
# number2 = 21

# total = number1 + number1
# sumup = 0
# for number in total:
#     sumup += number
# print(sumup + number2)
    
# print(total)



# fruit = ['orange juice', 'banana', 'apple']
# for item in fruit:
#     print(len(item), end=' ')

# def highest_even(lst:list):
#     evens = []+++
#     for number in lst:
#         if number % 2 == False:
#             evens.append(number)
#     return max(evens)

# print(highest_even([2, 4, 8, 10, 11, 3]))



# def reverse_func(lst):
#     numb = lst
#     index = -1
#     arrange = [None] * len(numb)

#     for item in numb:
#         arrange[index] = item
#         index -= 1
#     numb = arrange
#     return numb
# #

# print(reverse_func(lst=[-1, 2, -5, 100, -9, 20]))


# def sort_func(lst):
#
#     nas = lst
#     arrange = sorted(nas)
#     return arrange


# print(sort_func(list=[8, 92, 10,74, 32]))
# print(sort_func([8, 29, 100, 32, 83]))
# print(reverse_func([83, 'gas', 89, {'key': [82]}]))

# def reverse_list(file: list) -> list:
#     ind = -1
#     first_file = [None] * len(file)
#     for index in file:
#         first_file[ind] = index
#
#         ind -= 1
#     return first_file
#
#
# print(reverse_list([72, 10, 'jola']))


# def encryption(number:int) -> str:
#     constant = 7
#     divisor = 10
#     new_list = []
#     return_lst = []
#     # num =
#     if 4 < len(str(number)) > 4:
#         raise ValueError('Your input should not be greater or lesser than 4')
#     for index in str(number):++
#         new_list.append((constant + int(index)) % divisor)

#     point1 = -2
#     point2 = -1
#     count = 0

#     while count != len(new_list) / 2:
#         return_lst.append(new_list[point1])
#         return_lst.append(new_list[point2])

#         count += 1
#         point1 -= 2
#         point2 -= 2
#     # print(return_lst)
#     result = str(return_lst[0])
#     for i in (return_lst[1:]):
#         result = result + str(i)

#     return result


# print(encryption(number=9128))

# def decrypt_code():
#     point1 = -2
#     point2 = -1
#
#     while
#     num = for i in

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.isLast = False
#
#     def insert(self, word):
#         node = self.root
#         for letter in word:
#             if letter not in node.children:
#                 node.children[letter] = TrieNode()
#
#         node = node.children[letter]
#
#         node.isLast = True

# def meetingRooms(start, ends):
#     rearrange_rooms = [(s, 1) for s in start] + [(s, -1) for s in ends]
#     print(rearrange_rooms)
#
#     rearrange_rooms.sort()
#     print(rearrange_rooms)
#
#     rooms = 0
#     max_rooms = 0
#     # iterate and add value to room
#     for pos, value in rearrange_rooms:
#         rooms += value
#     print(rooms)
#     # store the max rooms
#     max_rooms = max(rooms, max_rooms)
#     return max_rooms
#
#
# print(meetingRooms([9, 5, 7, 3, 4, 9], [7, 2, 7, 5, 7]))


# document = (9, (19, 20), 'going', ['apple', 'you'])
# document[-1].append('gun')
#
# print(document)

# def two_dimensional(lst1: list) -> list:
#     # result = []
#     file = set(lst1[0])
#     for index in lst1[1:]:
#         result = file & set(index)
#         file = result
#     # result.append(result)
#     return list(file)


# print(two_dimensional([[2,8, 9,2, 1], [8,2,8,9, 2, 0], [0, 2,9,2, 9]]))

# from datetime import datetime
# birth_year = input('What year were you born?')

# age = 2021 - int(birth_year)
# print(f'Your age is {age}')

# user_name = input('Enter your username: ')
# password = input('Enter your password: ')
# pass_key = '*' * len(password)
# password_length = len(password)

# print(f'{user_name},your password {password} is {len(password)} letters long')

# import random
# count = 0
# try:
#     question1 = input(str('(1). What is 54 + 19?\n(a) 56.\n(b) 73.\n(c) No answer.\n'))

#     if question1 == 'b'.lower() or question1 == 'b'.upper():
#         count += 1
#     else:
#         count == 0
# except TypeError:
#     print('Your input cannot be a number!')

#     question2 = input(str('(2). What is 5 x 9?\n(a) 46.\n(b) 45.\n(c) No answer.\n'))
#     if question2 == 'b'.lower() or question1 == 'b'.upper():
#         count += 1
#     else:
#         count == 0
# except Exception as errormessage:
#     print(str(errormessage))

#     # print(count)
# new = random.randint(1, 7)
# print(count)
# # print()

# even = [1,2,3,4,5,5]
# odd = set(even)
# print(odd)
# print(even)
# print(tuple((even)))

# is_magician = False
# is_expert = True

# # check = "You're a master magician" if is_magician and is_expert else "You're not a magician and master"
# # print(check)

# if is_magician and is_expert:
#     print("You're a master magician")

# elif is_magician and not is_expert:
#     print("You're getting there!")

# elif not is_magician:
#     print("You need magic powers")

# my_list = [1,2,3,4,5,6,7,8,9,10]
# count = 0
# for item in my_list:
#     count += item

# print(count)

# for index, number in enumerate(list(range(100))):
#     if number == 50:
#         print(f'The index of 50 is {index}')

# picture = [
# [0,0,0,1,0,0,0],
# [0,0,1,1,1,0,0],
# [0,1,1,1,1,1,0],
# [1,1,1,1,1,1,1],
# [0,0,0,1,0,0,0],
# [0,0,0,1,0,0,0]
# ]

# def show_tree():
#     for index in picture:
#         for item in index:
#             print(' ' if item == 0 else '*', end='')
#         print('')

# show_tree()
# show_tree()
# show_tree()

# duplicated = []
# item = []
# my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


# for index in range(len(my_list)):
#     checker = my_list.pop()
#     if checker in my_list:
#         duplicated.append(checker)
# print(duplicated)
# item = []
# duplicate = []
# for index in my_list:
#     item.append(index) if index not in item else duplicate.append(index)
# del item
# # print(item)
# print(duplicate)

# for letter in my_list:
#     if my_list.count(letter) > 1:
#         if letter not in duplicated:
#             duplicated.append(letter)
# print(duplicated)





        
        
            