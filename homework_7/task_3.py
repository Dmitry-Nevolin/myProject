# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки
# арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение
# (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
# аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

class Cell:

    def __init__(self, cell_number):
        self.cell_number = cell_number

    def __add__(self, other):
        self.cell_number = self.cell_number + other.cell_number
        return Cell(self.cell_number)

    def __sub__(self, other):
        self.cell_number = self.cell_number - other.cell_number
        if self.cell_number > 0:
            return Cell(self.cell_number)
        else:
            return "Невозможно произвести данное действие"

    def __mul__(self, other):
        self.cell_number = round(self.cell_number * other.cell_number)
        return Cell(self.cell_number)

    def __truediv__(self, other):
        self.cell_number = self.cell_number // other.cell_number
        return Cell(self.cell_number)

    def make_order(self):
        result = divmod(self.cell_number, 5)
        for el in range(0, result[0]):
            print("*****\n")
        print("*" * result[1])


my_cell_1 = Cell(int(input("Введите число: ")))
my_cell_2 = Cell(int(input("Введите число: ")))
result = my_cell_1 + my_cell_2
print(result.make_order())  # В конце выплоления выдает еще и None, не могу найти причину(
print("Программа завершена")
