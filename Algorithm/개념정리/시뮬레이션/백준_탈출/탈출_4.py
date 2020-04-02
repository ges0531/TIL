import sys

sys.stdin = open('input.txt', 'r')


def water_BFS(water_node):
    water_queue = water_node[:]
    for j in range(len(water_queue)):
        water_visited[water_node[j][0]][water_node[j][1]] = 1
    while water_queue:
        for jj in range(len(water_node)):
            if water_queue:
                a = water_queue.pop(0)
                for k in range(4):
                    y = a[0]
                    x = a[1]
                    idy = y+dy[k]
                    idx = x+dx[k]
                    if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                        if not water_visited[idy][idx]:
                            if matrix[idy][idx] == '.':
                                water_visited[idy][idx] = water_visited[y][x] + 1
                                if water_visited[idy][idx] <= visited[idy][idx]:
                                    matrix[idy][idx] = '*'
                                water_queue.append([idy, idx])


def BFS(start_node):
    queue = [start_node]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        b = queue.pop(0)
        for k in range(4):
            y = b[0]
            x = b[1]
            idy = y+dy[k]
            idx = x+dx[k]
            if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                if not visited[idy][idx]:
                    if matrix[idy][idx] == '.':
                        visited[idy][idx] = visited[y][x] + 1
                        queue.append([idy, idx])


matrix_column, matrix_row = map(int, input().split())
matrix = [list(input()) for _ in range(matrix_column)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
water_visited = [[0]*matrix_row for _ in range(matrix_column)]
visited = [[0]*matrix_row for _ in range(matrix_column)]
S_location = []
water_location = []
D_location = []
my_min = 1000000
for column in range(len(matrix)):
    for row in range(len(matrix[column])):
        if matrix[column][row] == 'S':
            S_location = [column, row]
        elif matrix[column][row] == '*':
            water_location.append([column, row])
        elif matrix[column][row] == 'D':
            D_location = [column, row]

BFS(S_location)
result = water_BFS(water_location)
for ii in range(4):
    yy = D_location[0]
    xx = D_location[1]
    idyy = yy+dy[ii]
    idxx = xx+dx[ii]
    if 0 <= idyy < matrix_column and 0 <= idxx < matrix_row:
        if visited[idyy][idxx]:
            if matrix[idyy][idxx] != '*':
                if my_min > visited[idyy][idxx]:
                    my_min = visited[idyy][idxx]
if my_min == 1000000:
    print('KAKTUS')
else:
    print(my_min)


# for v in water_visited:
#     print(v)
# print()
# for v in visited:
#     print(v)




