import sys

sys.stdin = open('input.txt', 'r')


def backtracking(start_node):


matrix_size = int(input())
matrix = [[0]*matrix_size for _ in range(matrix_size)]

for column in range(matrix_size):
    for row in range(matrix_size):
