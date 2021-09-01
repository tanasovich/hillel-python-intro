"""
Advanced matrix sorter
Module exposes sort_matrix and print_matrix functions which make column
sorting and print matrix in beautiful way.
"""

__all__ = ["sort_matrix", "print_matrix_with_sums"]


def sort_matrix(matrix: list) -> None:
    """
    Sort matrix columns by column sums (ascending)
    Each column sorted asc/desc depending on index parity.

    :param matrix: matrix to be sorted
    :return: None
    """
    _find_matrix_column_sums(matrix)

    _sort_matrix_columns(matrix)

    _sort_column_elements(matrix)


_column_sums = list()


def _find_matrix_column_sums(matrix: list) -> None:
    """
    Find column sums in matrix and store in internal module var.

    :param matrix: matrix
    :return: None
    """
    for column in range(len(matrix)):
        _column_sums.append(0)
        for row in range(len(matrix)):
            _column_sums[column] += matrix[row][column]


def _sort_matrix_columns(matrix):
    """
    Matrix columns ascending sorting by column sums.

    :param matrix: matrix
    :return: None
    """
    for i in range(len(_column_sums) - 1):
        for j in range(len(_column_sums) - i - 1):
            if _column_sums[j] > _column_sums[j + 1]:
                _column_sums[j], _column_sums[j + 1] = _column_sums[j + 1], _column_sums[j]
                for row in range(len(matrix)):
                    matrix[row][j], matrix[row][j + 1] = matrix[row][j + 1], matrix[row][j]


def _sort_column_elements(matrix):
    """
    Sort each column in matrix
    odd column - descending sorting
    even column - ascending sorting

    :param matrix: matrix
    :return: None
    """
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
    """
    Print matrix with column sums.
    Align matrix elements in stdout.

    :param matrix: matrix
    :return: None
    """
    matrix.append(_column_sums)
    for i in range(len(matrix)):
        for j in range(len(matrix)-1):
            print(f"{matrix[i][j] : > 4}", end='')
        print()
    matrix.pop()
