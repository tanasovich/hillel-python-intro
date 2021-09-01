"""
Numeric sequences processing functions
List checker, number powering and generators.
"""


def is_list_has_sum_of_two(numbers: list[int], sum_of_two: int) -> bool:
    """
    Accepts numeric list and finds pair, sum them equals to sum_of_two

    :param numbers: numeric list to be checked.
    :param sum_of_two: sum, which has to be found.
    :return: True if list has pair, False otherwise.
    """
    if len(numbers) == 0:
        return False

    for i in range(len(numbers)):
        for j in (index for index in range(0, len(numbers)) if index != i):  # loop through list except ith element
            if numbers[i] + numbers[j] == sum_of_two:
                return True

    return False


def map_power_lambda(numbers: list, power: int) -> None:
    """
    Accepts numeric list and power. Prints list with powered elements

    :param numbers: numeric list
    :param power: power
    :return: None
    """
    if power == '':
        powered_numbers = map(lambda x, y=2: x ** y, numbers)
    else:
        power = int(power)
        powered_numbers = map(lambda x, y=2: x ** y, numbers, [power] * len(numbers))

    print(list(powered_numbers))


def prime_numbers_range(start: int, stop: int) -> list[int]:
    """
    Generates prime numbers in [start, stop) range.

    :param start: left margin of range (included)
    :param stop: right margin of range (excluded)
    :return: yields prime numbers
    """
    for number in range(start, stop):
        if number < 2:
            continue

        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number
