user_number = int(input("Введите целое положительное число: "))
max_figure = user_number % 10
while user_number >= 1:
    user_number = user_number // 10
    if user_number % 10 > max_figure:
        max_figure = user_number % 10
    if user_number > 9:
        continue
    else:
        print(f"{max_figure} является наибольшей цифрой в загаданном Вами числе")
        break
