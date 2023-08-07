class Human:
    count = 0

    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
        Human.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def is_minor(age):
        return age < 16

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name: str):
        # print('calling the setter')
        if name.islower():
            raise ValueError('Name cannot be all lower case')
        self._name = name

    # name.deleter
    # def name(self):
    #     print('deleting...')
    #     del self._name
    @age.setter
    def age(self, age: int):
        if age <= 0:
            raise ValueError('Age cannot be zero and  negative figure')
        self._age = age


oruko = Human('Adedoyin', 23)

oruko2 = Human('Jolaoye', 19)
print(oruko.name, oruko.age)
print(oruko2.name, oruko2.age)
print(oruko.is_minor(12))
