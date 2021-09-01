from random import randint

from sequences import *
from algorithms import matrix_handler
from algorithms import functions

if __name__ == "__main__":
    print(reverse_it(1234))
    print(count_first(None, 12))

    matrix: list = [[randint(1, 50) for j in range(10)] for i in range(10)]
    matrix_handler.sort_matrix(matrix)
    matrix_handler.print_matrix_with_sums(matrix)

    for i in functions.prime_numbers_range(1, 16):
        print(i, end=' ')
