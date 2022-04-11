class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула {direction}'

    def show_speed(self):
        return f'Ваша скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Вы нарушаете скоростной режим. Ваша скорость {self.speed}'
        else:
            return f'Ваша скорость {self.speed} в пределах допустимого'

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы нарушаете скоростной режим. Ваша скорость {self.speed}'
        else:
            return f'Ваша скорость {self.speed} в пределах допустимого'


class PoliceCar(Car):
    pass


town = TownCar(130, 'Black', 'BMW', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('Налево'),town.turn('Направо'), town.stop())

sport = SportCar(200, 'Purple', 'BMW M5', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('Налево'), sport.stop())

work = WorkCar(20, 'Red', 'Lada', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('Направо'), work.stop())

police = PoliceCar(100, 'White', 'Skoda', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('Направо'), police.stop())