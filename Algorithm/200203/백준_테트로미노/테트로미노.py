import sys

sys.stdin = open('input.txt','r')


def search_max(start_node, count):
    for i in range(4):

matrix_column, matrix_row = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]