import sys
from collections import deque

sys.stdin = open('input.txt', 'r')


def BFS(start_list):
    global result
    visited = [[0]*matrix_row for _ in range(matrix_column)]
    queue = deque()
    for i in range(len(start_list)):
        queue.append(start_list[i])
        visited[start_list[i][0]][start_list[i][1]] = 1
    while queue:
        a = queue.popleft()
        for j in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[j]
            idx = x+dx[j]
            if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                if not visited[idy][idx]:
                    if tomato_matrix[idy][idx] == 0:
                        tomato_matrix[idy][idx] = 1
                        visited[idy][idx] = visited[y][x]+1
                        queue.append([idy, idx])
                        result = visited[idy][idx]

matrix_row, matrix_column = map(int, input().split())
tomato_matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
tomato_list = []
result = 0
a = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for column in range(len(tomato_matrix)):
    for row in range(len(tomato_matrix[column])):
        if tomato_matrix[column][row] == 1:
            tomato_list.append([column, row])
BFS(tomato_list)
for column_2 in range(len(tomato_matrix)):
    if a == 0:
        break
    for row_2 in range(len(tomato_matrix[column_2])):
        if tomato_matrix[column_2][row_2] == 0:
            a = 0
            break
if a:
    if result:
        print(result-1)
    else:
        print(0)
else:
    print(-1)