import sys

sys.stdin = open('input.txt', 'r')


def up_location(start_node):
    y = start_node[0]
    x = start_node[1]
    while True:
        idy = y + dy[0]
        idx = x + dx[0]
        if matrix[idy][idx] == '#':
            break
        elif matrix[idy][idx] == 'O':
            return [-1, -1]
        else:
            y = idy
            x = idx
    return [y, x]


def down_location(start_node):
    y = start_node[0]
    x = start_node[1]
    while True:
        idy = y + dy[1]
        idx = x + dx[1]
        if matrix[idy][idx] == '#':
            break
        elif matrix[idy][idx] == 'O':
            return [-1, -1]
        else:
            y = idy
            x = idx
    return [y, x]


def left_location(start_node):
    y = start_node[0]
    x = start_node[1]
    while True:
        idy = y + dy[2]
        idx = x + dx[2]
        if matrix[idy][idx] == '#':
            break
        elif matrix[idy][idx] == 'O':
            return [-1, -1]
        else:
            y = idy
            x = idx
    return [y, x]


def right_location(start_node):
    y = start_node[0]
    x = start_node[1]
    while True:
        idy = y + dy[3]
        idx = x + dx[3]
        if matrix[idy][idx] == '#':
            break
        elif matrix[idy][idx] == 'O':
            return [-1, -1]
        else:
            y = idy
            x = idx
    return [y, x]


def marble_escape(start_node, count):
    global my_min
    if count == 11:
        return
    if start_node == [-1, -1]:
        my_min = min(my_min, count)
        return
    y = start_node[0]
    x = start_node[1]
    if not matrix[y+dy[0]][x+dx[0]] == '#':
        marble_escape(up_location([y, x]), count+1)
    if not matrix[y+dy[1]][x+dx[1]] == '#':
        marble_escape(down_location([y, x]), count+1)
    if not matrix[y+dy[2]][x+dx[2]] == '#':
        marble_escape(left_location([y, x]), count+1)
    if not matrix[y+dy[3]][x+dx[3]] == '#':
        marble_escape(right_location([y, x]), count+1)


def marble_escape_2(start_node, count):
    global my_min_2
    if count == 11:
        return
    if start_node == [-1, -1]:
        my_min_2 = min(my_min_2, count)
        return
    y = start_node[0]
    x = start_node[1]
    if not matrix[y+dy[0]][x+dx[0]] == '#':
        marble_escape_2(up_location([y, x]), count+1)
    if not matrix[y+dy[1]][x+dx[1]] == '#':
        marble_escape_2(down_location([y, x]), count+1)
    if not matrix[y+dy[2]][x+dx[2]] == '#':
        marble_escape_2(left_location([y, x]), count+1)
    if not matrix[y+dy[3]][x+dx[3]] == '#':
        marble_escape_2(right_location([y, x]), count+1)


matrix_column, matrix_row = map(int, input().split())
matrix = [list(input()) for _ in range(matrix_column)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
my_min = 100000
my_min_2 = 100000
flag_count = 0
flag_count_2 = 0
for column in range(matrix_column):
    for row in range(matrix_row):
        if matrix[column][row] == 'R':
            marble_escape([column, row], 0)
        elif matrix[column][row] == 'B':
            marble_escape_2([column, row], 0)

if my_min == 100000:
    print(-1)
elif my_min == my_min_2:
    print(-1)
else:
    print(my_min)