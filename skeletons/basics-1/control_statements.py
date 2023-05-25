#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Instrukcje sterujące
#
# -----------------------------------------------------------------------------


def parity_str(n: int) -> str:
    if n%2==0:
        return "parzysta"
    else:
        return "nieparzysta"
    """Zwróć łańcuch znaków "parzysta" jeśli `n` jest liczbą parzystą, a w przeciwym
    razie – zwróć łańcuch znaków "nieparzysta".

    W implementacji użyj wyrażenia warunkowego (ciało funkcji powinno składać się
    z jednej instrukcji!).

    Przykład: parity_str(2) => "parzysta", parity_str(3) => "nieparzysta"

    :param n: liczba, której parzystość jest badana
    :return: "parzysta" jeśli `n` jest liczbą parzystą, w przeciwym razie "nieparzysta"
    """
    pass


def plf(x: float) -> float:
    """Funkcja realizuje funkcję matematyczną:
            / 1   jeśli x < 3
    f(x) = {  1.5 jeśli x ∈ [3, 10)
            \ 4   jeśli x ≥ 10

    Przykład: plf(3) = 1.5, plf(10) = 4

    :param x: liczba rzeczywista
    :return: wartość funkcji f(x)
    """
    if x<3.0:
        return 1
    elif  x<10:
        return 1.5
    else:
        return 4

    pass


def factorial(n: int) -> int:
    """Oblicz silnię liczby.

    W implementacji użyj pętli `for`. Przyjmij, że `n` jest zawsze większe
    od 0 (nie musisz tego sprawdzać).

    Przykład: factorial(3) = 6, factorial(4) = 24 itd.

    :param n: liczba naturalna
    :return: silnia liczby `n`
    """
    sum=1
    for x in range(1,n+1):
        sum=sum*x
    return sum
    pass


def min_pow_2(n: int) -> int:
    """Oblicz najmniejszą potęgę 2 większą od zadanej liczby naturalnej `n`.

    W implementacji użyj pętli `while`. Przyjmij, że `n` jest zawsze większe
    od 0 (nie musisz tego sprawdzać).

    Przykład: min_pow_2(5) = 8, min_pow_2(8) = 16 itd.

    :param n: liczba naturalna
    :return: najmniejszą potęgę 2 większą od zadanej liczby całkowitej `n`
    """
    x=1
    while x<=n:
        x=x*2
    x*2
    return x
    pass
