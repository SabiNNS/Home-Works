class transport:
    def __init__(self, model, speed, fuel):
        self.model = model
        self.speed = speed
        self.fuel = fuel


    def introduse(self):
        return f"Я приехал на {self.model},со скоростью {self.speed} и который использует {self.fuel}."

car = transport("Автомобилe", 130, "бензин")
bus = transport("Автобусe", 90, "дизель")
train = transport("Поездe", 200, "дизель")

print(car.introduse())
print(bus.introduse())
print(train.introduse())
