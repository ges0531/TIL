import sys

sys.stdin = open('input.txt', 'r')


def DFS(start_node):
    stack = [start_node]
    visited = [[0]*4 for _ in range(4)]
    visited[start_node[0]][start_node[1]] = 1
    count = 0
    while stack:
        a = stack.pop()
        visited[a[0]][a[1]] = 1
        count += 1
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < 4 and 0 <= idx < 4:
                if visited[idy][idx] == 0:
                    stack.append([idy, idx])
        if count > 6:
            break
    for j in visited:
        print(j)



T = int(input())

for test_case in range(1, T+1):
    matrix = [list(input().split()) for _ in range(4)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    DFS([0, 0])