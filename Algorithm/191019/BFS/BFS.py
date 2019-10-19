import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    queue = [start_node]
    visited = [[0]*size for _ in range(size)]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < size and 0 <= idx < size:
                if not visited[idy][idx]:
                    if matrix[idy][idx] == 0:
                        visited[idy][idx] = visited[y][x]+1
                        queue.append([idy, idx])
    for k in visited:
        print(k)

size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
BFS([0, 0])