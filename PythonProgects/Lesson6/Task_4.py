class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Car {self.name} is running")

    def stop(self):
        print(f"Car {self.name} is stopped")

    def turn(self, direction):
        print(f"Car {self.name} turned {direction}")

    def show_speed(self):
        print(f"Car {self.name} -> Current speed: {self.speed}")


class TownCar(Car):
    max_speed = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        print(f"Max speed: {TownCar.max_speed}")
        if self.speed > TownCar.max_speed:
            print("Speed exceeded")


class WorkCar(Car):
    max_speed = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        print(f"Max speed: {WorkCar.max_speed}")
        if self.speed > WorkCar.max_speed:
            print("Speed exceeded")


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


# -----------------------------------------------------------------------
lada = TownCar(speed=60, name="Lada", color="White")
lada.go()
lada.turn("Left")
lada.show_speed()
lada.stop()
print(f"Car {lada.name} is police car: {lada.is_police}")
print(f"Car {lada.name} -> color: {lada.color}")
print()

kamaz = WorkCar(speed=60, name="Kamaz", color="Red")
kamaz.go()
kamaz.turn("Right")
kamaz.show_speed()
kamaz.stop()
print(f"Car {kamaz.name} is police car: {kamaz.is_police}")
print(f"Car {kamaz.name} -> color: {kamaz.color}")
print()

lamborghini = SportCar(speed=250, name="Lamborghini", color="Red")
lamborghini.go()
lamborghini.turn("Right")
lamborghini.show_speed()
lamborghini.stop()
print(f"Car {lamborghini.name} is police car: {lamborghini.is_police}")
print(f"Car {lamborghini.name} -> color: {lamborghini.color}")
print()

bobik = PoliceCar(speed=20, name="Бобик", color="blue")
bobik.go()
bobik.turn("Right")
bobik.show_speed()
bobik.stop()
print(f"Car {bobik.name} is police car: {bobik.is_police}")
print(f"Car {bobik.name} -> color: {bobik.color}")
print()
