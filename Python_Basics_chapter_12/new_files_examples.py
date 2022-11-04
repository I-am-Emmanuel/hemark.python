from pathlib import Path

path = Path.home() / 'hello.txt'
path.touch()

file = path.open(mode="r", encoding="utf-8")
file = 'Holla\nEkaasan\nBonjour\nGoodmorning'

with path.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line)
    # print(line, end='')
