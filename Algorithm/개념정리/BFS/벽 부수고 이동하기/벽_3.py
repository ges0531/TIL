import sys

sys.stdin = open('input.txt', 'r')

def DFS(start_node, count,  flag):
    global my_min
    if start_node == [matrix_column-1, matrix_row-1]:
        my_min = min(my_min, count)
        return
    if memoization[start_node[0]][start_node[1]] == 0:
        memoization[start_node[0]][start_node[1]] = count
    else:
        if memoization[start_node[0]][start_node[1]] > count:
            memoization[start_node[0]][start_node[1]] = count
        else:
            return
    y = start_node[0]
    x = start_node[1]
    for i in range(4):
        idy = y + dy[i]
        idx = x + dx[i]
        if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
            if not visited[idy][idx]:
                if matrix[idy][idx] == 0:
                    visited[idy][idx] = 1
                    DFS([idy, idx], count+1, flag)
                    visited[idy][idx] = 0
                elif matrix[idy][idx] == 1 and flag == 0:
                    visited[idy][idx] = 1
                    DFS([idy, idx], count+1, 1)
                    visited[idy][idx] = 0


matrix_column, matrix_row = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(matrix_column)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
my_min = 10000000000
visited = [[0]*matrix_row for _ in range(matrix_column)]
memoization = [[0]*matrix_row for _ in range(matrix_column)]
visited[0][0] = 1
DFS([0, 0], 0, 0)
if my_min == 10000000000:
    print(-1)
else:
    print(my_min+1)
