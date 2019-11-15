import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    global visited, count
    queue = [start_node]
    while queue:
        a = queue.pop(0)
        y = a[0]
        x = a[1]
        for i in range(8):
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < size and 0 <= idx < size:
                if not matrix[y][x] == '*':
                    if matrix[idy][idx] == '*':
                        break
        else:
            for j in range(8):
                idy = y + dy[j]
                idx = x + dx[j]
                if 0 <= idy < size and 0 <= idx < size:
                    if not visited[idy][idx]:
                        visited[y][x] = 1
                        visited[idy][idx] = 1
                        queue.append([idy, idx])


T = int(input())

for test_case in range(1, T+1):
    size = int(input())
    matrix = [list(input()) for _ in range(size)]
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    dx_2 = [0, 0, -1, 1]
    dy_2 = [-1, 1, 0, 0]
    count = 0
    visited = [[0] * size for _ in range(size)]
    visited_2 = [[0] * size for _ in range(size)]
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if not matrix[row][column] == '*' and not visited[row][column]:
                BFS([row, column])
    for row_1 in range(len(matrix)):
        for column_1 in range(len(matrix[row_1])):
            if not visited[row_1][column_1] and matrix[row_1][column_1] == '.':
                count += 1
    print(count)
