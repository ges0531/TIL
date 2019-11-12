import sys

sys.stdin = open('input.txt', 'r')


def DFS(start_node):
    global visited, flag, my_max
    for i in range(4):
        y = start_node[0]
        x = start_node[1]
        idy = y+dy[i]
        idx = x+dx[i]
        if 0 <= idy < size and 0 <= idx < size:
            if not visited[idy][idx]:
                if matrix[y][x] > matrix[idy][idx]:
                    visited[idy][idx] = visited[y][x]+1
                    DFS([idy, idx])
                    visited[idy][idx] = 0
                else:
                    for j in range(1, cons_depth+1):
                        if matrix[y][x] > matrix[idy][idx]-j:
                            if flag:
                                matrix[idy][idx] -= j
                                visited[idy][idx] = visited[y][x] + 1
                                flag = 0
                                DFS([idy, idx])
                                visited[idy][idx] = 0
                                matrix[idy][idx] += j
                                flag = 1
    result = max(map(max, visited))
    if my_max < result:
        my_max = result


T = int(input())

for test_case in range(1, T+1):
    size, cons_depth = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    up_max = max(map(max, matrix))
    my_max = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == up_max:
                flag = 1
                visited = [[0] * size for _ in range(size)]
                visited[row][column] = 1
                DFS([row, column])
    print('#{} {}'.format(test_case, my_max))