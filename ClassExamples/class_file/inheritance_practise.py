class Human:

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def __str__(self):
        return f'name= {self.last_name} {self.first_name}, age= {self.age}, sex= {self.sex}'


class Manager(Human):
    def __init__(self, first_name: str, last_name: str, age: int, sex: str, bonus: float):
        self.bonus = bonus
        super().__init__(first_name, last_name, age, sex)

    def full_name(self):
        return f'{self.last_name[0].upper()} {self.first_name}, {self.age}, {self.sex}'

    def pay_salary(self, salary):
        return salary + self.bonus


class Employee(Human):
    def pay_salary(self, salary):
        return salary
    pass


manager = Manager('Oluwadara', 'Aderogba', 22, 'Male', 2000)
employee1 = Employee('Olasiyan', 'Adebimpe', 23, 'Female')
# print(employee1.full_name(), employee1.age, employee1.sex)
# print(manager.full_name())
#
# human_list = [employee1, manager, Human('Shola', 'Aderogba', 29, 'Hers')]
# for human in human_list:

human_list = [employee1, manager]
for human in human_list:
    print(human.full_name(), human.pay_salary(50000))
    # print(human.pay_salary(50_000))
