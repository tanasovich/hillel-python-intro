import math


def reverse_it(n: int) -> int:
    if n > 10:
        digit = n % 10
        not_yet_reversed = n // 10
        digits_count = int(math.log10(not_yet_reversed) + 1)

        return digit * 10**digits_count + reverse_it(not_yet_reversed)
    else:
        return n


if __name__ == "__main__":
    print(reverse_it(1))
    print(reverse_it(1111))
    print(reverse_it(123))
    print(reverse_it(123456789))
