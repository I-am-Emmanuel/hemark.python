from pathlib import Path

path = Path.home() / 'starships.txt'
path.touch()
lists = [
          'Discovery\n',
          'Enterprise\n',
          'Defiant\n',
          'Voyager\n'
                    ]
with path.open(mode='w', encoding='utf-8') as file:
    file = file.writelines(lists)
    # file = file.write('Discovery\nEnterprise\nDefiant\nVoyager\n')


with path.open(mode='r', encoding='utf-8')as file:
    file = file.read()
for line in lists[0::2]:
    print(line, end='')