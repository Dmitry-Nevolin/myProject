# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять
# список необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.

class MyException(Exception):

    def __init__(self, text):
        self.text = text


el = None
work_list = []
while el != "Stop":
    try:
        while True:
            el = input("Введите число (Если хотите завершить ввод, введите 'Stop'): ")
            if el == "Stop":
                break
            elif not el.isdigit():
                raise MyException("Необходимо вводить только числа. Попробуйте заново")
            else:
                work_list.append(el)
        print(f"Результат: {work_list}")
    except MyException as err:
        print(err)
