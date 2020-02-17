import sys

sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(1000000)
def DFS(start_node):
    for j in range(4):
        y = start_node[0]
        x = start_node[1]
        idy = y + dy[j]
        idx = x + dx[j]
        if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
            if not visited[idy][idx]:
                if matrix[idy][idx] == 1:
                    visited[idy][idx] = 1
                    DFS([idy, idx])


T = int(input())
for test_case in range(1, T+1):
    matrix_row, matrix_column, cabbage_count = map(int, input().split())
    matrix = [[0]*matrix_row for _ in range(matrix_column)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(cabbage_count):
        cabbage_location = list(map(int, input().split()))
        matrix[cabbage_location[1]][cabbage_location[0]] = 1
    visited = [[0]*matrix_row for _ in range(matrix_column)]
    count = 0
    for column in range(matrix_column):
        for row in range(matrix_row):
            if matrix[column][row] == 1:
                if not visited[column][row]:
                    visited[column][row] = 1
                    count += 1
                    DFS([column, row])
    print(count)