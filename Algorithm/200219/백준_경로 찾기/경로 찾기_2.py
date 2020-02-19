import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    queue = [start_node]
    while queue:
        a = queue.pop(0)
        for i in range(matrix_size):
            if not visited[start_node][i]:
                if matrix[a][i]:
                    visited[start_node][i] = 1
                    queue.append(i)


matrix_size = int(input())
matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
visited = [[0]*matrix_size for _ in range(matrix_size)]
for column in range(matrix_size):
    for row in range(matrix_size):
        if matrix[column][row]:
            BFS(column)
for v in visited:
    print(' '.join(map(str, v)))
