import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    visited[start_node[0]][start_node[1]] = 1
    queue = [start_node]
    count = 1
    while queue:
        a = queue.pop(0)
        y = a[0]
        x = a[1]
        for k in range(4):
            idy = y + dy[k]
            idx = x + dx[k]
            if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                if not visited[idy][idx]:
                    if not matrix[idy][idx]:
                        visited[idy][idx] = 1
                        queue.append([idy, idx])
                        count += 1
    return count


matrix_column, matrix_row, rect_count = map(int, input().split())
matrix = [[0]*matrix_row for _ in range(matrix_column)]
rect_list = [list(map(int, input().split())) for _ in range(rect_count)]
visited = [[0]*matrix_row for _ in range(matrix_column)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
my_list = []
flag_count = 0
for re in range(rect_count):
    for column in range(rect_list[re][1], rect_list[re][3]):
        for row in range(rect_list[re][0], rect_list[re][2]):
            matrix[column][row] = 1
for i in range(matrix_column):
    for j in range(matrix_row):
        if not visited[i][j] and not matrix[i][j]:
            flag_count += 1
            my_list.append(BFS([i, j]))
my_list.sort()
print(flag_count)
print(' '.join(map(str, my_list)))
