"""
Encapsulation is the process of restricting access to certain parts of an object.
"""

class Car:
    def __init__(self):
        self.__speed = 0 # private attribute

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed
    
    def __str__(self):
        return f"Car with speed: {self.__speed}"
    
    
car = Car()

car.set_speed(100)
print('car speed', car.get_speed())