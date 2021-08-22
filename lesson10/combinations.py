def without_00(a: int, b: int) -> int:
    if a == 0:
        return 1
    if a == 1:
        return b + 1
    if a > 1 and b == 0:
        return 0

    return without_00(a - 1, b - 1) + without_00(a, b - 1)


if __name__ == "__main__":
    print(without_00(2, 2))
