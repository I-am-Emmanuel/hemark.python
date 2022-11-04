from demostrating_private_attributes import PrivateClass

class PrivateData:
    pass


my_object = PrivateClass()

print(my_object.public_data)
# print(my_object.__private_data()) This will not work calling a private attributes without a ClasName
print(my_object._PrivateClass__private_data)

my_object._PrivateClass__private_data = 'modified'
print(my_object._PrivateClass__private_data)