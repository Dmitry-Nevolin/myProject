# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


user_name = input("Введите Ваше имя: ")
user_surname = input("Введите Вашу фамилию: ")
user_position = input("Введите Вашу должность: ")
income_dict = {"wage": int(input("Введите размер зарплаты: ")), "bonus": int(input("Введите размер бонусов: "))}
worker_1 = Position(user_name, user_surname, "Teacher", income_dict)
full_name = worker_1.get_full_name()
total_income = worker_1.get_total_income()
print(f"{full_name}, работающий на такой должности, как {user_position}, получает {total_income} рублей")
