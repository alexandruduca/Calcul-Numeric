import time

def read_from_file(filename):
    dictionary = {}
    length = 0
    file = open(filename, "r")
    Lines = file.readlines()
    for line in Lines:
        values = line.split(",")
        if len(values) <= 2:
            if values[0] != "\n":
                length = int(values[0])
        else:
            value, i, j = float(values[0]), int(values[1]), int(values[2])
            if j <= i:
                if i in dictionary.keys():
                    dictionary[i].add((value, j))
                else:
                    dictionary[i] = {(value, j)}
                if j in dictionary.keys():
                    dictionary[j].add((value, i))
                else:
                    dictionary[j] = {(value, i)}
    return dictionary, length


def read_from_file_transpose(filename):
    dictionary = {}
    length = 0
    file = open(filename, "r")
    Lines = file.readlines()
    for line in Lines:
        values = line.split(",")
        if len(values) <= 2:
            if values[0] != "\n":
                length = int(values[0])
        else:
            value, j, i = float(values[0]), int(values[1]), int(values[2])
            if i <= j:
                if i in dictionary.keys():
                    dictionary[i].add((value, j))
                else:
                    dictionary[i] = {(value, j)}
                if j in dictionary.keys():
                    dictionary[j].add((value, i))
                else:
                    dictionary[j] = {(value, i)}
    return dictionary, length


def sum_result(a, b, n):
    sum_function = {}
    for i in range(0, n):
        if i in a.keys() and i not in b.keys():
            sum_function[i] = a[i]
        elif i not in a.keys() and i in b.keys():
            sum_function[i] = b[i]
        else:
            a_values = {j: value for value, j in a[i]}
            b_values = {j: value for value, j in b[i]}
            for key in a_values.keys():
                if key in b_values.keys():
                    sum_values = a_values[key] + b_values[key]
                    if i not in sum_function.keys():
                        sum_function[i] = {(sum_values, key)}
                    else:
                        sum_function[i].add((sum_values, key))
                else:
                    if i not in sum_function.keys():
                        sum_function[i] = {(a_values[key], key)}
                    else:
                        sum_function[i].add((a_values[key], key))
            for key in b_values.keys():
                if key not in a_values.keys():
                    if i not in sum_function.keys():
                        sum_function[i] = {(b_values[key], key)}
                    else:
                        sum_function[i].add((b_values[key], key))
    return sum_function


def product_result(a, a_transpose, n):
    product_function = {}
    for i in range(0, n):
        for j in range(0, n):
            sum_values = 0
            if i in a.keys() and i in a_transpose.keys():
                a_values = {k: value for value, k in a[i]}
                a_transpose_values = {k: value for value, k in a_transpose[j]}
                for key in a_values:
                    if key in a_transpose_values:
                        sum_values += a_values[key] * a_transpose_values[key]
                if sum_values:
                    if i in product_function:
                        product_function[i].add((sum_values, j))
                    else:
                        product_function[i] = {(sum_values, j)}
    return product_function


a, n = read_from_file("a.txt")
b, _ = read_from_file("b.txt")
a_plus_b, _ = read_from_file("a_plus_b.txt")
a_ori_a, _ = read_from_file("a_ori_a.txt")

sum_a_b = sum_result(a, b, n)
print("Comparatie suma: ", sum_a_b == a_plus_b)

start_time = time.time()

a_transpose, _ = read_from_file_transpose("a.txt")
product_a_b = product_result(a, a_transpose, n)
print("Comparatie produs: ", product_a_b == a_ori_a)

print("Timp executie produs: %s secunde." % "{:.2f}".format(round((time.time() - start_time), 2)))

