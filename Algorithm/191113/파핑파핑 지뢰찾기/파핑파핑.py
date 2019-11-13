import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    global visited
    queue = [start_node]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        for j in (0, -1), (0, 1), (-1, 0), (1, 0):
            y = a[0]
            x = a[1]
            idy = y+j[0]
            idx = x+j[1]
            if 0 <= idy < size and 0 <= idx < size:
                if not visited[idy][idx]:
                    if matrix[idy][idx] == 0:
                        visited[idy][idx] = 1
                        queue.append([idy, idx])

T = int(input())
for test_case in range(1, T+1):
    size = int(input())
    matrix = [list(input()) for _ in range(size)]
    visited = [[0] * size for _ in range(size)]
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    count = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            flag = 1
            for i in range(8):
                if 0 <= row+dy[i] < size and 0 <= column+dx[i] < size:
                    if matrix[row][column] == '.':
                        if matrix[row+dy[i]][column+dx[i]] == '*':
                            if not visited[row+dy[i]][column+dx[i]]:
                                visited[row + dy[i]][column + dx[i]] = 1
                                flag = 0
            if flag:
                matrix[row][column] = 0
            else:
                count += 1
    for row_1 in range(len(matrix)):
        for column_1 in range(len(matrix[row_1])):
            if not visited[row_1][column_1]:
                if matrix[row_1][column_1] == 0:
                    BFS([row_1, column_1])
                    count += 1
    print(count)

