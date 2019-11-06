import sys

sys.stdin = open('input.txt', 'r')


def cctv_up(start_node):
    global count, visited
    y = start_node[0]
    x = start_node[1]
    while y >= 0:
        y = y-1
        if matrix[y][x] == 0:
            if not visited[y][x]:
                count += 1
                visited[y][x] = 1


def cctv_down(start_node):
    global count, visited
    y = start_node[0]
    x = start_node[1]
    while y < matrix_row:
        y = y+1
        if matrix[y][x] == 0:
            if not visited[y][x]:
                count += 1
                visited[y][x] = 1


def cctv_right(start_node):
    global count, visited
    y = start_node[0]
    x = start_node[1]
    while x < matrix_column:
        x = x+1
        if matrix[y][x] == 0:
            if not visited[y][x]:
                count += 1
                visited[y][x] = 1


def cctv_left(start_node):
    global count, visited
    y = start_node[0]
    x = start_node[1]
    while x >= 0:
        x = x-1
        if matrix[y][x] == 0:
            if not visited[y][x]:
                count += 1
                visited[y][x] = 1


matrix_row, matrix_column = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_row)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
one_list = [[0], [1], [2], [3]]  # 0 상 1 하 2 좌 3 우
two_list = [[0, 1], [2, 3]]
three_list = [[0, 3], [3, 1], [1, 2], [2, 0]]
four_list = [[2, 0, 3], [0, 3, 1], [3, 1, 2], [1, 2, 0]]
five_list = [[0, 1, 2, 3]]
count = 0
visited = [[0]*matrix_column for _ in range(matrix_row)]
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column]:
            if matrix[row][column] == 1:
