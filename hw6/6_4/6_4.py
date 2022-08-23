# 4. Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.
from random import choice
from lib6_4 import out_red, out_default, out_blue, out_yellow


class Car:
    direction = ['направо', 'налево', 'вперед', 'назад']

    def __init__(self, s, c, n, is_police=False):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = is_police

    @staticmethod
    def go():
        out_default(f'поехала')

    @staticmethod
    def stop():
        out_default(f'остановилась')

    def turn(self):
        out_default(f'направление: {choice(self.direction)}')

    def show_speed(self):
        out_default(f'скорость: {self.speed}')

    def show_car(self):
        return out_red(f"Полицейская машина: {self.color} {self.name}") if self.is_police else out_default(
            f'Гражданская машина: {self.color} {self.name}')


class TownCar(Car):
    __max_speed = 60

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > self.__max_speed:
            out_yellow('ПРЕВЫШЕНИЕ СКОРОСТИ')


class WorkCar(Car):
    __max_speed = 40

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > self.__max_speed:
            out_yellow('ПРЕВЫШЕНИЕ СКОРОСТИ')


class SportCar(Car):
    def __init__(self, s, c, n, is_police, r):
        super().__init__(s, c, n, is_police)
        self.reputation = f'Репутация +{r * s}'

    def show_speed(self):
        Car.show_speed(self)
        out_blue(self.reputation)


class PoliceCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n, is_police=True)


car_1 = TownCar(100, 'белый', 'Volvo', False)
car_2 = WorkCar(40, 'синий', 'CAT', False)
car_3 = SportCar(220, 'красная', 'Ferrari', False, 1.2)
car_4 = PoliceCar(200, 'белый', 'Mercedes')

car_list = [car_1, car_2, car_3, car_4]

for car in car_list:
    car.show_car()
    car.go()
    car.turn()
    car.show_speed()
    car.stop()
    out_default('*' * 30)
