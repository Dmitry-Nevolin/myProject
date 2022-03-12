# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад
# и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве
# единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Storage:

    def __init__(self):
        self.kind_and_quantity = {}

    def take_equipment(self, equipment):
        for key, value in equipment.items():
            if key in self.kind_and_quantity:
                if not value.isdigit():
                    print("Ошибка")
                else:
                    self.kind_and_quantity[key] += int(value)
            else:
                if not value.isdigit():
                    print("Ошибка")
                else:
                    self.kind_and_quantity[key] = int(value)

    def __str__(self):
        return f"{self.kind_and_quantity}"


class Equipment(Storage):

    def __init__(self, quantity):
        super().__init__()
        self.quantity = quantity


class Printers(Equipment):

    def __init__(self, quantity, type_of):
        super().__init__(quantity)
        self.type_of = type_of

    def make_thing(self):
        return {self.type_of: self.quantity}


class Scanners(Equipment):

    def __init__(self, quantity, type_of):
        super().__init__(quantity)
        self.type_of = type_of

    def make_thing(self):
        return {self.type_of: self.quantity}


class Copiers(Equipment):

    def __init__(self, quantity, type_of):
        super().__init__(quantity)
        self.type_of = type_of

    def make_thing(self):
        return {self.type_of: self.quantity}


my_storage = Storage()
work_list = []
printer_1 = work_list.append((Printers(input("Введите количество принтеров: "), "Printers")).make_thing())
printer_2 = work_list.append((Printers(input("Введите количество принтеров: "), "Printers")).make_thing())
scanner_1 = work_list.append((Scanners(input("Введите количество сканнеров: "), "Scanners")).make_thing())
copier_1 = work_list.append((Copiers(input("Введите количество принтеров: "), "Copiers")).make_thing())
for i in work_list:
    my_storage.take_equipment(i)
print(my_storage)
