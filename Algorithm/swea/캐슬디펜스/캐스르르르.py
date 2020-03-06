import sys

sys.stdin = open('input.txt')


def power_set(k, n, arr, t):
    global result
    if k == n:
        count = 0
        for i in range(n):
            if t[i] == 2:
                count += 1
        if count == 3:
            result.append(t[:])
    else:
        t[k] = arr[k]
        power_set(k+1, n, arr, t)
        t[k] = 0
        power_set(k + 1, n, arr, t)


def BFS(start_node, length):
    queue = [start_node]
    visited = [[0]*matrix_row for _ in range(matrix_column+1)]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        if real_result:
            break
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                if not visited[idy][idx]:
                    visited[idy][idx] = visited[y][x]+1
                    queue.append([idy, idx])
                    if matrix[idy][idx] == 1:
                        if visited[idy][idx] <= length+1:
                            real_result.append([idy, idx])


matrix_column, matrix_row, attack = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_column)]+[0]
copy_matrix = [[0]*matrix_row for _ in range(matrix_column)]
for col_1 in range(matrix_column):
    for row_1 in range(matrix_row):
        copy_matrix[col_1][row_1] = matrix[col_1][row_1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 0]
N = matrix_row
archer = [2]*N
result = []
my_max = 0
power_set(0, N, archer, [0]*N)

for ii in range(len(result)):
    count = 0
    matrix[matrix_column] = result[ii]
    for iii in range(matrix_column):
        my_result = []
        for kk in range(matrix_row):
            if matrix[matrix_column][kk]:
                real_result = []
                BFS([matrix_column, kk], attack)
                if real_result:
                    my_result.append(real_result[0])
        for jj in range(len(my_result)):
            if matrix[my_result[jj][0]][my_result[jj][1]]:
                matrix[my_result[jj][0]][my_result[jj][1]] = 0
                count += 1
        for j in range(matrix_column - 1, -1, -1):
            if j:
                matrix[j] = matrix[j - 1]
            else:
                matrix[j] = [0] * matrix_row

    if count > my_max:
        my_max = count
    for col in range(matrix_column):
        for row in range(matrix_row):
            matrix[col][row] = copy_matrix[col][row]
print(my_max)


