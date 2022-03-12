# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def count():
    name, work_hours, money, premium = argv
    work_hours = int(work_hours)
    money = int(money)
    premium = int(premium)
    return work_hours * money + premium


print(count())
