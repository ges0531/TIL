import sys, pprint

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    queue = [start_node]
    visited = [[0]*size for _ in range(size)]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        y = a[0]
        x = a[1]
        for i in range(4):
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < size and 0 <= idx < size:
                if not visited[idy][idx]:
                    if matrix[idy][idx]:
                        visited[idy][idx] = visited[y][x] + 1
                        queue.append([idy, idx])

    for v in visited:
        print(v)


def DFS(start_node):
    global visited_2
    for i in range(4):
        y = start_node[0]
        x = start_node[1]
        idy = y+dy[i]
        idx = x+dx[i]
        if 0 <= idy < size and 0 <= idx < size:
            if not visited_2[idy][idx]:
                if matrix[idy][idx]:
                    visited_2[idy][idx] = visited_2[y][x] + 1
                    DFS([idy, idx])
                    visited_2[idy][idx] = 0

    for v in visited_2:
        print(v)
    print()


size = 4
matrix = [list(map(int, input().split())) for _ in range(size)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
BFS([0, 0])
print()
visited_2 = [[0]*size for _ in range(size)]
visited_2[0][0] = 1
DFS([0, 0])