#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_len = len(row)
        for col in range(row_len):
            if col != row_len - 1:
                print("{:d}".format(row[col]), end=' ')
            else:
                print("{:d}".format(row[col]), end='')
            print(end=' ')
