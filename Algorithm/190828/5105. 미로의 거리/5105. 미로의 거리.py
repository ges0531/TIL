import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

def BFS(E, v):
    visited = [[0]*size for _ in range(size)]
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t[0]][t[1]]:
            visited[t[0]][t[1]] = 1

        for k in range(len(E[t])):
            if not visited[k]:
                if E[t][k] == 1:
                    queue.append(k)

for test_case in range(1, 1+T):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    size = int(input())
    matrix = [list(map(int, input())) for _ in range(size)]
    for column in range(len(matrix)):
        for row in range(len(matrix[0])):
            if matrix[column][row] == 2:
                location = [column, row]
    BFS(matrix, location)
    print(matrix)
