# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.

import copy


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ""
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str, self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        result = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                result[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(result)


user_list_1 = [[1, 2, 4], [3, 4, 5], [5, 6, 7]]
user_list_2 = [[11, 21, 41], [31, 41, 51], [51, 61, 71]]

matrix_1 = Matrix(user_list_1)
matrix_2 = Matrix(user_list_2)
print(matrix_1)
print(matrix_2)

matrix_3 = matrix_1 + matrix_2
print(matrix_3)
