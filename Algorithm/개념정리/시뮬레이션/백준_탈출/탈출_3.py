import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node, water_list):
    queue = [start_node]
    water_queue = water_list[:]
    visited = [[0]*matrix_row for _ in range(matrix_column)]
    water_visited = [[0]*matrix_row for _ in range(matrix_column)]
    visited[start_node[0]][start_node[1]] = 1
    for j in range(len(water_list)):
        water_visited[water_list[j][0]][water_list[j][1]] = 1
    while queue:
        for w in range(len(water_list)):
            if water_queue:
                b = water_queue.pop(0)
                for i in range(4):
                    water_y = b[0]
                    water_x = b[1]
                    water_idy = water_y+dy[i]
                    water_idx = water_x + dx[i]
                    if 0 <= water_idy < matrix_column and 0 <= water_idx < matrix_row:
                        if not water_visited[water_idy][water_idx]:
                            if matrix[water_idy][water_idx] == '.' or matrix[water_idy][water_idx] == 'S':
                                matrix[water_idy][water_idx] = '*'
                                water_visited[water_idy][water_idx] = 1
                                water_queue.append([water_idy, water_idx])
        a = queue.pop(0)
        for k in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[k]
            idx = x+dx[k]
            if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                if not visited[idy][idx]:
                    if matrix[idy][idx] == 'D':
                        return visited[y][x]
                    elif matrix[idy][idx] == '.':
                        matrix[idy][idx] = 'S'
                        visited[idy][idx] = visited[y][x] + 1
                        queue.append([idy, idx])
        for m in matrix:
            print(m)
        print()


matrix_column, matrix_row = map(int, input().split())
matrix = [list(input()) for _ in range(matrix_column)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
S_location = []
water_location = []
for column in range(len(matrix)):
    for row in range(len(matrix[column])):
        if matrix[column][row] == 'S':
            S_location = [column, row]
        elif matrix[column][row] == '*':
            water_location.append([column, row])
result = BFS(S_location, water_location)
if result:
    print(result)
else:
    print('KAKTUS')

