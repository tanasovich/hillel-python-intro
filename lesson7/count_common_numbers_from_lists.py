first_list: list = list(map(int, input("Enter numbers separated by space for the first list: ").split()))

second_list: list = list(map(int, input("Enter numbers separated by space for the second list: ").split()))

print(len(set(first_list) & set(second_list)))
