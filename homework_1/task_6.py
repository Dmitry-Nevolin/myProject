distance_in_process = int(input("Введите расстояние за 1-й день пробежки (в км): "))
distance_n = int(input("Введите расстояние, которого вы хотите достичь (в км): "))
increase = 0.1
days = 1
print(f"{days}-й день: {distance_in_process}")

while distance_in_process < distance_n:
    distance_in_process = distance_in_process + distance_in_process * increase
    days += 1
    print(f"{days}-й день: {distance_in_process:.2f} км")
print(f"Ответ: на {days}-й день спортсмен достиг результата - не менее {distance_n} км")
