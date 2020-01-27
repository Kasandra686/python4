from sys import argv
from itertools import count, cycle

try:
    # итератор, генерирующий целые числа, начиная с указанного,
    script_name, num = argv
    for el in count(int(num)):
        print(el)
        if el > 60:
            break
    # итератор, повторяющий элементы некоторого списка, определенного заранее. например
    list = [23, 5, 6, 1]
    new_list = []
    i = 0
    for el in cycle(list):
        new_list.append(el)
        if i > 10:
            break
        i += 1
    print(f"б){new_list}")
except ValueError:
    print("Необходимо ввести число!")
