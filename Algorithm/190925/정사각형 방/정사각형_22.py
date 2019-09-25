import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    global my_max, visited
    y = 0
    x = 0
    queue = [start_node]
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
                    if matrix[idy][idx] == matrix[y][x]+1:
                        visited[idy][idx] = visited[y][x]+1
                        queue.append([idy, idx])
    if my_max <= visited[y][x]:
        my_max = visited[y][x]



T = int(input())

for test_case in range(1, T+1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[0] * size for _ in range(size)]
    my_max = 0
    num = 1000000000

    for column in range(len(matrix)):
        for row in range(len(matrix[column])):
            if visited[column][row] == 0 or visited[column][row] == 1:
                BFS([column, row])


    print('#{} {} {}'.format(test_case, 1, my_max))