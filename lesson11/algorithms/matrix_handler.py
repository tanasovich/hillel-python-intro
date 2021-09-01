def sort_matrix(matrix: list) -> None:
    find_matrix_column_sums(matrix)

    sort_matrix_columns(matrix)

    sort_column_elements(matrix)


column_sums = list()


def find_matrix_column_sums(matrix: list) -> None:
    for column in range(len(matrix)):
        column_sums.append(0)
        for row in range(len(matrix)):
            column_sums[column] += matrix[row][column]


def sort_matrix_columns(matrix):
    for i in range(len(column_sums) - 1):
        for j in range(len(column_sums) - i - 1):
            if column_sums[j] > column_sums[j + 1]:
                column_sums[j], column_sums[j + 1] = column_sums[j + 1], column_sums[j]
                for row in range(len(matrix)):
                    matrix[row][j], matrix[row][j + 1] = matrix[row][j + 1], matrix[row][j]


def sort_column_elements(matrix):
    for j in range(len(matrix)):
        for i in range(len(matrix) - 1):
            for k in range(len(matrix) - i - 1):
                if j % 2 == 0:
                    if matrix[k][j] < matrix[k + 1][j]:
                        matrix[k][j], matrix[k + 1][j] = matrix[k + 1][j], matrix[k][j]
                else:
                    if matrix[k][j] > matrix[k + 1][j]:
                        matrix[k][j], matrix[k + 1][j] = matrix[k + 1][j], matrix[k][j]


def print_matrix_with_sums(matrix: list) -> None:
    matrix.append(column_sums)
    for i in range(len(matrix)):
        for j in range(len(matrix)-1):
            print(f"{matrix[i][j] : > 4}", end='')
        print()
