import sys

sys.stdin = open('input.txt', 'r')


def pipe_search(start_node, direction_flag):
    global count
    if start_node == [matrix_size-1, matrix_size-1]:
        count += 1
        return
    if not (0 <= start_node[0] < matrix_size and 0 <= start_node[1] < matrix_size):
        return
    if matrix[start_node[0]][start_node[1]] == 1:
        return
    if direction_flag == 2:
        if matrix[start_node[0]-1][start_node[1]] == 1:
            return
        elif matrix[start_node[0]][start_node[1]-1] == 1:
            return
    y = start_node[0]
    x = start_node[1]
    if direction_flag == 0:
        pipe_search([y, x+1], 0)
        pipe_search([y+1, x+1], 2)
    elif direction_flag == 1:
        pipe_search([y+1, x], 1)
        pipe_search([y+1, x+1], 2)
    elif direction_flag == 2:
        pipe_search([y, x+1], 0)
        pipe_search([y + 1, x], 1)
        pipe_search([y + 1, x + 1], 2)

matrix_size = int(input())
matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
count = 0

pipe_search([0, 1], 0)
print(count)

