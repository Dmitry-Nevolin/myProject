# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 4, 2, 1]
number = int(input("Введите цифру: "))
i = 0
if number in my_list:
    my_list.insert(my_list.index(number) + 1, number)
else:
    while True:
        if number > my_list[i]:
            my_list.insert(i, number)
            break
        elif number < my_list[i]:
            i += 1

print(f"New list: {my_list}")
