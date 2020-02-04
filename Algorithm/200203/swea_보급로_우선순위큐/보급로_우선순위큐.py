import sys
from queue import PriorityQueue

sys.stdin = open('input.txt', 'r')

def BFS(start_node):
    queue = [start_node]
    visited = [[0]*matrix_size for _ in range(matrix_size)]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        print(a)
        if a == [matrix_size-1, matrix_size-1]:
            return visited[matrix_size-1][matrix_size-1]-1
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < matrix_size and 0 <= idx < matrix_size:
                if not visited[idy][idx]:
                    visited[idy][idx] = 1
                    if queue:
                        if matrix[idy][idx] < matrix[queue[0][0]][queue[0][1]]:
                            queue = [[idy, idx]]+queue
                        else:
                            queue.append([idy, idx])
                    else:
                        queue.append([idy, idx])
        for v in visited:
            print(v)
        print()



T = int(input())
T = 1
for test_case in range(1, T+1):
    matrix_size = int(input())
    matrix = [list(map(int, input())) for _ in range(matrix_size)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    print(BFS([0, 0]))