import sys

sys.stdin = open('input.txt', 'r')

def iswall(x, y):
    return 0 <= x < matrix_row and 0 <= y < matrix_column

dxdy = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]

matrix_row, matrix_column, shark_count = map(int, input().split())
shark_list = [list(map(int, input().split())) for _ in range(shark_count)]
for minus in range(len(shark_list)):
    shark_list[minus][0] -= 1
    shark_list[minus][1] -= 1
result = 0
column = -1
flag_count = [0]*len(shark_list)
for time in range(matrix_column):
    visited = [0] * len(shark_list)
    row = 0
    column += 1
    for _ in range(matrix_row):
        flag = 0
        for i in range(len(shark_list)):
            if row == shark_list[i][0] and column == shark_list[i][1]:
                result += shark_list[i][4]
                flag = 1
                shark_list.pop(i)
                break
        row += 1
        if flag:
            break
    for j in range(len(shark_list)-1, -1, -1):
        dx, dy = dxdy[shark_list[j][3]]
        kx, ky = shark_list[j][0], shark_list[j][1]
        if flag_count[j] % 2:
            dx, dy = -dx, -dy
        for _ in range(shark_list[j][2]):
            nx, ny = kx + dx, ky + dy
            if iswall(nx, ny):
                kx, ky = nx, ny
            else:
                dx, dy = -dx, -dy
                kx, ky = kx + dx, ky + dy
                flag_count[j] += 1
        shark_list[j][0], shark_list[j][1] = kx, ky
        visited[j] = 1
        for shark in range(len(shark_list)-1, -1, -1):
            if visited[shark] and j != shark:
                if shark_list[j][0] == shark_list[shark][0] and shark_list[j][1] == shark_list[shark][1]:
                    if shark_list[j][4] > shark_list[shark][4]:
                        shark_list.pop(shark)
                    else:
                        shark_list.pop(j)

print(result)
