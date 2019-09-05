import sys

sys.stdin = open('input.txt', 'r')

T = int(input())


def track(start_node):
    result = 0
    queue = start_node
    visited = [[0]*size for _ in range(size)]
    visited[start_node[0][0]][start_node[0][1]] = 1
    stop = 0
    while queue:
        a = queue.pop(0)
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < size and 0 <= idx < size:
                if visited[idy][idx] == 0:
                    if matrix[idy][idx] == 0 or matrix[idy][idx] == 3:
                        visited[idy][idx] = visited[y][x] + 1
                        result = visited[idy][idx]
                        queue.append([idy, idx])
    for col_2 in range(len(matrix)):
        for row_2 in range(len(matrix[0])):
            if matrix[col_2][row_2] == 3:
                if visited[col_2][row_2]:
                    return visited[col_2][row_2]-2
                else:
                    return 0
for test_case in range(1, T+1):
    size = int(input())
    matrix = [list(map(int, input())) for _ in range(size)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    start = []
    for column in range(len(matrix)):
        for row in range(len(matrix[0])):
            if matrix[column][row] == 2:
                start.append([column, row])
    print('#{} {}'.format(test_case, track(start)))
