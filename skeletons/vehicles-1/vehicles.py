#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import abstractmethod


class Vehicle:
    def __init__(self, id_: str, brand: str) -> None:
        self.id = id_
        self.brand = brand

    @abstractmethod
    def max_speed(self) -> float:
        pass


class Car(Vehicle):
    def __init__(self, id_: str, brand: str, engine_hp: float):
        super().__init__(id_, brand)
        self.engine_hp = engine_hp

    def __str__(self) -> str:
        return "{self.id} :  {self.brand}".format(self=self)

    def max_speed(self):
        return self.engine_hp


class Bicycle(Vehicle):
    def __init__(self, id_: str, brand: str, n_gears: int):
        super().__init__(id_, brand)
        self.n_gears = n_gears

    def max_speed(self):
        return self.n_gears * 3
