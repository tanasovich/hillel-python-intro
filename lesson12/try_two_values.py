def sum_or_cat(first, second):
    """
    Accepts two values.
    Returns sum of them if both are numbers.
    Returns concatenation if some of them are non-numeric value.

    :param first: first value
    :param second: second value
    :return: sum or concatenation
    """
    try:
        x = float(first)
        y = float(second)
        return x + y
    except ValueError:
        return str(first) + str(second)


if __name__ == "__main__":
    print(sum_or_cat(2, 2))
    print(sum_or_cat('string', 2))
    print(sum_or_cat('string', 'string'))
