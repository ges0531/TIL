import sys

sys.stdin = open('input.txt', 'r')


def water_change(water_location):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    y = water_location[0]
    x = water_location[1]
    for i in range(4):
        idy = y + dy[i]
        idx = x + dx[i]
        if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
            if not water_visited[idy][idx]:
                if not (matrix[idy][idx] == 'X' or matrix[idy][idx] == 'D' or matrix[idy][idx] == 'S'):
                    matrix[idy][idx] = '*'
                    water.append([idy, idx])


def hedgehog_change(hedgehog_location):
    global flag
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    y = hedgehog_location[0]
    x = hedgehog_location[1]
    for i in range(4):
        idy = y + dy[i]
        idx = x + dx[i]
        if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
            if not hedgehog_visited[idy][idx]:
                if matrix[idy][idx] == 'D':
                    matrix[idy][idx] = 'S'
                    break
                elif not (matrix[idy][idx] == 'X' or matrix[idy][idx] == '*'):
                    matrix[y][x] = '.'
                    matrix[idy][idx] = 'S'
                    hedgehog.append([idy, idx])
                    break
    else:
        flag = 1


matrix_column, matrix_row = map(int, input().split())
matrix = [list(input()) for _ in range(matrix_column)]
water_visited = [[0] * matrix_row for _ in range(matrix_column)]
hedgehog_visited = [[0] * matrix_row for _ in range(matrix_column)]
D_location = []
water = []
hedgehog = []
count = 0
flag = 0
for column in range(len(matrix)):
    for row in range(len(matrix[column])):
        if matrix[column][row] == 'D':
            D_location = [column, row]
        elif matrix[column][row] == '*':
            water.append([column, row])
            water_visited[column][row] = 1
        elif matrix[column][row] == 'S':
            hedgehog.append([column, row])
            hedgehog_visited[column][row] = 1
while matrix[D_location[0]][D_location[1]] == 'D':
    for w in range(len(water)):
        water_change(water[w])
    for h in range(len(hedgehog)):
        hedgehog_change(hedgehog[h])
    count += 1
    if flag:
        break
    for v in matrix:
        print(v)
    print()
if flag:
    print('KAKTUS')
else:
    print(count)
