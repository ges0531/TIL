import sys

sys.stdin = open('input.txt', 'r')

def link_index(start_node, end_node, count):
    global flag
    if flag:
        return
    if count > matrix_size:
        return
    if count and start_node == end_node:
        flag = 1
        return
    for i in range(matrix_size):
        if matrix[start_node][i]:
            link_index(i, end_node, count+1)


matrix_size = int(input())
matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
visited = [[0]*matrix_size for _ in range(matrix_size)]
for column in range(matrix_size):
    for row in range(matrix_size):
        flag = 0
        link_index(column, row, 0)
        if flag:
            visited[column][row] = 1
for v in visited:
    print(' '.join(map(str, v)))