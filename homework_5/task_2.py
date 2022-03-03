# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open("task_2", "r") as file_obj:
    content = file_obj.readlines()
    print(f"Количество строк: {len(content)}")
    n = 0
    for el in content:
        el = el.split(" ")
        n += 1
        print(f"Количество слов с строке № {n}: {len(el)}")
