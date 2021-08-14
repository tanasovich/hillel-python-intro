def prime_numbers_range(start: int, stop: int) -> list[int]:
    for number in range(start, stop):
        if number < 2:
            continue

        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number


if __name__ == "__main__":
    for i in prime_numbers_range(1, 100):
        print(i, end=' ')
