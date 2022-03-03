# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open("task_4", "r") as file_obj:
    content = file_obj.readlines()
print(content)
content_list_1 = []
content_list_2 = []
content_list_3 = []
translate_list = ["Один", "Два", "Три", "Четыре"]
for el in content:
    el = el.split(" ")
    content_list_1.append(el[0])
    content_list_2.append(el[1])
    content_list_3.append(el[2])
content_list_1 = translate_list

with open("task_4_1", "w") as file_obj:
    i = 0
    first_els = content_list_1
    second_els = content_list_2
    third_els = content_list_3
    while i < 4:
        file_obj.write(f"{first_els[i]} {second_els[i]} {third_els[i]} \n",)
        i += 1
