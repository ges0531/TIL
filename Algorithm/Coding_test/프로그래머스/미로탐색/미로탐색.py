import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    global result
    queue = [start_node]
    visited = [[0]*end_node[1] for _ in range(end_node[0])]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < end_node[0] and 0 <= idx < end_node[1]:
                if not visited[idy][idx]:
                    if matrix[idy][idx]:
                        visited[idy][idx] = visited[y][x]+1
                        queue.append([idy, idx])
    result = visited[end_node[0]-1][end_node[1]-1]
end_node = list(map(int, input().split()))
matrix = [list(map(int, list(input()))) for _ in range(end_node[0])]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = 0
BFS([0, 0])
print(result)