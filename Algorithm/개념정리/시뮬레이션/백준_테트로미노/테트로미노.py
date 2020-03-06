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
                visited[idy][idx] = 0

def final_case(start_node, start_flag, count):
    global my_max
    if count == 3:
        if start_flag > my_max:
            my_max = start_flag
        return
    for j in range(4):
        y = start_node[0]
        x = start_node[1]
        idy = y+dy[j]
        idx = x+dx[j]
        if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
            if not visited[idy][idx]:
                visited[idy][idx] = 1
                final_case([y, x], start_flag+matrix[idy][idx], count+1)
                visited[idy][idx] = 0


matrix_column, matrix_row = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
my_max = 0

# 5번째 경우 고려
visited = [[0]*matrix_row for _ in range(matrix_column)]
for column in range(matrix_column):
    for row in range(matrix_row):
        search_max([column, row], 0, 0)
        final_case([column, row], matrix[column][row], 0)

print(my_max)