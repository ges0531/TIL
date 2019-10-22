import sys
import collections
sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    global wall_matrix
    queue = collections.deque()
    queue.append(start_node)
    visited = [[0]*matrix_row for _ in range(matrix_column)]
    visited[start_node[0]][start_node[1]] = 1
    flag = 0
    while queue:
        a = queue.popleft()
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                if not visited[idy][idx]:
                    if not wall_matrix[idy][idx]:
                        if flag == 0:
                            if matrix[idy][idx] == 1:
                                matrix[idy][idx] = 0
                                wall_matrix[idy][idx] = 1
                                flag = 1
                        if matrix[idy][idx] == 0:
                            visited[idy][idx] = visited[y][x]+1
                            queue.append([idy, idx])
    if visited[matrix_column-1][matrix_row-1]:
        return visited[matrix_column-1][matrix_row-1]


matrix_column, matrix_row = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(matrix_column)]
count = 0
my_min = 100000000
for col in range(len(matrix)):
    for row in range(len(matrix[col])):
        if matrix[col][row]:
            count += 1
wall_matrix = [[0] * matrix_row for _ in range(matrix_column)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for _ in range(count):
    a = BFS([0, 0])
    if a:
        if a < my_min:
            my_min = a
if my_min == 100000000:
    print(-1)
else:
    print(my_min)