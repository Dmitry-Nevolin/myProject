# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.

class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def weight_count(self, asphalt, thickness):
        return self._length * self._width * asphalt * thickness


length = int(input("Введите значение длины дороги: "))
width = int(input("Введите значение ширины дороги: "))
result = Road(length, width)
print(result.weight_count(25, int(input("Введите толщину асфальта: "))))
