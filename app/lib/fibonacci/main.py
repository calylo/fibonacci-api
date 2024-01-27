import math


def is_fibonacci_number(n):
    n_sqaured = n * n

    return (
        _is_perfect_square(5 * n_sqaured + 4)
        or _is_perfect_square(5 * n_sqaured - 4)
    )


def _is_perfect_square(number):
    sqaure_root_of_number = round(math.sqrt(number))

    return (sqaure_root_of_number * sqaure_root_of_number == number)

# algorithm for calculating nth fibonacci number
# sourced from https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/


def get_nth_number(n):
    matrix_f = [[1, 1],
         [1, 0]]
    if n == 0:
        return 0
    _nth_power_of_matrix(matrix_f, n - 1)

    return matrix_f[0][0]


def _multiply_matrix(matrix_f, matrix_m):
    x = (matrix_f[0][0] * matrix_m[0][0] +
         matrix_f[0][1] * matrix_m[1][0])
    y = (matrix_f[0][0] * matrix_m[0][1] +
         matrix_f[0][1] * matrix_m[1][1])
    z = (matrix_f[1][0] * matrix_m[0][0] +
         matrix_f[1][1] * matrix_m[1][0])
    w = (matrix_f[1][0] * matrix_m[0][1] +
         matrix_f[1][1] * matrix_m[1][1])

    matrix_f[0][0] = x
    matrix_f[0][1] = y
    matrix_f[1][0] = z
    matrix_f[1][1] = w


def _nth_power_of_matrix(matrix_f, n):
    if n == 0 or n == 1:
        return
    matrix_m = [[1, 1],
                [1, 0]]

    _nth_power_of_matrix(matrix_f, n // 2)
    _multiply_matrix(matrix_f, matrix_f)

    if n % 2 != 0:
        _multiply_matrix(matrix_f, matrix_m)
