from random import randint


def sort_matrix(matrix: list, column_sums: list) -> None:
    pass


def print_matrix_with_sums(matrix: list, column_sums: list) -> None:
    matrix.append(column_sums)
    for i in range(len(matrix)):
        for j in range(len(matrix)-1):
            print(f"{matrix[i][j] : > 4}", end='')
        print()


if __name__ == "__main__":
    answer: str = input("Please, enter the size of matrix: ")

    if answer.isdigit():
        if int(answer) < 6:
            exit(-2)
    else:
        exit(-1)

    matrix_size: int = int(answer)

    matrix: list = [[randint(1, 50) for j in range(matrix_size)] for i in range(matrix_size)]

    column_sums: list = [0 for i in range(matrix_size)]
    for column in range(matrix_size):
        for row in range(matrix_size):
            column_sums[column] += matrix[row][column]

    sort_matrix(matrix, column_sums)

    print_matrix_with_sums(matrix, column_sums)
