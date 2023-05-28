#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import abstractmethod
from typing import TypeVar, Container


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


def compute_min_travel_duration(distance: float, vehicle: Vehicle) -> float:
    return distance / vehicle.max_speed()


def compute_min_travel_duration_as_string(distance: float, vehicle: Vehicle) -> str:
    return "{:.3f} h".format(distance / vehicle.max_speed())


C = TypeVar('C', bound=Vehicle)


def vehicle_collection_as_string(collection: Container[C]) -> str:
    return "\n".join(map(str, collection))


class Movable:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def move(self, dx: float, dy: float):
        self.x = self.x + dx
        self.y = self.y + dy
