from random import randint


column_sums = list()


def sort_matrix(matrix: list) -> None:
    for i in range(len(column_sums)-1):
        for j in range(len(column_sums)-i-1):
            if column_sums[j] > column_sums[j + 1]:
                column_sums[j], column_sums[j + 1] = column_sums[j + 1], column_sums[j]
                for row in range(len(matrix)):
                    matrix[row][j], matrix[row][j + 1] = matrix[row][j + 1], matrix[row][j]

    for j in range(len(matrix)):
        for i in range(len(matrix)-1):
            for k in range(len(matrix)-i-1):
                if j % 2 == 0:
                    if matrix[k][j] < matrix[k + 1][j]:
                        matrix[k][j], matrix[k + 1][j] = matrix[k + 1][j], matrix[k][j]
                else:
                    if matrix[k][j] > matrix[k + 1][j]:
                        matrix[k][j], matrix[k + 1][j] = matrix[k + 1][j], matrix[k][j]


def print_matrix_with_sums(matrix: list) -> None:
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

    for column in range(matrix_size):
        column_sums.append(0)
        for row in range(matrix_size):
            column_sums[column] += matrix[row][column]

    matrix.append(column_sums)
    print("До сортировки:")
    print_matrix_with_sums(matrix)
    matrix.pop()

    sort_matrix(matrix)

    matrix.append(column_sums)
    print("\nПосле сортировки")
    print_matrix_with_sums(matrix)
    matrix.pop()
