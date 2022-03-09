# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

with open("task_3", "r") as file_obj:
    content = file_obj.readlines()
    salary_list = []
    for el in content:
        el = el.split(" ")
        salary_list.append(int(el[1]))
        if int(el[1]) > 20000:
            print(el[0])
    print(f"Средняя зарплата: {sum(salary_list) / len(salary_list)}")
