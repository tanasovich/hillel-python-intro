def is_list_has_sum_of_two(numbers: list[int], sum_of_two: int) -> bool:
    if len(numbers) == 0:
        return False

    for i in range(len(numbers)):
        for j in (index for index in range(0, len(numbers)) if index != i):  # loop through list except ith element
            if numbers[i] + numbers[j] == sum_of_two:
                return True

    return False


def map_power_lambda(numbers: list, power: int) -> None:
    powered_numbers: map = map()

    if power == '':
        powered_numbers = map(lambda x, y=2: x ** y, numbers)
    else:
        power = int(power)
        powered_numbers = map(lambda x, y=2: x ** y, numbers, [power] * len(numbers))

    print(list(powered_numbers))


def prime_numbers_range(start: int, stop: int) -> list[int]:
    for number in range(start, stop):
        if number < 2:
            continue

        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number
