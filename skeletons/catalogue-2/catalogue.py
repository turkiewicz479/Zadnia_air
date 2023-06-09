#!/usr/bin/python
# -*- coding: utf-8 -*-


from copy import copy, deepcopy
from typing import Callable, Mapping, Optional, List




class Product:
    def __init__(self, id_: Optional[str], name: str, price: float) -> None:
        if len(name) > 20:
            raise ValueError(f"Name too long ({len(name)} chars)")
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
        """Wygeneruj ID zgodnie z regułą: usuń spacje i dodaj na koniec liczbę wszystkich znaków w nazwie.
        """
        return ''.join([c for c in name if c != ' ']) + '_' + str(len(name))

    @classmethod
    def from_string(cls, string: str) -> 'Product':
        params = {}
        for param in string.split(';'):
            key, value = param.split('=')
            params[key.strip()] = value.strip()

        id_ = params.get('id')
        name = params.get('name')
        price = float(params.get('price', 0.0))

        return cls(id_=id_, name=name, price=price)


class InventoryOverflowException(Exception):
    pass



class Catalogue:
    Inventory = Mapping[str, Product]

    def __init__(self, inventory: Inventory = None) -> None:
        if inventory is not None and len(inventory) > 2:
            raise InventoryOverflowException("Initial inventory exceeds the limit of 2 products.")
        self.inventory = deepcopy(inventory) if inventory else {}

    def add_product(self, product: Product) -> None:
        if len(self.inventory) >= 2:
            raise InventoryOverflowException("Limit of 2 products in the catalogue has been reached.")
        self.inventory[product.id] = copy(product)

    def add_products(self, products: List[Product]) -> int:
        added_count = 0
        for product in products:
            try:
                self.add_product(product)
                added_count += 1
            except InventoryOverflowException:
                print(f"Error when adding product: {str(product)}")
                print("   Reason: inventory overflow")
                break
        return added_count

    def __contains__(self, id_: str) -> bool:
        return id_ in self.inventory

    def get_products_with_appropriate_price(self, predicate: Callable[[float], bool]) -> Inventory:
        return {k: v for (k, v) in self.inventory.items() if predicate(v.price)}

    def get_products_by_name_part(self, chunk: str, ignore_case: bool = False) -> Inventory:
        has_chunk = (lambda name, chunk_: chunk_.lower() in name.lower()) if ignore_case \
            else (lambda name, chunk_: chunk_ in name)
        return {k: v for (k, v) in self.inventory.items() if has_chunk(v.name, chunk)}
