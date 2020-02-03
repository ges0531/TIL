import sys
from queue import PriorityQueue

sys.stdin = open('input.txt', 'r')

def BFS(start_node):
    queue = PriorityQueue()
    queue.put((0, 0, [start_node[0], start_node[1]]))
    visited = [[0]*matrix_size for _ in range(matrix_size)]
    visited[start_node[0]][start_node[1]] = 1
    count = 0
    while queue:
        a = queue.get()
        count += 1
        if [a[2][0], a[2][1]] == [matrix_size-1, matrix_size-1]:
            return visited[matrix_size-1][matrix_size-1]-1
        for i in range(4):
            y = a[2][0]
            x = a[2][1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < matrix_size and 0 <= idx < matrix_size:
                if not visited[idy][idx]:
                    visited[idy][idx] = visited[y][x] + matrix[y][x]
                    queue.put((matrix[idy][idx], count, [idy, idx]))


T = int(input())
# T = 4
for test_case in range(1, T+1):
    matrix_size = int(input())
    matrix = [list(map(int, input())) for _ in range(matrix_size)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    print(BFS([0, 0]))