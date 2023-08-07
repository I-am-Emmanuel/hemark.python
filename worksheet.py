# def str_challenge(lst: list) -> str:
#     string = lst[0]
#     dictionary = lst[1]
#     dictionary_list = dictionary.split(",")
#
#     found_words = []
#     for word in dictionary_list:
#         if ~string.find(word):
#             found_words.append(word)
#
#     return found_words
# print(str_challenge(["baseball", "a,ball,cat,rake,base,se,duro"]))
# # => [a, ball, cat..]


# def numb_challenge(lst: list):
#     found_numb = []
#     moving1 = lst[0]
#     moving2 = lst
#     # lst = [[3, 1, 2, 4], [4, 2, 7, 0], [3, 2, 1, 4]]
#     while moving2 != len(lst):
#         for index in lst:
#             if index in moving2:
#                 found_numb.append(index)
#         moving1 += 1
#         moving2 += 1
#     return found_numb
#
#
# print(numb_challenge([[3, 1, 2, 4], [4, 2, 7, 0], [3, 2, 1, 4]]))


# file = [[3, 1, 2, 4], [4, 2, 7, 0], [3, 2, 1, 4]]
# result = []
# numb = set(file[0])
# for index in file[1:]:
#     result = numb & (set(index))
#     numb = result
#
# print(sorted(list(numb)))


# def intersection(self, nums: list) -> int:
# d = defaultdict(int)
# for nums_i in file:
#     for num in nums_i:
#         d[num] += 1
# print(d)

#
# char = "1231"
# dic = {}
# for index in char:
#     if index in dic:
#         dic[index] += 1
#     else:
#         dic[index] = 1
# for key, val in dic.items():
#     if val > 1:
#         digit = key
# print(digit)

number, digit = '123', '3'
#
# th, _, new = number.partition(digit)
# t, _, new2 = number.rpartition(digit)
#
#
# if int(new) > int(t):
#     print(str(new))
# elif int(new) == int(t):
#     print(str(new))
# else:
#     print(str(t))
#
# lst = []
# for index in number:
#     if index == digit:
#         del index
#     else:
#         res = index
# print(res)


# cap = []

# def difference_of_two_array(nums: list) -> list:
#     stor = []
#     index1 = set(nums[0])
#     for index in nums[1:]:
#         ind = index1.difference(set(index))
#         index2 = set(index).difference(index1)
#         stor.append(list(ind))
#         stor.append(list(index2))
#     return stor


# print(difference_of_two_array([[1, 2, 3, 4], [8, 4, 1, 3]]))

# def difference_of_two_array(numb1: list, numb2: list) -> list:
#     caps = []
#     numb = set(numb1).difference(set(numb2))
#     numbs = set(numb2).difference(set(numb1))
#     caps.append(list(numb))
#     caps.append(list(numbs))
#     return caps
#
#
# print(difference_of_two_array([1, 2, 3, 4], [8, 4, 1, 3]))

# hashing = ['a', 'a', 'a', 'h', 'h', 'i', 'b', 'a', 'c']
# count = 1
# hole = 0
# hole2 = 1
# maxim = 0
# while hole2 < len(hashing):
#     if hashing[hole] is hashing[hole2]:
#         count += 1
#         hole += 1
#         hole2 += 1
#         if hashing[hole] is not hashing[hole2]:
#             maxim = count
#             continue
#         count = 0
#     elif hashing[hole] != hashing[hole2]:
#         maxim = count
#
#
# print(maxim)

names = ['Sade', 'Tola', 'Jide', 'Sunkanmi']


# count = 0
# new_array = []
# for index, name in enumerate(names):
#     new_array.append(name)
#     count += 1
#     if count == 0:
#         print(name)
#     print("No name to show")
#     if index == 2:
#         print(name)

# index = 0
# pointer = names[index]
# new_lst = []
# while pointer != len(names):
#     new_lst.append(pointer)
#     pointer += 1
# print(new_lst)
# lst = []
# dict = {1: 'monday', 2: 'tuesday', 3: 'wednesday'}
# for key, value in dict.items():
#     lst.append(value)
# print(lst)


# class Solution:
# def two_sum(nums: list, target: int) -> list:
#     store = []
#     number = nums[0]
#     numbers = len(nums) - 1
#     new = nums[numbers]
#     while number != new:
#         for i, j in enumerate(nums):
#             result = number + j
#             if result == target:
#                 store.extend([number, i])
#                 nums[0] += 1



    # for ind, index in enumerate(nums):
    #     for i, j in enumerate(nums):
    #         if index + j == target and (index != j) and (ind and i) not in result:
    #             result.extend([ind, i])

    # return store


# print(two_sum(nums=[2, 11, 15, 7, 15, 8, 7], target=22))

# def permutation_all_types(words) -> str:
#     for i in range(0, len(words)):
#         for j in range(1, len(words)):
#             return f'{words[i]} {words[j]}'
#
#
# word = input('Enter any sentence: ')
#
# print(permutation_all_types(words=word))

# return result


# result = []
# nums = [2, 11, 15, 7]
# for ind in range(0, len(nums)):
#     for i in range(1, len(nums)):
#
#         if nums[ind] + nums[i] == 18 and (ind and i) not in result:
#             result.extend([ind, i])
# result.append(i)
# continue
# if [ind, i] or [i, ind] in result:
#     continue
# else:
#     result.extend([ind, i])

# i += 1
# j += 1
# print(result)

# print()

# fig = [5, 3, 8, 1]

# def filterArray(lst: list, a: int, b: int) -> list:
#     result = []
#     for i in sorted(lst):
#         result.append(i)
#
#
#
# print(filterArray(lst=fig, a=3, b=1))


# data =

# def incr(x):
#     return x+1
#
# print(list(map(incr,[10,9,8])))


# sports = ['basketball', 'football', "tennis"]

# for i in range(0, 5):
#     print (f'These are the available{sports}')
#     sport = input('Enter your sport:' )
#     sports.append(sport)
#     del(sports[0])
# print(sports)

h = int('0b1001101', 2)
print(h)