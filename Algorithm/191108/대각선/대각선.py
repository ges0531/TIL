import sys

sys.stdin = open('input.txt', 'r')


def great(n1, n2):
    for i in range(n1, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i


matrix_column, matrix_row = map(int, input().split())
if matrix_column > matrix_row:
    result = (matrix_column//matrix_row) + 1
elif matrix_column == matrix_row:
    result = 1
else:
    result = (matrix_row//matrix_column)+1


matrix_row_small = matrix_row//great(matrix_row, matrix_column)
matrix_column_small = matrix_column//great(matrix_row, matrix_column)
count = 0
if matrix_column > matrix_row:
    for ii in range(matrix_row_small):
        for j in range(result):
            count += 1
else:
    for ii in range(matrix_column_small):
        for j in range(result):
            count += 1

print(count*great(matrix_row, matrix_column))
