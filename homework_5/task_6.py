# Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

final_dict = {}

with open("task_6", "r") as file_obj:
    for line in file_obj:
        subject, lecture, practice, lab = line.split()
        final_dict[subject] = int(lecture) + int(practice) + int(lab)
    print(final_dict)
