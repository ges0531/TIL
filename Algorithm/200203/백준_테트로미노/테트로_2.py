import sys

sys.stdin = open('input.txt','r')


def search_max(start_node, count, poly_sum):
    global my_max

    if count == 4:
        if my_max < poly_sum:
            my_max = poly_sum
        return
    for i in range(4):
        y = start_node[0]
        x = start_node[1]
        idy = y+dy[i]
        idx = x+dx[i]
        if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
            if not visited[idy][idx]:
                visited[idy][idx] = 1
                search_max([idy, idx], count+1, poly_sum+matrix[idy][idx])


matrix_column, matrix_row = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
my_max = 0

# 5번째 경우 고려

for column in range(matrix_column):
    for row in range(matrix_row):
        visited = [[0]*matrix_row for _ in range(matrix_column)]
        search_max([column, row], 0, 0)

print(my_max)