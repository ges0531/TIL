import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    global copy_count
    queue = [start_node]
    visited = [[0]*matrix_row for _ in range(matrix_column)]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        for j in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[j]
            idx = x+dx[j]
            if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                if not visited[idy][idx]:
                    if copy_list[idy][idx] == 0:
                        copy_list[idy][idx] = 2
                        copy_count -= 1
                        visited[idy][idx] = 1
                        queue.append([idy, idx])


def comb(n, r, arr, t):
    global my_max, copy_count, zero_count
    if r == 0:
        copy_count = zero_count
        for copy_1 in range(matrix_column):
            for copy_2 in range(matrix_row):
                copy_list[copy_1][copy_2] = matrix[copy_1][copy_2]
        for i in range(3):
            copy_list[t[i][0]][t[i][1]] = 1
        for k in range(len(virus_list)):
            BFS(virus_list[k])
        for i in range(3):
            copy_list[t[i][0]][t[i][1]] = 0
        if my_max < copy_count:
            my_max = copy_count
        return
    elif r > n:
        return
    t[r-1] = arr[n-1]
    comb(n-1, r-1, arr, t)
    comb(n-1, r, arr, t)


matrix_column, matrix_row = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
zero_list = []
virus_list = []
zero_count = 0
copy_count = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
my_max = 0
copy_list = [[0]*matrix_row for _ in range(matrix_column)]
for column in range(matrix_column):
    for row in range(matrix_row):
        if matrix[column][row] == 0:
            zero_list.append([column, row])
            zero_count += 1
        elif matrix[column][row] == 2:
            virus_list.append([column, row])

comb(zero_count, 3, zero_list, [0]*3)
print(my_max-3)