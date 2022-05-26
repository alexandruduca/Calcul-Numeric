import math
import random
import copy
import numpy as np

n = 100
eps = 10 ** (-12)


def search_pivot(A, l):
    max_value = -9999
    index = l
    for i in range(l, n):
        value = abs(A[i][l])
        if value > max_value:
            max_value = value
            index = i
    return max_value, index


def swap_lines(A, b, l, index):
    A[l], A[index] = A[index], A[l]
    b[l], b[index] = b[index], b[l]
    return A, b


def solve_upper_triangular_system(A, b):
    x = [0] * n
    for i in reversed(range(0, n)):
        sum_products_line = 0
        for j in range(i + 1, n):
            sum_products_line += A[i][j] * x[j]
        x[i] = (b[i] - sum_products_line) / A[i][i]
    return x


def verify_solution(A_init, x_gauss, b_init):
    multiplication = []
    for i in range(0, n):
        sum_products_line = 0
        line = A_init[i]
        for j in range(0, n):
            sum_products_line = sum_products_line + line[j] * x_gauss[j]
        multiplication.append(sum_products_line)
    diff = []
    for i in range(0, n):
        difference = multiplication[i] - b_init[i]
        diff.append(difference)
    euclidean = 0
    for i in range(0, n):
        euclidean += diff[i] ** 2
    euclidean = math.sqrt(euclidean)
    return euclidean


def gauss_elimination(A, b):
    A_copy = copy.deepcopy(A)
    b_copy = copy.deepcopy(b)
    l = 0
    pivot, index = search_pivot(A, l)
    A, b = swap_lines(A, b, l, index)
    while l < n - 1 and abs(pivot) > eps:
        for i in range(l + 1, n):
            f = A[i][l] / pivot
            for j in range(l + 1, n):
                A[i][j] = A[i][j] - f * A[l][j]
            b[i] = b[i] - f * b[l]
            A[i][l] = 0
        l += 1
        pivot, index = search_pivot(A, l)
        A, b = swap_lines(A, b, l, index)
    if abs(pivot) <= eps:
        print("singular matrix")
    else:
        x_gauss = solve_upper_triangular_system(A, b)
        solution = verify_solution(A_copy, x_gauss, b_copy)
        return x_gauss, solution, A


def inverse_matrix(A):
    I_n = []
    for i in range(0, n):
        line = []
        for j in range(0, n):
            if i == j:
                line.append(1)
            else:
                line.append(0)
        I_n.append(line)
    for i in range(0, n):
        A[i] = A[i] + I_n[i]
    b = [0] * n
    _, _, R_b_transformed = gauss_elimination(A, b)
    b_gauss = []
    for i in range(0, n):
        b_gauss.append(R_b_transformed[i][n:])
    A_gauss = []
    for i in range(0, n):
        A_gauss.append(R_b_transformed[i][:n])
    A_inverse = []
    for j in range(0, n):
        A_inverse.append(solve_upper_triangular_system(A_gauss, [b_gauss[i][j] for i in range(0, n)]))
    A_aux = copy.deepcopy(A_inverse)
    A_inverse = []
    for j in range(0, n):
        line = []
        for i in range(0, n):
            line.append(A_aux[i][j])
        A_inverse.append(line)
    return A_inverse


def library(A_init, x_gauss, b_init):
    x_lib = np.linalg.solve(A_init, b_init)
    euclid_1 = np.array(x_gauss) - x_lib
    euclid_1 = np.linalg.norm(euclid_1, 2)

    A_inv = np.linalg.inv(A_init)
    multiplication = np.matmul(A_inv, b_init)
    multiplication = np.array(multiplication)
    euclid_2 = np.array(x_gauss) - multiplication
    euclid_2 = np.linalg.norm(euclid_2, 2)

    return euclid_1, euclid_2


def random_input(n):
    A = []
    for i in range(0, n):
        line = []
        for j in range(0, n):
            line.append(random.randint(0, 10))
        A.append(line)
    b = [0] * n
    for i in range(0, n):
        b[i] = random.randint(0, 10)
    return A, b


A, b = random_input(n)
# A = [[2, 0, 1], [0, 2, 1], [4, 4, 6]]
# b = [5, 1, 14]
print("Initial matrix: ", A)
x_gauss, solution, matrix = gauss_elimination(A, b)
print("x gauss: ", x_gauss)
print("||A_init * x_gauss - b_init||: ", solution)
euclid_1, euclid_2 = library(A, x_gauss, b)
print("||x_gauss - x_lib|| = ", euclid_1)
print("||x_gauss - A_inv * b_init|| = ", euclid_2)

inverse_A = inverse_matrix(copy.deepcopy(A))
A_inv_bibl = np.linalg.inv(copy.deepcopy(A))
euclid_3 = np.linalg.norm(np.array(inverse_A) - np.array(A_inv_bibl))
print("||A_inv_gauss - A_inv_bibl||: ", euclid_3)
