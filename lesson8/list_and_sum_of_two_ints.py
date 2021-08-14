def is_list_has_sum_of_two(numbers: list[int], sum_of_two: int) -> bool:
    if len(numbers) == 0:
        return False

    for i in range(len(numbers)):
        for j in (index for index in range(0, len(numbers)) if index != i):  # loop through list except ith element
            if numbers[i] + numbers[j] == sum_of_two:
                return True

    return False


if __name__ == "__main__":
    print(is_list_has_sum_of_two([1, 2, 3, 4, 5], 7))
    print(is_list_has_sum_of_two([1, 2, 3, 4, 5], 3))
    print(is_list_has_sum_of_two([1, 2, 3, 4, 5], 9))
    print(is_list_has_sum_of_two([1, 2, 3, 4, 5], 10))
    print(is_list_has_sum_of_two([], 3))
