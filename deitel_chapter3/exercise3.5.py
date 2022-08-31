print("Enter any two numbers and I tell you their relationship")

first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

if first_number == second_number:
    print(f'{first_number} is equal to {second_number}\n'
          f'{first_number} is not greater than {second_number}\n{first_number} is not less than {second_number}')

elif first_number > second_number and first_number != second_number:
    print(f'{first_number} is greater than {second_number}\n{first_number} is not equal to {second_number}\n'
          f'{second_number} is less than {first_number}')

elif second_number > first_number and second_number != first_number:
    print(f'{second_number} is greater than {first_number}\n'
          f'{second_number} is not equal to {first_number}\n{first_number} is less than {second_number}')



