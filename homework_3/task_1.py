# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def multi(figure_1, figure_2):
    return figure_1 / figure_2


figure_1 = int(input("Введите число: "))
figure_2 = int(input("Введите число: "))

if figure_2 == 0:
    print("Ошибка")
elif figure_1 % figure_2 == 0:
    print(int(multi(figure_1, figure_2)))
else:
    print(multi(figure_1, figure_2))
