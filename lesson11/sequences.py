from math import log10


def reverse_it(n: int) -> int:
    if n > 10:
        digit = n % 10
        not_yet_reversed = n // 10
        digits_count = int(log10(not_yet_reversed) + 1)

        return digit * 10**digits_count + reverse_it(not_yet_reversed)
    else:
        return n


def without_00(a: int, b: int) -> int:
    if a == 0:
        return 1
    if a == 1:
        return b + 1
    if a > 1 and b == 0:
        return 0

    return without_00(a - 1, b - 1) + without_00(a, b - 1)


def count_first(nums, n: int) -> list:
    def a(k: int) -> int:
        if k == 1:
            return 1
        return a(k - a(k - 1)) + 1

    sequence = list()

    for i in range(1, n + 1):
        sequence.append(a(i))

    return sequence
