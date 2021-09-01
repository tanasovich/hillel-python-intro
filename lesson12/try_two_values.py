def sum_or_cat(first, second):
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
