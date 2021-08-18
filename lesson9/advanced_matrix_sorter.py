from random import randint


def sort_matrix(matrix: list) -> None:
    pass


def print_matrix(matrix: list) -> None:
    pass


if __name__ == "__main__":
    answer: str = input("Please, enter the size of matrix: ")

    if answer.isdigit():
        if int(answer) < 6:
            exit(-2)
    else:
        exit(-1)

    matrix_size: int = int(answer)

    matrix: list = [[randint(1, 50) for j in range(matrix_size)] for i in range(matrix_size)]

    sort_matrix(matrix)

    print_matrix(matrix)
