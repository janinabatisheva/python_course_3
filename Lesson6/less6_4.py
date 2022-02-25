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

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed() if self.speed <= 60 else print('Превышена скорость!')


class SportCar(Car):
    color = 'яркий'


class WorkCar(Car):
    def show_speed(self):
        super().show_speed() if self.speed <= 40 else print('Превышена скорость!')


class PoliceCar(Car):
    is_police = True


car1 = TownCar(50, 'серебристый', 'Daewoo')
car1.go()
car1.show_speed()

car2 = SportCar(120, 'красно-белый', 'Audi')
car2.stop()

car3 = WorkCar(45, 'желтый', 'Wolkswagen')
car3.turn('влево')
car3.show_speed()

car4 = PoliceCar(80, 'белый', 'Skoda')
car4.turn('вправо')
car4.show_speed()
