import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    queue = deque()
    queue.append(start_node)
    visited = [[[0, 0] for _ in range(matrix_row)] for _ in range(matrix_column)]
    visited[start_node[0]][start_node[1]][0] = 1
    while queue:
        y, x, flag = queue.popleft()
        for i in range(4):
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                if not visited[idy][idx][flag]:
                    if matrix[idy][idx] == 0:
                        visited[idy][idx][flag] = visited[y][x][flag] + 1
                        queue.append([idy, idx, flag])
                    elif matrix[idy][idx] == 1 and flag == 0:
                        visited[idy][idx][1] = visited[y][x][flag] + 1
                        queue.append([idy, idx, 1])
    return visited[matrix_column-1][matrix_row-1]


matrix_column, matrix_row = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(matrix_column)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = BFS([0, 0, 0])
if result == [0, 0]:
    print(-1)
else:
    if result[0] == 0 or result[1] == 0:
        print(sum(result))
    else:
        print(min(result))
