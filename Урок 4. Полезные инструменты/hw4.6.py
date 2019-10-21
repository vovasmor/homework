"""

Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.

"""
from itertools import count
from itertools import cycle
from random import sample

# бесконечный итератор, генерирующий целые числа, начиная с указанного,
for el in count(7):
    print(el)


# бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
my_list = sample(range(0,100), 20)
for el in cycle(my_list):
    print(el)