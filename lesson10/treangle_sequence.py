def count_first(nums, n: int) -> list:
    def a(k: int) -> int:
        if k == 1:
            return 1
        return a(k - a(k - 1)) + 1

    sequence = list()

    for i in range(1, n + 1):
        sequence.append(a(i))

    return sequence


if __name__ == "__main__":
    print(count_first(None, 2))
    print(count_first(None, 5))
    print(count_first(None, 10))
