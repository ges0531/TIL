import sys

sys.stdin = open('input.txt', 'r')


def DFS(start_node):
    stack = [start_node]
    visited = [[0]*matrix_row for _ in range(matrix_column)]
    visited[start_node[0]][start_node[1]] = 1
    while stack:
        a = stack.pop()
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                if visited[idy][idx] == 0:
                    if matrix[idy][idx] == 0:
                        visited[idy][idx] = 1
                        stack.append([y, x])
                        stack.append([idy, idx])
    for j in visited:
        print(j)







matrix_column, matrix_row = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
DFS([0, 0])