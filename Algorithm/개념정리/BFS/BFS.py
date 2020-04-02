import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    queue = [start_node]
    visited = [[0]*matrix_row for _ in range(matrix_column)]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                if visited[idy][idx] == 0:
                    if matrix[idy][idx] == 0:
                        visited[idy][idx] = visited[y][x] + 1
                        matrix[idy][idx] = 2
                        queue.append([idy, idx])
    for j in visited:
        print(j)
    print(1)
    for k in matrix:
        print(k)


matrix_column, matrix_row = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
BFS([0, 0])