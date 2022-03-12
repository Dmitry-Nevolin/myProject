# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:

    def __init__(self, data):
        self.data = data

    @classmethod
    def get_int(cls, data):
        data_list = data.split("-")
        return f"День: {int(data_list[0])}\nМесяц: {int(data_list[1])}\nГод: {int(data_list[2])}"

    @staticmethod
    def validation():
        data_list = data.split("-")
        if int(data_list[1]) > 12 or int(data_list[1]) < 1:
            return "Неверные данные по месяцу"
        elif int(data_list[0]) > 31 or int(data_list[0]) < 1:
            return "Неверные данные по дню"
        elif int(data_list[2]) < 1:
            return "Неверные данные по году"
        elif int(data_list[1]) == 2 and int(data_list[0]) > 29:
            return "Неверные данные по дню и месяцу"
        else:
            return "Программа завершена"


data = f"{input('Введите день: ')}-{input('Введите месяц: ')}-{input('Введите год: ')}"
print(Data.get_int(data))
print(Data.validation())
