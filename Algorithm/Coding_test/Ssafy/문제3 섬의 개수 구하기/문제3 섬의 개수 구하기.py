import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

def DSFr(v):
    visited[v] = True
    v = 0
for test_case in range(1, T+1):
    size = int(input())
    visited = [0] * size
    matrix = [0] * size
    for s in range(size):
        col = list(map(int, input().split()))
        matrix[s] = col
    for column in range(matrix):
        for row in range(matrix[0]):
            if matrix[column][row] != 0:
                DSFr(1)