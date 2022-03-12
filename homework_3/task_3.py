# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.


def my_func(figure_1, figure_2, figure_3):
    figure_list = [figure_1, figure_2, figure_3]
    figure_list_final = []
    max_figure = figure_list[0]
    for i in figure_list:
        if i > max_figure or (i <= max_figure and (i > figure_list[0] or i > figure_list[1] or i > figure_list[2])):
            max_figure = i
            figure_list_final.append(max_figure)
        elif i == max_figure and (i == figure_list[0] and i == figure_list[1] and i == figure_list[2]):
            max_figure = i
            figure_list_final.append(max_figure)
        else:
            continue
    if len(figure_list_final) == 3:
        figure_list_final = figure_list_final[:2]
    return f"Итоговая сумма: {sum(figure_list_final)}"


print(my_func(int(input("Введите число: ")), int(input("Введите число: ")), int(input("Введите число: "))))
