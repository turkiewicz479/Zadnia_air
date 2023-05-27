#!/usr/bin/python
# -*- coding: utf-8 -*-
from copy import copy, deepcopy
from typing import Callable, Mapping, Optional


class Product:
    def __init__(self, id_: Optional[str], name: str, price: float) -> None:
        # TODO: Zaimplementuj.
        self.id = id_ if id_ is not None else self.generate_id(name)
        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        self.__price = min([price, 100])

    def __str__(self) -> str:
        return '{self.name} [{self.id}] : ${self.price:.2f}'.format(self=self)

    def __eq__(self, other) -> bool:
        return (self.id == other.id) and (self.name == other.name) and (self.price == other.price)

    @classmethod
    def generate_id(cls, name: str) -> str:
        return ''.join([c for c in name if c != ' ']) + '_' + str(len(name))
    pass


    # TODO: Zaimplementuj.


class Catalogue:
    Inventory = Mapping[str, Product]
    def __init__(self, inventory:Inventory=None)->None:
        self.inventory = deepcopy(inventory) if inventory else{}

    def add_product(self, product: Product)->None:
        self.inventory[product.id]= copy(product)
    def __contains__(self, id_: str)-> bool:
        return id_ in self.inventory


    # TODO: Zaimplementuj.
    pass
