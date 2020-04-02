import sys

sys.stdin = open('input.txt', 'r')

def BFS(start_node):
    global my_min
    queue = [start_node]
    visited = [[0]*len(matrix[0]) for _ in range(len(matrix))]
    visited[start_node[0]][start_node[1]] = 1
    result = 0
    while queue:
        if result > my_min:
            break
        a = queue.pop(0)
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < len(matrix) and 0 <= idx < len(matrix[0]):
                if not visited[idy][idx]:
                    if matrix[y][x] > matrix[idy][idx]:
                        if matrix[idy][idx] + height >= matrix[y][x]:
                            visited[idy][idx] = 1
                            queue.append([idy, idx])
                        else:
                            result += matrix[y][x] - matrix[idy][idx]
                            visited[idy][idx] = 1
                            queue.append([idy, idx])
                    else:
                        if matrix[y][x] + height >= matrix[idy][idx]:
                            visited[idy][idx] = 1
                            queue.append([idy, idx])
                        else:
                            result += matrix[idy][idx] - matrix[y][x]
                            visited[idy][idx] = 1
                            queue.append([idy, idx])

    if my_min > result:
        my_min = result


matrix = [list(map(int, input().split())) for _ in range(4)]
height = 3
my_min = 100000000000
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for column in range(len(matrix)):
    for row in range(len(matrix[column])):
        BFS([[column, row]])
