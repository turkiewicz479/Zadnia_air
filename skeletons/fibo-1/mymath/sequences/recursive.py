#!/usr/bin/python
# -*- coding: utf-8 -*-
def fib(n: int) -> List[int]:
    """Zwróć n pierwszych elementów ciągu Fibonacciego.

    Parametry:
     n -- liczba elementów ciągu do wygenerowania
    """
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(b)
        a, b = b, a + b
    return result