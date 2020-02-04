import sys
from queue import PriorityQueue

sys.stdin = open('input.txt', 'r')

def BFS(start_node):
    queue = [start_node]
    visited = [[0]*matrix_size for _ in range(matrix_size)]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        # visited[a[0]][a[1]] = 1
        if a == [matrix_size-1, matrix_size-1]:
            return memoization[matrix_size-1][matrix_size-1]
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < matrix_size and 0 <= idx < matrix_size:
                if matrix[idy][idx] + memoization[y][x] < memoization[idy][idx]:
                    memoization[idy][idx] = matrix[idy][idx] + memoization[y][x]
                if not visited[idy][idx]:
                    memoization[idy][idx] = memoization[y][x]+matrix[idy][idx]
                    visited[idy][idx] = 1
                    if queue:
                        if matrix[idy][idx] < matrix[queue[0][0]][queue[0][1]]:
                            queue = [[idy, idx]]+queue
                        else:
                            queue.append([idy, idx])
                    else:
                        queue.append([idy, idx])
        for m in memoization:
            print(m)
        print()



T = int(input())
T = 3
for test_case in range(1, T+1):
    matrix_size = int(input())
    matrix = [list(map(int, input())) for _ in range(matrix_size)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    memoization = [[0]*matrix_size for _ in range(matrix_size)]

    print(BFS([0, 0]))