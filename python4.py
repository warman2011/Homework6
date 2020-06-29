class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала...')

    def stop(self):
        print(f'{self.name} остановилась...')

    def turn_right(self):
        print(f'{self.name} повернула направо!')

    def turn_left(self):
        print(f'{self.name} повернула налево!')

    def show_speed(self):
        print(f'Скорость {self.name}: ', str(self.speed))

    def police(self):
        if self.is_police == True:
            return print(f"{self.name} полиция!!!")
        else:
            return print(f"{self.name} не полиция.")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} у Вас превышение скорости... сбавьте скорость!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


        
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} у Вас превышение скорости... сбавьте скорость!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



auto1 = TownCar(70, 'Red', 'Priora',False)
auto2 = SportCar(100, 'Black', 'BMW', False)
auto3 = WorkCar(50, "White", "Musorovoz", False)
auto4 = PoliceCar(60, "Black", 'lada', True)

print(auto1.speed, auto2.color, auto3.name, auto4.is_police)

auto1.go()
auto1.show_speed()
auto1.turn_left()
auto1.stop()
auto1.police()
auto2.go()
auto2.show_speed()
auto2.turn_left()
auto2.stop()
auto2.police()
auto3.go()
auto3.show_speed()
auto3.turn_left()
auto3.stop()
auto3.police()
auto4.go()
auto4.show_speed()
auto4.turn_left()
auto4.stop()
auto4.police()

