import sys

sys.stdin = open('input.txt', 'r')

matrix_row, matrix_column = map(int, input().split())
print(matrix_row, matrix_column)