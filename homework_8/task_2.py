# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyException(Exception):

    def __init__(self, text):
        self.text = text


try:
    dividend = int(input("Введите число: "))
    divider = int(input("Введите число: "))
    if divider == 0:
        raise MyException("Делить на ноль нельзя")
except MyException as err:
    print(err)
else:
    print(dividend / divider)
