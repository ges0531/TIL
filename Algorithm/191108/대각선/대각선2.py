import sys

sys.stdin = open('input.txt', 'r')


matrix_column, matrix_row = map(int, input().split())
if matrix_column == 1 or matrix_row == 1:
    print(matrix_row*matrix_column)
else:
    if matrix_column > matrix_row:
        if matrix_column % matrix_row:
            print(((matrix_column//matrix_row) + 1)*matrix_row)
        else:
            print(matrix_column)
    elif matrix_column == matrix_row:
        print(matrix_column)
    else:
        if matrix_row % matrix_column:
            print(((matrix_row//matrix_column)+1) * matrix_column)
        else:
            print(matrix_row)