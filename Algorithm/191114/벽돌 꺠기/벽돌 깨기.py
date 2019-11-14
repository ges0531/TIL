import sys
import itertools

sys.stdin = open('input.txt', 'r')


def block(start_node, size):
    global visited
    queue = [start_node]
    size_queue = [size]
    visited = [[0]*matrix_column for _ in range(matrix_row)]
    while queue:
        a = queue.pop(0)
        visited[a[0]][a[1]] = 1
        b = size_queue.pop(0)
        for i in range(1, b):
            if a[0]+i < matrix_row:
                if not visited[a[0]+i][a[1]]:
                    visited[a[0]+i][a[1]] = 1
                    queue.append([a[0] + i, a[1]])
                    size_queue.append(matrix[a[0] + i][a[1]])
            if a[0]-i >= 0:
                if not visited[a[0] - i][a[1]]:
                    visited[a[0]-i][a[1]] = 1
                    queue.append([a[0] - i, a[1]])
                    size_queue.append(matrix[a[0] - i][a[1]])
            if a[1]+i < matrix_column:
                if not visited[a[0]][a[1]+i]:
                    visited[a[0]][a[1]+i] = 1
                    queue.append([a[0], a[1] + i])
                    size_queue.append(matrix[a[0]][a[1] + i])
            if a[1]-i >= 0:
                if not visited[a[0]][a[1]-i]:
                    visited[a[0]][a[1]-i] = 1
                    queue.append([a[0], a[1] - i])
                    size_queue.append(matrix[a[0]][a[1] - i])


def delete_node():
    global visited
    for row in range(len(visited)):
        for column in range(len(visited[row])):
            if visited[row][column]:
                matrix[row][column] = 0


def down_node(start_node):
    if matrix[start_node[0]+1][start_node[1]]:
        return
    else:
        d = 1
        while True:
            if matrix[start_node[0]+d][start_node[1]]:
                matrix[start_node[0] + d-1][start_node[1]] = matrix[start_node[0]][start_node[1]]
                matrix[start_node[0]][start_node[1]] = 0
                break
            else:
                if start_node[0]+d == matrix_row-1:
                    matrix[start_node[0] + d][start_node[1]] = matrix[start_node[0]][start_node[1]]
                    matrix[start_node[0]][start_node[1]] = 0
                    break
                else:
                    d += 1


def find_start_node(column_number):
    f = 0
    while True:
        if matrix[f][column_number]:
            return f
        else:
            if f == matrix_row-1:
                return 0
            else:
                f += 1


def find_block_count():
    count = 0
    for row_3 in range(len(matrix)):
        for column_3 in range(len(matrix[row_3])):
            if matrix[row_3][column_3]:
                count += 1
    return count


T = int(input())
# T = 1
for test_case in range(1, T+1):
    marble_count, matrix_column, matrix_row = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(matrix_row)]
    copy_matrix = [[0]*matrix_column for _ in range(matrix_row)]
    for copy_1 in range(len(matrix)):
        for copy_2 in range(len(matrix[copy_1])):
            copy_matrix[copy_1][copy_2] = matrix[copy_1][copy_2]
    index_list = [jj for jj in range(matrix_column)]
    my_min = 10000000000
    my_perm = list(itertools.product(index_list, repeat=marble_count))
    for co_1 in range(len(my_perm)):
        for co_2 in range(len(my_perm[co_1])):
            find_matrix_row = find_start_node(my_perm[co_1][co_2])
            block([find_matrix_row, my_perm[co_1][co_2]], matrix[find_matrix_row][my_perm[co_1][co_2]])
            delete_node()
            for row_2 in range(len(matrix)-2, -1, -1):
                for column_2 in range(len(matrix[row_2])-1, -1, -1):
                    down_node([row_2, column_2])
        result = find_block_count()
        if my_min > result:
            my_min = result
        for copy_1 in range(len(matrix)):
            for copy_2 in range(len(matrix[copy_1])):
                matrix[copy_1][copy_2] = copy_matrix[copy_1][copy_2]
    print('#{} {}'.format(test_case, my_min))


