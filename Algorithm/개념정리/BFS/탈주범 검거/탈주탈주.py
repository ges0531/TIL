import sys

sys.stdin = open('input.txt', 'r')


def link_check(k, idy, idx):
    if k == 0:
        if matrix[idy][idx] == 1 or matrix[idy][idx] == 2 or matrix[idy][idx] == 5 or matrix[idy][idx] == 6:
            return True
    elif k == 1:
        if matrix[idy][idx] == 1 or matrix[idy][idx] == 2 or matrix[idy][idx] == 4 or matrix[idy][idx] == 7:
            return True
    elif k == 2:
        if matrix[idy][idx] == 1 or matrix[idy][idx] == 3 or matrix[idy][idx] == 4 or matrix[idy][idx] == 5:
            return True
    elif k == 3:
        if matrix[idy][idx] == 1 or matrix[idy][idx] == 3 or matrix[idy][idx] == 6 or matrix[idy][idx] == 7:
            return True


def BFS(start_node, time):
    queue = [start_node]
    visited = [[0]*matrix_column for _ in range(matrix_row)]
    visited[start_node[0]][start_node[1]] = 1
    result_count = 0
    while queue:
        a = queue.pop(0)
        y = a[0]
        x = a[1]
        idy = y
        idx = x
        for i in range(4):
            if matrix[y][x] == 1:
                idy = y+one_list[i][0]
                idx = x+one_list[i][1]
            elif matrix[y][x] == 2:
                idy = y+two_list[i][0]
                idx = x+two_list[i][1]
            elif matrix[y][x] == 3:
                idy = y+three_list[i][0]
                idx = x+three_list[i][1]
            elif matrix[y][x] == 4:
                idy = y+four_list[i][0]
                idx = x+four_list[i][1]
            elif matrix[y][x] == 5:
                idy = y+five_list[i][0]
                idx = x+five_list[i][1]
            elif matrix[y][x] == 6:
                idy = y+six_list[i][0]
                idx = x+six_list[i][1]
            elif matrix[y][x] == 7:
                idy = y+seven_list[i][0]
                idx = x+seven_list[i][1]
            if 0 <= idy < matrix_row and 0 <= idx < matrix_column:
                if idy-y or idx-x:
                    if link_check(i, idy, idx):
                        if not visited[idy][idx]:
                            visited[idy][idx] = visited[y][x]+1
                            if visited[idy][idx] <= time:
                                result_count += 1
                            queue.append([idy, idx])
    return result_count


T = int(input())
# T = 1
for test_case in range(1, T+1):
    matrix_row, matrix_column, escape_row, escape_column, escape_time = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(matrix_row)]
    one_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    two_list = [[-1, 0], [1, 0], [0, 0], [0, 0]]
    three_list = [[0, 0], [0, 0], [0, -1], [0, 1]]
    four_list = [[-1, 0], [0, 0], [0, 0], [0, 1]]
    five_list = [[0, 0], [1, 0], [0, 0], [0, 1]]
    six_list = [[0, 0], [1, 0], [0, -1], [0, 0]]
    seven_list = [[-1, 0], [0, 0], [0, -1], [0, 0]]
    print('#{} {}'.format(test_case, BFS([escape_row, escape_column], escape_time)+1))