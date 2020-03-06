import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    queue = [start_node]
    visited = [[0] * matrix_row for _ in range(matrix_column)]
    visited[start_node[0]][start_node[1]] = 1
    visited_en = [matrix[0][0]]
    count = 1
    while queue:
        a = queue.pop(0)
        y = a[0]
        x = a[1]
        for i in range(4):
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                if matrix[idy][idx] not in visited_en:
                    if not visited[idy][idx]:
                        count += 1
                        visited[idy][idx] = count
                        visited_en.append(matrix[idy][idx])
                        queue.append([idy, idx])
    return max(map(max, visited))


matrix_column, matrix_row = map(int, input().split())
matrix = [list(input()) for _ in range(matrix_column)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
print(BFS([0, 0]))
