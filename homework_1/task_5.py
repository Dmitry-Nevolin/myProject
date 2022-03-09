revenue = int(input("Введите значение Вашей выручки (в рублях): "))
costs = int(input("Введите значение Ваших издержек (в рублях): "))

if revenue > costs:
    profit = revenue - costs
    profitability = profit / revenue * 100
    print(f"Ваша выручка соствляет {profit} рублей, а рентабельность равна {profitability} %")
    staff = int(input("Введите число сотрудников: "))
    profit_per_employee = profit / staff
    print(f"Ваша прибыль на одного сотрудника составляет {profit_per_employee} рублей")
elif revenue == costs:
    print("Ваше предприятие работает в ноль")
else:
    loses = costs - revenue
    print(f"Ваши убытки составили {loses} рублей")
