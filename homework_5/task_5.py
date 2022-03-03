# Создать(программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open("task_5", "w") as file_obj:
    content = input("Введите ряд чисел через пробел: ")
    file_obj.write(content)
with open("task_5", "r") as file_obj:
    content = file_obj.readlines()
    sum_list = []
    for el in content:
        el = el.split(" ")
        for i in el:
            i = int(i)
            sum_list.append(i)
        print(sum(sum_list))
