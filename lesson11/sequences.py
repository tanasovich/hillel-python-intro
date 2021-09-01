"""
Numeric sequences

Module implements three functions, which produce different numeric
sequences. These functions realized in recursive way.
"""
from math import log10

__all__ = ["reverse_it", "without_00", "count_first"]


def reverse_it(n: int) -> int:
    """
    Accepts integer number (positive) and returns it's reversed
    variant.
    :param n: number to be reversed
    :return: reversed number
    """
    if n > 10:
        digit = n % 10
        not_yet_reversed = n // 10
        digits_count = int(log10(not_yet_reversed) + 1)

        return digit * 10**digits_count + reverse_it(not_yet_reversed)
    else:
        return n


def without_00(a: int, b: int) -> int:
    """
    Determines how much sequences with a zeroes and b ones exists
    without two zeroes subsequences.
    :param a: zeroes quantity
    :param b: ones quantity
    :return: number of combinations
    """
    if a == 0:
        return 1
    if a == 1:
        return b + 1
    if a > 1 and b == 0:
        return 0

    return without_00(a - 1, b - 1) + without_00(a, b - 1)


def count_first(nums, n: int) -> list:
    """
    Accepts n and return elements (until nth index) from A002024
    numeric sequence.
    A002024 is a such sequence where each ith element appears i times.
    (see https://oeis.org/A002024)
    :param nums: numeric list
    :param n: index of element from the sequence
    :return: nth element
    """
    def a(k: int) -> int:
        if k == 1:
            return 1
        return a(k - a(k - 1)) + 1

    sequence = list()

    for i in range(1, n + 1):
        sequence.append(a(i))

    return sequence
