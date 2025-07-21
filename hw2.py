class Transport:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        print("Transport is moving")


class Car(Transport):
    def __init__(self, name, speed, fuel):
        super().__init__(name,speed)
        self.fuel = fuel

    def move(self):
        super().move()
        print(f"{self.name} is driving at {self.speed}km/h using {self.fuel}")


class Plane(Transport):
    def __init__(self, name, speed, wingspan):
        super().__init__(name, speed)
        self.wingspan = wingspan

    def move(self):
          super().move()
          print(f"{self.name} is flying at {self.speed}km/h a wingspan of {self.wingspan} meters")


class Boat(Transport):
    def __init__(self, name, speed, sail_type):
        super().__init__(name, speed)
        self.sail_type = sail_type

    def move(self):
        super().move()
        print(f"{self.name} is sailing at {self.speed} knots using a {self.sail_type} sail")

car = Car("Lexus", 120, "petrol")
plane = Plane("Airbus", 800, "70")
boat = Boat("Titanic", 40, "triangular")

car.move()
plane.move()
boat.move()