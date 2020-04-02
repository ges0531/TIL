import sys

sys.stdin = open('input.txt', 'r')


def DFS(start_node, count):
    global my_max
    my_max = max(my_max, count)
    for i in range(4):
        idy = start_node[0] + dy[i]
        idx = start_node[1] + dx[i]
        if 0 <= idy < matrix_column and 0 <= idx < matrix_row and matrix[idy][idx] not in visited_en:
            visited_en.append(matrix[idy][idx])
            DFS([idy, idx], count+1)
            visited_en.remove(matrix[idy][idx])


matrix_column, matrix_row = map(int, input().split())
matrix = [list(input()) for _ in range(matrix_column)]
visited_en = [matrix[0][0]]
my_max = 0
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
DFS([0, 0], 1)
print(my_max)