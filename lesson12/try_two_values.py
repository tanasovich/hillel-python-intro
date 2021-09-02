def sum_or_cat():
    """
    Accepts two values from the stdin.
    Returns sum of them if both are numbers.
    Returns concatenation if some of them are non-numeric value.

    :return: sum or concatenation
    """
    first, second = input("Please, enter two values: ").split()

    try:
        x = float(first)
        y = float(second)
        return x + y
    except ValueError:
        return str(first) + str(second)


if __name__ == "__main__":
    print(sum_or_cat())
