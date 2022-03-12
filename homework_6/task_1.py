# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

import time


class Trafficlight:

    def __init__(self, __color, running):
        self.__color = __color
        self.running = running

    def color_change(self):
        if self.__color == "Red":
            time.sleep(self.running)
            return f"\033[31m{self.__color}"
        elif self.__color == "Yellow":
            time.sleep(self.running)
            return f"\033[33m{self.__color}"
        elif self.__color == "Green":
            time.sleep(self.running)
            return f"\033[32m{self.__color}"
        elif self.__color == "Stop":
            time.sleep(self.running)
            return "\033[37mПрограмма завершена"
            # change_index -= 1


seconds_for_green = int(input("Введите количество секунд для зеленого цвета: "))
use_dict = {0: "Red", 7: "Yellow", 2: "Green", seconds_for_green: "Stop"}
for key, value in use_dict.items():
    lights = Trafficlight(value, key)
    print(lights.color_change())
