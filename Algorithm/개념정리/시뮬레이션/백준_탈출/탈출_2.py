import sys

sys.stdin = open('input.txt', 'r')


def hedgehog_change(hedgehog_location, count, virtual_matrix, water_location, visited):
    global my_min
    for v in visited:
        print(v)
    print()
    y = hedgehog_location[0]
    x = hedgehog_location[1]
    if virtual_matrix[y][x] == 'D':
        if my_min > count:
            my_min = count
        return
    copy_matrix = [[0]*matrix_row for _ in range(matrix_column)]
    for copy_1 in range(len(virtual_matrix)):
        for copy_2 in range(len(virtual_matrix[copy_1])):
            copy_matrix[copy_1][copy_2] = virtual_matrix[copy_1][copy_2]
    water_list = []
    for w in range(len(water_location)):
        for j in range(4):
            water_y = water_location[w][0]
            water_x = water_location[w][1]
            water_idy = water_y + dy[j]
            water_idx = water_x + dx[j]
            if 0 <= water_idy < matrix_column and 0 <= water_idx < matrix_row:
                if copy_matrix[water_idy][water_idx] == '.':
                    copy_matrix[water_idy][water_idx] = '*'
                    water_list.append([water_idy, water_idx])

    for i in range(4):
        idy = y+dy[i]
        idx = x+dx[i]
        if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
            if not visited[idy][idx]:
                if copy_matrix[idy][idx] == '.' or copy_matrix[idy][idx] == 'D':
                    visited[y][x] = 1
                    hedgehog_change([idy, idx], count+1, copy_matrix, water_list, visited)
                    visited[y][x] = 0

matrix_column, matrix_row = map(int, input().split())
matrix = [list(input()) for _ in range(matrix_column)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
my_min = 100000000
water = []
S_location = []
flag = 0
for column in range(len(matrix)):
    for row in range(len(matrix[column])):
        if matrix[column][row] == 'S':
            S_location = [column, row]
        elif matrix[column][row] == '*':
            water.append([column, row])
hedgehog_change(S_location, 0, matrix, water, [[0]*matrix_row for _ in range(matrix_column)])
if my_min == 100000000:
    print('KAKTUS')
else:
    print(my_min)
