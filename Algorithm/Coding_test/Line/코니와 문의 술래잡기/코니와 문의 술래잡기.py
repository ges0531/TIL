import sys

sys.stdin = open('input.txt')




def BFS(start_node):
    queue = [start_node]
    visited = [[0]*matrix_row for _ in range(matrix_column)]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                if visited[idy][idx] == 0:
                    if matrix[idy][idx] == 0:
                        visited[idy][idx] = 1
                        matrix[idy][idx] = matrix[idy-1][idx] + matrix[idy][idx-1]
                        queue.append([idy, idx])


matrix_row , matrix_column = map(int, input().split())
matrix = [[0]*matrix_row for _ in range(matrix_column)]
koni_location = list(map(int, input().split()))
matrix[0][0] = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
if koni_location[0] > matrix_row or koni_location[1] > matrix_column:
    print('fail')
else:
    BFS([0, 0])
    print(koni_location[0]+koni_location[1])
    print(matrix[koni_location[0]][koni_location[1]])


