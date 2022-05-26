import copy
import math

eps = pow(10, -6)
k_max = 10_000


def read_from_file(filename):
    dictionary = {}
    dictionary_d = {}
    length = 0
    null_element = False
    file = open(filename, "r")
    Lines = file.readlines()
    for line in Lines:
        values = line.split(",")
        if len(values) <= 2:
            if values[0] != "\n":
                length = int(values[0])
        else:
            value, i, j = float(values[0]), int(values[1]), int(values[2])
            if j < i:
                if i in dictionary.keys():
                    dictionary[i].add((value, j))
                else:
                    dictionary[i] = {(value, j)}
            if i == j:
                if not abs(value) < eps:
                    if i in dictionary.keys():
                        dictionary[i].add((value, j))
                    else:
                        dictionary[i] = {(value, j)}
                    dictionary_d[i] = value
                else:
                    null_element = True

    return dictionary, dictionary_d, length, null_element


def read_from_file_vector(filename):
    vector = {}
    counter = 0
    file = open(filename, "r")
    Lines = file.readlines()
    for line in Lines:
        if line != "\n":
            vector[counter] = float(line.rstrip())
            counter += 1
    return vector


def compute_new_x(a, b, diagonal, x_p, data_size):
    x_c = {}
    sum_4 = {}
    for i in range(data_size):
        first_sum = 0
        for value, j in a[i]:
            if j < i:
                first_sum += value * x_p[j]
                if j not in x_c.keys():
                    x_c[j] = value * x_p[i]
                else:
                    x_c[j] = x_c[j] + value * x_p[i]
        sum_4[i] = first_sum

    for i in range(data_size):
        if i in x_c.keys():
            x_c[i] = (b[i] - sum_4[i] - x_c[i]) / diagonal[i]
        else:
            x_c[i] = (b[i] - sum_4[i]) / diagonal[i]
    return x_c


def norm(x_c, x_p):
    sum_values = 0
    for i in x_c.keys():
        sum_values += pow(x_c[i] - x_p[i], 2)
    return math.sqrt(sum_values)


def solve_system(a, b, diagonal, data_size):
    x_c = {i: 0 for i in range(0, data_size)}  # x (k+1)
    x_p = {i: 0 for i in range(0, data_size)}  # x (k)
    k = 0
    while True:
        x_p = copy.deepcopy(x_c)
        x_c = compute_new_x(a, b, diagonal, x_p, data_size)
        delta = norm(x_c, x_p)
        k += 1
        if delta < eps or delta > (10 ** 8) or k > k_max:
            break
    if delta < eps:
        x_star = x_c
        return x_star, k
    print("norm: ", delta)
    return False, False


# a1, diagonal_a1, n1, null_n1 = read_from_file("a_1.txt")
# b1 = read_from_file_vector("b_1.txt")
# x1, iterations1 = solve_system(a1, b1, diagonal_a1, n1)
# sorted(x1)
# # print(x1)
# print("Iterations for a_1, b_1: ", iterations1)

# a2, diagonal_a2, n2, null_n2 = read_from_file("a_2.txt")
# b2 = read_from_file_vector("b_2.txt")
# x2, iterations2 = solve_system(a2, b2, diagonal_a2, n2)
# sorted(x2)
# print(x2)
# print("Iterations for a_2, b_2: ", iterations2)

# a3, diagonal_a3, n3, null_n3 = read_from_file("a_3.txt")
# b3 = read_from_file_vector("b_3.txt")
# x3, iterations3 = solve_system(a3, b3, diagonal_a3, n3)
# sorted(x3)
# # print(x3)
# print("Iterations for a_3, b_3: ", iterations3)
#
# a4, diagonal_a4, n4, null_n4 = read_from_file("a_4.txt")
# b4 = read_from_file_vector("b_4.txt")
# x4, iterations4 = solve_system(a4, b4, diagonal_a4, n4)
# sorted(x4)
# # print(x4)
# print("Iterations for a_4, b_4: ", iterations4)
#
a5, diagonal_a5, n5, null_n5 = read_from_file("a_5.txt")
b5 = read_from_file_vector("b_5.txt")
x5, iterations5 = solve_system(a5, b5, diagonal_a5, n5)
if not x5:
    print("Divergence")
