import sys

sys.stdin = open('input.txt', 'r')


def pipe_search(start_node):
    stack = [start_node]
    count = 0
    while stack:
        a = stack.pop()
        y = a[0]
        x = a[1]
        if [y, x] == [matrix_size-1, matrix_size-1]:
            count += 1
        else:
            if a[2] == 0:
                if x+1 < matrix_size:
                    if matrix[y][x+1] == 0:
                        stack.append([y, x+1, 0])
                if y+1 < matrix_size and x+1 < matrix_size:
                    if matrix[y+1][x+1] == matrix[y+1][x] == matrix[y][x+1] == 0:
                        stack.append([y+1, x+1, 2])
            elif a[2] == 1:
                if y+1 < matrix_size:
                    if matrix[y+1][x] == 0:
                        stack.append([y+1, x, 1])
                if y+1 < matrix_size and x+1 < matrix_size:
                    if matrix[y+1][x+1] == matrix[y+1][x] == matrix[y][x+1] == 0:
                        stack.append([y+1, x+1, 2])
            elif a[2] == 2:
                if x + 1 < matrix_size:
                    if matrix[y][x + 1] == 0:
                        stack.append([y, x + 1, 0])
                if y + 1 < matrix_size:
                    if matrix[y + 1][x] == 0:
                        stack.append([y + 1, x, 1])
                if y + 1 < matrix_size and x + 1 < matrix_size:
                    if matrix[y+1][x+1] == matrix[y+1][x] == matrix[y][x+1] == 0:
                        stack.append([y+1, x+1, 2])
    return count


matrix_size = int(input())
matrix = [list(map(int, input().split())) for _ in range(matrix_size)]

print(pipe_search([0, 1, 0]))

