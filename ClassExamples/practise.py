"""print("Piagram A")
for i in range(1, 21, 2):
    print(('*' * i).center(20))

print("Diagram B")
for i in range(1, 11):
    print("*" * i)

print("Diagram c")
for i in range(1, 11):
    print(("*" * i).rjust(10))
print("Diagram")
for i in range(11, 0, -1):
    print("*" * i)

print("Diagram E")
for i in range(11, 0, -1):
    print(("*" * i).rjust(11))

print("Diagram F")
for i in range(21, 0, -2):
    print(("*" * i).center(22))

    for i in range(1, 11):
        print(("*" * i).rjust(10))

binary = "1011001001"
print(binary.replace("1","0"))

binary = "1011001001"
print(binary.replace("1", "#").replace("0", "1").replace("#","0"))

binary = "1011001001"
print(binary.translate(str.maketrans("01", "10")))


name = "Banke Owolabi"
print(name.translate(str.maketrans("B", "b", "Owa")))

numbers = "0123502351163"
print(numbers.translate(str.maketrans("021", "888", "3")))

print("Sorry, is this the {} minute {}".format(5, 'ARGUMENT'))"""
import math

"""import math

l = "Sorry is this the {} minute {}?".format(5, 'Arguement')

print("{} is {} years old".format("Bill", 25))

print("{:^10} is {:.2E} years old".format("Bill", math.pi*100))

print("{:^10} is {:.2%} years old".format("Bill", math.pi*100))

for i in range (1, 11):
    sym = "*" * i
    print("{:10}".format(sym))

for i in range(1, 11):
    sym = "*" * i
    print(f"{sym:10}")"""


"""l = f"Sorry is this the {5} minute {'Argument'}?"


minute = 5
arg = 'Argument'
l = f"Sorry is this the {minute =} minute {arg =}?"
print(l)
"""

"""def add(first_number: int, second_number: int) -> int:

    
    Add two numbers
    :param first_number:
    :param second_number:
    :return:
    """
"""
    return first_number + second_number

print(add(2,3))
print(add('2', '3'))
print(add.__doc__)
print(add.__name__)
print(add.__annotations__)
    #help(add)"""

"""def get_digit(number, position):
    return digit at position in number, counting from right
    return number//(10 ** position)%10

print(get_digit(3794, 2))"""

"""def get_length(number):
    :return number 
    return len(str(number))

print(get_length(7783))"""
"""
def get_length(number):
    import math
    return math.ceil(math.log10(number))

print(get_length(7783))"""

"""def get_floor(number):
    import math
    return math.floor(math.log10(number))

print(get_floor(7889))"""

"""def get_anagram(number):
    square_number = int(math.pow(number, 2))
    other_number = (math.sqrt(square_number))
    if square_number.endswith(other_number):
        return number("This number is an anagram")
    else:
        return number("This number is not an anagram")

print(get_anagram(600))
"""


