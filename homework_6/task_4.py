# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed != 0:
            return "Машина поехала"

    def stop(self):
        if self.speed == 0:
            return "Машина остановилась"

    def turn(self):
        direction = int(input("Если поворот направо, введите 1; если налево - 2"))
        if direction == 1:
            return "Машина повернула направо"
        if direction == 2:
            return "Машина повернула налево"

    def show_speed(self):
        return f"Скорость равна {self.speed}"


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f"Скорость больше {self.speed}, необходимо снизить скорость"
        else:
            return f"Скорость равна {self.speed}"


class SportCar(Car):

    def show_speed(self):
        return f"Скорость равна {self.speed}"


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f"Скорость больше {self.speed}, необходимо снизить скорость"
        else:
            return f"Скорость равна {self.speed}"


class PoliceCar(Car):

    def show_speed(self):
        return f"Скорость равна {self.speed}"


user_speed = int(input("Введите показатель скорости: "))
user_color = input("Введите цвет Вашей машины: ")
user_name = input("Введите марку Вашей машины: ")
user_is_police = int(input("Если машина полицейская, введите 1; если нет - 2: "))
if user_is_police == 1:
    final_user_is_police = True
else:
    final_user_is_police = False


if final_user_is_police is False:
    car_1 = TownCar(user_speed, user_color, user_name, final_user_is_police)
    print(car_1.go())
    print(car_1.stop())
    print(car_1.turn())
    print(car_1.show_speed())
    car_2 = SportCar(user_speed, user_color, user_name, final_user_is_police)
    print(car_2.go())
    print(car_2.stop())
    print(car_2.turn())
    print(car_2.show_speed())
    car_3 = WorkCar(user_speed, user_color, user_name, final_user_is_police)
    print(car_3.go())
    print(car_3.stop())
    print(car_3.turn())
    print(car_3.show_speed())
else:
    car_4 = PoliceCar(user_speed, user_color, user_name, final_user_is_police)
    print(car_4.go())
    print(car_4.stop())
    print(car_4.turn())
    print(car_4.show_speed())
