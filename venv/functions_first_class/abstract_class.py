from abc import ABC, abstractmethod


class Car(ABC):  # abstract based class
    def __init__(self, name, engine):
        self.__name = name
        self.__engine = engine
        self.__speed = none

    @abstractmethod
    def speed(self, speed):
        self.__speed = speed


class Car1(Car):
    def speed(self, speed):
        self.__speed = speed * 2

