from math import sqrt

from ..number_theory.factor import factorize
from ..number_theory.primes import sieves

from ..utils.timeit import timeit


def root(a: int, b: int, c: int) -> float:
    return (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)


def t(n: int) -> float:
    return n * (n + 1) / 2


@timeit
def problem12():
    """
    Highly divisible triangular number
    Problem 12

    The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
    1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

         1: 1
         3: 1,3
         6: 1,2,3,6
        10: 1,2,5,10
        15: 1,3,5,15
        21: 1,3,7,21
        28: 1,2,4,7,14,28

    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?
    """
    max_n = int(1000)
    target = 500
    primes = sieves(max_n)
    k = 1
    old_k = 1
    # First find the search space by multiplying prime numbers until the factorize is
    for prime in primes:
        old_k = k
        k *= prime
        nb_factors = len(factorize(k))
        if nb_factors > target:
            break
    n = int(root(1, 1, -2 * old_k)) + 1
    k = t(n)
    while len(factorize(int(k))) < target:
        n += 1
        k += n
    return int(k)


if __name__ == "__main__":
    problem12()
