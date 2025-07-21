from abc import ABC, abstractmethod

class Student:
    def __init__(self, name, grade, password):
        self.name = name
        self._grade = grade
        self.__password = password

    def change_password(self, new_pass):
        self.__password = new_pass
        print('пароль успешно изменен')

    def get_info(self):
        print(f"Имя:{self.name}, Оценка:{self._grade}, Пароль:{self.__password}")

student1 = Student("Сабрина", 11, 1233221)
student1.change_password("6757")
student1.get_info()


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car is stopped")

class Bike(Vehicle):
    def move(self):
        print("Bike is moving")

    def stop(self):
        print("Bika is stopped")

car = Car()
bike = Bike()
car.move()
car.stop()
bike.move()
bike.stop()