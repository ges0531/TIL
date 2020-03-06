import sys

sys.stdin = open('input.txt', 'r')


def color_DFS(start_node):
    y = start_node[0]
    x = start_node[1]
    visited_2[start_node[0]][start_node[1]] = 1
    for i in range(4):
        idy = y + dy[i]
        idx = x + dx[i]
        if 0 <= idy < matrix_size and 0 <= idx < matrix_size:
            if not visited[idy][idx]:
                if not matrix[idy][idx] == 'B':
                    visited[idy][idx] = 1
                    color_DFS([idy, idx])
                    visited[idy][idx] = 0


def R_DFS(start_node):
    y = start_node[0]
    x = start_node[1]
    visited_3[start_node[0]][start_node[1]] = 1
    for i in range(4):
        idy = y + dy[i]
        idx = x + dx[i]
        if 0 <= idy < matrix_size and 0 <= idx < matrix_size:
            if not visited[idy][idx]:
                if matrix[idy][idx] == 'R':
                    visited[idy][idx] = 1
                    R_DFS([idy, idx])
                    visited[idy][idx] = 0


def B_DFS(start_node):
    y = start_node[0]
    x = start_node[1]
    visited_4[start_node[0]][start_node[1]] = 1
    for i in range(4):
        idy = y + dy[i]
        idx = x + dx[i]
        if 0 <= idy < matrix_size and 0 <= idx < matrix_size:
            if not visited[idy][idx]:
                if matrix[idy][idx] == 'B':
                    visited[idy][idx] = 1
                    B_DFS([idy, idx])
                    visited[idy][idx] = 0


def G_DFS(start_node):
    y = start_node[0]
    x = start_node[1]
    visited_5[start_node[0]][start_node[1]] = 1
    for i in range(4):
        idy = y + dy[i]
        idx = x + dx[i]
        if 0 <= idy < matrix_size and 0 <= idx < matrix_size:
            if not visited[idy][idx]:
                if matrix[idy][idx] == 'G':
                    visited[idy][idx] = 1
                    G_DFS([idy, idx])
                    visited[idy][idx] = 0


matrix_size = int(input())
matrix = [list(input()) for _ in range(matrix_size)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
visited = [[0]*matrix_size for _ in range(matrix_size)]
visited_2 = [[0]*matrix_size for _ in range(matrix_size)]
visited_3 = [[0]*matrix_size for _ in range(matrix_size)]
visited_4 = [[0]*matrix_size for _ in range(matrix_size)]
visited_5 = [[0]*matrix_size for _ in range(matrix_size)]
color_count = 0
R_count = 0
B_count = 0
G_count = 0
for column in range(matrix_size):
    for row in range(matrix_size):
        if not matrix[column][row] == 'B' and not visited_2[column][row]:
            color_count += 1
            visited[column][row] = 1
            color_DFS([column, row])
            visited[column][row] = 0
        if matrix[column][row] == 'R' and not visited_3[column][row]:
            R_count += 1
            visited[column][row] = 1
            R_DFS([column, row])
            visited[column][row] = 0
        if matrix[column][row] == 'B' and not visited_4[column][row]:
            B_count += 1
            visited[column][row] = 1
            B_DFS([column, row])
            visited[column][row] = 0
        if matrix[column][row] == 'G' and not visited_5[column][row]:
            G_count += 1
            visited[column][row] = 1
            G_DFS([column, row])
            visited[column][row] = 0

print(R_count+B_count+G_count, color_count+B_count)
