from pathlib import Path

# path = Path.home() / "new_folder" / "new_file.txt"
# path.parent.mkdir(parents=True)
# with path.open(mode='w', encoding='utf-8') as file:
#     file = file.write('Documents file')
# print()

# path = Path.home() / 'Chatting.txt'
# path.touch()
# with path.open(mode='w', encoding='utf-8') as file:
#     file = file.write("Hello bro, I would like to meet and talk to you anytime you are free")
#
# with path.open(mode='r', encoding='utf-8') as file:
#     file = file.read()
#
# with path.open(mode='a', encoding='utf-8') as file:
#     file = file.write("\nJust call my phone number when you're free")
#
# with path.open(mode='r', encoding='utf-8') as file:
#     file = file.read()
#     print(file)
#
# path = Path.home() / 'Animal_type.txt'
# path.touch()
# list_of_lists = [
#     'Goat\n',
#     'Hen\n',
#     'Lion\n',
#     'Tiger\n',
#     'Snake\n',
#     'Snail\n',
#     'Elephant\n'
# ]
# with path.open(mode='w', encoding='utf-8') as file:
#     file = file.writelines(list_of_lists)
#
# with path.open(mode='r', encoding='utf-8') as file:
#     file = file.read()
# for line in list_of_lists:
#     # print(f'{line[:]}', end='')
#     print(line)

# path = Path.home() / 'new file.txt'
# with path.open(mode='w', encoding='utf-8')as file:
#     file = file.write('Hello docs')

# with path.open(mode='r', encoding='utf-8')as file:
#     file = file.read()
# print(file)
#
# file_path = Path.home() / "temperatures.txt"
# temperature_readings = [68, 65, 68, 70, 74, 72]
# with file_path.open(mode="a", encoding="utf-8") as file:
#     file.write(str(temperature_readings[0]))
# for temp in temperature_readings[1:]:
#     file.write(f",{temp}")
#
# with file_path.open(mode="r", encoding="utf-8") as file:
#     file_path = file.read()
#     print(file_path)

import csv

file_path = Path.home() / 'temperatures.csv'


with file_path.open(mode="w", encoding="utf-8") as file:
    writer = csv.writer(file)
    daily_temperatures = [
        [68, 65, 68, 70, 74, 72],
        [67, 67, 70, 72, 72, 70],
        [68, 70, 74, 76, 74, 73],
    ]
for temp_list in daily_temperatures:
    writer.writerow(file)

with file_path.open(mode="w", encoding="utf-8") as file:
    writer = csv.writer(file)
writer.writerows(daily_temperatures)

with file_path.open(mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
for rows in reader:
    print(rows)
