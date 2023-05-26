#!/usr/bin/python
# -*- coding: utf-8 -*-
import from typing import  Mapping

class Product:
    def __init__(self, id_: str, name: str, price: float) -> None:
        # TODO: Zaimplementuj.
        self.id = id_
        self.name = name
        self.price = price
    def __str__(self)->str:
        return '{self.name} [{self.id}] : ${self.price:.2f}'.format(self=self)
    def __eq__(self, other)-> bool:
        return self.id == other.id and self.name == other.name and self.price == other.price
    pass

    # TODO: Zaimplementuj.


class Catalogue:
    Inventory = Mapping[str, Product]
    def __init__(self, inventory:Inventory):

    # TODO: Zaimplementuj.
    pass
