import sys

sys.stdin = open('input.txt', 'r')


def color_BFS(start_node):
    queue = [start_node]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        y = a[0]
        x = a[1]
        for i in range(4):
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < matrix_size and 0 <= idx < matrix_size:
                if not visited[idy][idx]:
                    if matrix[idy][idx] == 'R' or matrix[idy][idx] == 'G':
                        visited[idy][idx] = 1
                        queue.append([idy, idx])


def B_BFS(start_node):
    queue = [start_node]
    visited_2[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        y = a[0]
        x = a[1]
        for i in range(4):
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < matrix_size and 0 <= idx < matrix_size:
                if not visited_2[idy][idx]:
                    if matrix[idy][idx] == 'B':
                        visited_2[idy][idx] = 1
                        queue.append([idy, idx])


def R_BFS(start_node):
    queue = [start_node]
    visited_3[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        y = a[0]
        x = a[1]
        for i in range(4):
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < matrix_size and 0 <= idx < matrix_size:
                if not visited_3[idy][idx]:
                    if matrix[idy][idx] == 'R':
                        visited_3[idy][idx] = 1
                        queue.append([idy, idx])


def G_BFS(start_node):
    queue = [start_node]
    visited_4[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        y = a[0]
        x = a[1]
        for i in range(4):
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < matrix_size and 0 <= idx < matrix_size:
                if not visited_4[idy][idx]:
                    if matrix[idy][idx] == 'G':
                        visited_4[idy][idx] = 1
                        queue.append([idy, idx])


matrix_size = int(input())
matrix = [list(input()) for _ in range(matrix_size)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[0]*matrix_size for _ in range(matrix_size)]
visited_2 = [[0]*matrix_size for _ in range(matrix_size)]
visited_3 = [[0]*matrix_size for _ in range(matrix_size)]
visited_4 = [[0]*matrix_size for _ in range(matrix_size)]
color_count = B_count = R_count = G_count = 0
for column in range(matrix_size):
    for row in range(matrix_size):
        if not visited[column][row]:
            if matrix[column][row] == 'R' or matrix[column][row] == 'G':
                color_BFS([column, row])
                color_count += 1
        if not visited_2[column][row]:
            if matrix[column][row] == 'B':
                B_BFS([column, row])
                B_count += 1
        if not visited_3[column][row]:
            if matrix[column][row] == 'R':
                R_BFS([column, row])
                R_count += 1
        if not visited_4[column][row]:
            if matrix[column][row] == 'G':
                G_BFS([column, row])
                G_count += 1

print(B_count + R_count + G_count, color_count + B_count)