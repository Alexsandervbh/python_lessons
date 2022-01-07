# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Поехал(а) {self.name}.'

    def stop(self):
        return f' \n Остановился (ась) {self.name}.'

    def turn(self, direction):
        return f' \n {self.name} повернул (а) {direction}'

    def show_speed(self):
        return f' \n Ваша скорость {self.speed} км/ч'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\n Ваша скорость привышена! И составляет: {self.speed} км/ч'
        else:
            return f'\n Скорость не превышена {self.speed} км/ч'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\n Ваша скорость привышена! И составляет: {self.speed} км/ч'
        else:
            return f'\n Скорость не превышена {self.speed} км/ч'

class PoliceCar(Car):
    pass

town = TownCar(90, 'grey', 'Mazda', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('На лево'), town.turn('На право'), town.stop())

sport = SportCar(250, 'blue', 'Maserati', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('На право'), sport.stop())

work = WorkCar(40, 'white', 'Kamaz', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('На право'), work.stop())

police = PoliceCar(55, 'white', 'Volga',True)
print('4:\n' + police.go(), police.show_speed(), police.turn('На лево'), police.turn('На право'), police.stop())