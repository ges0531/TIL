import sys

sys.stdin = open('input.txt', 'r')


def iswall(x, y):
    return 0 <= x < matrix_row and 0 <= y < matrix_column


def catch(column):
    global result
    for row in range(matrix_row):
        for i in range(len(shark_list)):
            if [row, column] == shark_list[i][0:2]:
                result += shark_list[i][4]
                shark_list.pop(i)
                return



dxdy = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
matrix_row, matrix_column, shark_count = map(int, input().split())
shark_list = [list(map(int, input().split())) for _ in range(shark_count)]

row_short = (matrix_row-1)*2
column_short = (matrix_column-1)*2
for minus in range(len(shark_list)):
    shark_list[minus][0] -= 1
    shark_list[minus][1] -= 1
    if shark_list[minus][2] == 1 or shark_list[minus][2] == 2:
        shark_list[minus][2] = shark_list[minus][2] % row_short
    elif shark_list[minus][2] == 3 or shark_list[minus][2] == 4:
        shark_list[minus][2] = shark_list[minus][2] % column_short

result = 0
column = -1
for _ in range(matrix_column):
    visited = [[-1]*(matrix_column-1) for _ in range(matrix_row-1)]
    print(visited)
    column += 1
    catch(column)
    remove_list = []
    for j in range(len(shark_list)):
        dx, dy = dxdy[shark_list[j][3]]
        kx, ky = shark_list[j][0], shark_list[j][1]
        flag_count = 0
        for _ in range(shark_list[j][2]):
            nx, ny = kx + dx, ky + dy
            if iswall(nx, ny):
                kx, ky = nx, ny
            else:
                dx, dy = -dx, -dy
                kx, ky = kx + dx, ky + dy
                flag_count += 1
        if flag_count % 2:
            if shark_list[j][3] % 2:
                shark_list[j][3] += 1
            else:
                shark_list[j][3] -= 1
        shark_list[j][0], shark_list[j][1] = kx, ky
        print(j)
        if visited[shark_list[j][0]][shark_list[j][1]] < 0:
            visited[shark_list[j][0]][shark_list[j][1]] = j
        else:
            if shark_list[j][4] > shark_list[visited[shark_list[j][0]][shark_list[j][1]]][4]:
                remove_list.append(visited[shark_list[j][0]][shark_list[j][1]])
                visited[shark_list[j][0]][shark_list[j][1]] = j
            else:
                remove_list.append(j)
    remove_list.sort()
    for ii in range(len(remove_list)-1, -1, -1):
        shark_list.pop(remove_list[ii])
print(result)
