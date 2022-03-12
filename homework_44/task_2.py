# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

numbers = [100, 109, 110, 77, 87]

new_numbers = [el for el in numbers[1:] if numbers[numbers.index(el)] > numbers[numbers.index(el) - 1]]

print(new_numbers)
