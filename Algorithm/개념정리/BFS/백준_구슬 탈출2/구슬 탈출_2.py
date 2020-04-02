import sys

sys.stdin = open('input.txt', 'r')


def up_location(start_node, flag):
    y = start_node[0]
    x = start_node[1]
    while True:
        idy = y + dy[0]
        idx = x + dx[0]
        if flag:
            if matrix[idy][idx] == '#' or matrix[idy][idx] == 'B':
                break
            elif matrix[idy][idx] == 'O':
                return [-1, -1]
            else:
                y = idy
                x = idx
        else:
            if matrix[idy][idx] == '#' or matrix[idy][idx] == 'R':
                break
            elif matrix[idy][idx] == 'O':
                return [-1, -1]
            else:
                y = idy
                x = idx

    return [y, x]


def down_location(start_node, flag):
    y = start_node[0]
    x = start_node[1]
    while True:
        idy = y + dy[1]
        idx = x + dx[1]
        if flag:
            if matrix[idy][idx] == '#' or matrix[idy][idx] == 'B':
                break
            elif matrix[idy][idx] == 'O':
                return [-1, -1]
            else:
                y = idy
                x = idx
        else:
            if matrix[idy][idx] == '#' or matrix[idy][idx] == 'R':
                break
            elif matrix[idy][idx] == 'O':
                return [-1, -1]
            else:
                y = idy
                x = idx
    return [y, x]


def left_location(start_node, flag):
    y = start_node[0]
    x = start_node[1]
    while True:
        idy = y + dy[2]
        idx = x + dx[2]
        if flag:
            if matrix[idy][idx] == '#' or matrix[idy][idx] == 'B':
                break
            elif matrix[idy][idx] == 'O':
                return [-1, -1]
            else:
                y = idy
                x = idx
        else:
            if matrix[idy][idx] == '#' or matrix[idy][idx] == 'R':
                break
            elif matrix[idy][idx] == 'O':
                return [-1, -1]
            else:
                y = idy
                x = idx
    return [y, x]


def right_location(start_node, flag):
    y = start_node[0]
    x = start_node[1]
    while True:
        idy = y + dy[3]
        idx = x + dx[3]
        if flag:
            if matrix[idy][idx] == '#' or matrix[idy][idx] == 'B':
                break
            elif matrix[idy][idx] == 'O':
                return [-1, -1]
            else:
                y = idy
                x = idx
        else:
            if matrix[idy][idx] == '#' or matrix[idy][idx] == 'R':
                break
            elif matrix[idy][idx] == 'O':
                return [-1, -1]
            else:
                y = idy
                x = idx
    return [y, x]


def marble_escape(start_node, start_node_2, count, count_2, flag):
    global my_min, my_min_2
    if flag:
        if count == 11:
            return
        if start_node == [-1, -1]:
            my_min = min(my_min, count)
            return
        y = start_node[0]
        x = start_node[1]
        if not matrix[y+dy[0]][x+dx[0]] == '#' and not matrix[y+dy[0]][x+dx[0]] == 'B':
            matrix[y][x] = '.'
            idy, idx = up_location([y, x], flag)
            matrix[idy][idx] = 'R'
            marble_escape([idy, idx], start_node_2, count+1, count_2, 0)
            matrix[y][x] = 'R'
            matrix[idy][idx] = '.'
        if not matrix[y+dy[1]][x+dx[1]] == '#' and not matrix[y+dy[1]][x+dx[1]] == 'B':
            matrix[y][x] = '.'
            idy, idx = down_location([y, x], flag)
            matrix[idy][idx] = 'R'
            marble_escape([idy, idx], start_node_2, count + 1, count_2, 0)
            matrix[y][x] = 'R'
            matrix[idy][idx] = '.'
        if not matrix[y+dy[2]][x+dx[2]] == '#'and not matrix[y+dy[2]][x+dx[2]] == 'B':
            matrix[y][x] = '.'
            idy, idx = left_location([y, x], flag)
            matrix[idy][idx] = 'R'
            marble_escape([idy, idx], start_node_2, count + 1, count_2, 0)
            matrix[y][x] = 'R'
            matrix[idy][idx] = '.'
        if not matrix[y+dy[3]][x+dx[3]] == '#'and not matrix[y+dy[3]][x+dx[3]] == 'B':
            matrix[y][x] = '.'
            idy, idx = right_location([y, x], flag)
            matrix[idy][idx] = 'R'
            marble_escape([idy, idx], start_node_2, count + 1, count_2, 0)
            matrix[y][x] = 'R'
            matrix[idy][idx] = '.'
    else:
        if count_2 == 11:
            return
        if start_node_2 == [-1, -1]:
            my_min_2 = min(my_min_2, count_2)
            return
        y = start_node_2[0]
        x = start_node_2[1]
        if not matrix[y+dy[0]][x+dx[0]] == '#'and not matrix[y+dy[0]][x+dx[0]] == 'R':
            matrix[y][x] = '.'
            idy, idx = up_location([y, x], flag)
            matrix[idy][idx] = 'B'
            marble_escape(start_node, [idy, idx], count, count_2+1, 1)
            matrix[y][x] = 'B'
            matrix[idy][idx] = '.'
        if not matrix[y+dy[1]][x+dx[1]] == '#'and not matrix[y+dy[1]][x+dx[1]] == 'R':
            matrix[y][x] = '.'
            idy, idx = down_location([y, x], flag)
            matrix[idy][idx] = 'B'
            marble_escape(start_node, [idy, idx], count, count_2+1, 1)
            matrix[y][x] = 'B'
            matrix[idy][idx] = '.'
        if not matrix[y+dy[2]][x+dx[2]] == '#'and not matrix[y+dy[2]][x+dx[2]] == 'R':
            matrix[y][x] = '.'
            idy, idx = left_location([y, x], flag)
            matrix[idy][idx] = 'B'
            marble_escape(start_node, [idy, idx], count, count_2+1, 1)
            matrix[y][x] = 'B'
            matrix[idy][idx] = '.'
        if not matrix[y+dy[3]][x+dx[3]] == '#'and not matrix[y+dy[3]][x+dx[3]] == 'R':
            matrix[y][x] = '.'
            idy, idx = right_location([y, x], flag)
            matrix[idy][idx] = 'B'
            marble_escape(start_node, [idy, idx], count, count_2+1, 1)
            matrix[y][x] = 'B'
            matrix[idy][idx] = '.'


# def marble_escape_2(start_node, count, flag):
#     global my_min_2, flag_2
#     if count == 11:
#         return
#     if start_node == [-1, -1]:
#         if my_min_2 > count:
#             my_min_2 = count
#             flag_2 = flag
#     y = start_node[0]
#     x = start_node[1]
#     if not matrix[y+dy[0]][x+dx[0]] == '#':
#         marble_escape_2(up_location([y, x]), count+1, 0)
#     if not matrix[y+dy[1]][x+dx[1]] == '#':
#         marble_escape_2(down_location([y, x]), count+1, 1)
#     if not matrix[y+dy[2]][x+dx[2]] == '#':
#         marble_escape_2(left_location([y, x]), count+1, 2)
#     if not matrix[y+dy[3]][x+dx[3]] == '#':
#         marble_escape_2(right_location([y, x]), count+1, 3)


matrix_column, matrix_row = map(int, input().split())
matrix = [list(input()) for _ in range(matrix_column)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
my_min = 100000
my_min_2 = 100000
flag_count = 0
flag_count_2 = 0
r_location = []
b_location = []
for column in range(matrix_column):
    for row in range(matrix_row):
        if matrix[column][row] == 'R':
            r_location = [column, row]
        elif matrix[column][row] == 'B':
            b_location = [column, row]
marble_escape(r_location, b_location, 0, 0, 1)
print(my_min)
if my_min == 100000:
    print(-1)
elif my_min == my_min_2:
    print(-1)
else:
    print(my_min)