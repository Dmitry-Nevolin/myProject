# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

month = int(input("Введите номер месяца: "))
year_list = []
year_dict = {}
if month < 3 or month == 12:
    year_dict.setdefault(month, "зима")
    year_list.append(month)
elif month in range(3, 5):
    year_dict.setdefault(month, "весна")
    year_list.append(month)
elif month in range(6, 8):
    year_dict.setdefault(month, "лето")
    year_list.append(month)
elif month in range(9, 11):
    year_dict.setdefault(month, "осень")
    year_list.append(month)
print(f"{year_list[0]} месяц относится к такому времени года, как {year_dict.get(month)}")
