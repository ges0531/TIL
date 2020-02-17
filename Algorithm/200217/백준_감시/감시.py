import sys

sys.stdin = open('input.txt', 'r')

def cctv_search(start_node, direction):
    y = start_node[0]
    x = start_node[1]
    idy = y+dy[direction]
    idx = x+dx[direction]
    if matrix[y][x] == 6:
        return
    if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
        visited[idy][idx] = 1
        cctv_search([idy, idx], direction)



matrix_column,  matrix_row = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[0]*matrix_row for _ in range(matrix_column)]
