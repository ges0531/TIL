import sys

sys.stdin = open('input.txt', 'r')


def DFS(start_node):
    if start_node not in flag_list:
        flag_list.append(start_node)
    y = start_node[0]
    x = start_node[1]
    visited_2[y][x] = 1
    for k in range(4):
        idy = y + dy[k]
        idx = x + dx[k]
        if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
            if not visited[idy][idx]:
                if not matrix[idy][idx]:
                    visited[idy][idx] = 1
                    DFS([idy, idx])
                    visited[idy][idx] = 0


matrix_column, matrix_row, rect_count = map(int, input().split())
matrix = [[0]*matrix_row for _ in range(matrix_column)]
rect_list = [list(map(int, input().split())) for _ in range(rect_count)]
visited = [[0]*matrix_row for _ in range(matrix_column)]
visited_2 = [[0]*matrix_row for _ in range(matrix_column)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
my_list = []
for re in range(rect_count):
    for column in range(rect_list[re][1], rect_list[re][3]):
        for row in range(rect_list[re][0], rect_list[re][2]):
            matrix[column][row] = 1
for i in range(matrix_column):
    for j in range(matrix_row):
        if not visited_2[i][j] and not matrix[i][j]:
            flag_list = []
            visited[i][j] = 1
            DFS([i, j])
            my_list.append(len(flag_list))
my_list.sort()
print(' '.join(map(str, my_list)))
