# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!

def count(figure):
    current = 1
    factorial = 1
    while current != figure + 1:
        factorial = factorial * current
        yield factorial
        current += 1


for el in count(int(input("Введите число: "))):
    print(el)
