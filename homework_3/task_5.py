# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

def sum_func():
    numbers = input("Введите числа через пробел (для выхода из программы введите 'x'): ").split()
    work_list = list(numbers)
    result = 0
    next_step = 1
    for i in work_list:
        if i == "x":
            next_step += 1
            break
        else:
            result = result + int(i)
    print(result)
    while "x" not in work_list:
        next_step = int(input("Если хотите добавить чисел, введите 1: "))
        if next_step == 1:
            new_numbers = input("Введите числа через пробел: ").split()
            work_list = list(new_numbers)
            for figure in work_list:
                if figure == "x":
                    break
                else:
                    result = result + int(figure)
                    continue
        else:
            print("Программа завершена")
            break

        print(result)

    print(f"Итоговая сумма - {result}")


sum_func()
