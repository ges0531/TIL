import sys

sys.stdin = open('input.txt', 'r')

def BFS(start_node):
    queue = [start_node]
    visited = [[0] * N for _ in range(N)]
    visited[start_node[0]][start_node[1]] = 1
    visited_2 = [[0] * N for _ in range(N)]
    while queue:
        a = queue.pop(0)
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < N and 0 <= idx < N:
                if not visited[idy][idx]:
                    visited[idy][idx] = 1
                    queue.append([idy, idx])
                    if (matrix[idy][idx] + matrix[y][x]) > visited_2[idy][idx]:
                        visited_2[idy][idx] += matrix[idy][idx] + matrix[y][x]
    for v in visited_2:
        print(v)


T = int(input())
T = 3
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    BFS([0, 0])