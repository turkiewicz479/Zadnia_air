#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Krotki
#
# -----------------------------------------------------------------------------

from typing import List, Any, Tuple, Union


def tuple_from_numbers(a: int, b: int) -> Union[Tuple[()], Tuple[int, int]]:
    """Jeśli liczby `a` i `b` są równe zwraca pustą krotkę, jeśli nie – zwraca
        krotkę złożoną z tych liczb.
    """
    if a==b:
        return ()
    else:
        return (a,b)
    pass


def tuple_from_elements(lst: List[int]) -> Union[Tuple[int, ...], Tuple[None, ...]]:
    """Jeśli lista zawiera co najmniej 3 elementy – zwraca krotkę złożoną z trzech
    pierwszych elementów listy, jeśli nie – zwraca krotkę (None, None, None).

    W implementacji:
    - do tworzenia krotki złożonej z trzech elementów listy NIE korzystaj z zapisu
    z użyciem przecinka, tylko użyj slice'ingu oraz funkcji wbudowanej tuple()
    - do tworzenia krotki (None, None, None) NIE korzystaj z zapisu z użyciem
    przecinka, tylko użyj operatora mnożenia * dla krotki (None,).

    Wywołaj funkcję tuple_from_elements() tak, aby zwrócona krotka została
    rozpakowana do zmiennych `a`, `b` i `c` (wypisz te zmienne).
    """
    if len(lst)>=3:
        return (lst[0],lst[1],lst[2])
    else:
        return (None,None,None)
    pass


def append_tuple_to_list(lst: List[Any], tpl: Tuple[Any, Any]) -> List[Any]:
    """Dopisz na koniec listy elementy z krotki.

    W implementacji NIE korzystaj z funkcji list(), tylko z metody extend()!
    """
    list= lst.copy()
    x,y=tpl
    list.append(x)
    list.append(y)
    return list
    pass
