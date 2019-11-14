import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    queue = [start_node]
    visited = [[0]*size for _ in range(size)]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        y = a[0]
        x = a[1]
        for i in range(8):
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < size and 0 <= idx < size:
                if not visited[idy][idx]:
                    if matrix[y][x] == '*':
                        if matrix[idy][idx] != '*':
                            queue.append([idy, idx])
                            visited[idy][idx]


T = int(input())

for test_case in range(1, T+1):
    size = int(input())
    matrix = [list(input()) for _ in range(size)]
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == '.':
                matrix[row][column] = 0
    for jj in matrix:
        print(jj)
    BFS([0, 0])