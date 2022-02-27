# Реализовать два небольших скрипта: итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.

from itertools import count, cycle
start = int(input("Введите число: "))
finish = int(input("Введите число: "))
generator_1 = count(start)
for el in generator_1:
    if el == finish + 1:
        break
    else:
        print(el)

numbers = input("Введите числа через пробел: ").split(" ")
numbers = list(numbers)
new_numbers = []
generator_2 = cycle(numbers)
condition = int(input("Укажите количество запрашиваемых элементов: "))
for el in generator_2:
    if len(new_numbers) >= condition:
        break
    else:
        new_numbers.append(el)
for i in new_numbers:
    print(i)
