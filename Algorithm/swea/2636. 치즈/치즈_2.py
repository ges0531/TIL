import sys

sys.stdin = open('input.txt', 'r')


def DFS(location_a, location_b, x):
    location = [location_a, location_b]
    stack = []
    while True:
        check = 0
        for g in range(4):
            if matrix[location[0]+dy[g]][location[1]+dx[g]] == x:
                matrix[location[0]][location[1]] = 0
                matrix[location[0] + dy[g]][location[1] + dx[g]] = 0
                for h in range(4):
                    if matrix[column_3 + dy[h]][row_3 + dx[h]] == 1:
                        matrix[column_3 + dy[h]][row_3 + dx[h]] = 4
                location[0] += dy[g]
                location[1] += dx[g]
                stack.append(location)
                check = 1
        if stack == []:
            break
        if check == 0:
            location = stack.pop()


matrix_column, matrix_row = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
hour = 0
result = []
result_count = 1
while result_count != 0:
    for column in range(len(matrix)):
        for row in range(len(matrix[0])):
            if matrix[column][row] == 0:
                count = 0
                for i in range(4):
                    a = 0
                    b = 0
                    while True:
                        a += dy[i]
                        b += dx[i]
                        if column+a < 0 or column+a >= matrix_column:
                            break
                        elif row+b < 0 or row+b >= matrix_row:
                            break
                        elif matrix[column+a][row+b] == 1:
                            count += 1
                            break
                if count == 4:
                    matrix[column][row] = 3
    for i in matrix:
        print(i)
    print('## 1')
    for column_2 in range(len(matrix)):
        for row_2 in range(len(matrix[0])):
            if matrix[column_2][row_2] == 1:
                for j in range(4):
                    if matrix[column_2+dy[j]][row_2+dx[j]] == 0:
                        matrix[column_2][row_2] = 4
                        break
    for i in matrix:
        print(i)
    print('## 2')
    for column_3 in range(len(matrix)):
        for row_3 in range(len(matrix[0])):
            if matrix[column_3][row_3] == 4:
                matrix[column_3][row_3] = 0
    for i in matrix:
        print(i)
    print('## 3')

    for column_3 in range(len(matrix)):
        for row_3 in range(len(matrix[0])):
            if matrix[column_3][row_3] == 3:
                for h in range(4):
                    if matrix[column_3+dy[h]][row_3+dx[h]] == 0:
                        DFS(column_3, row_3, 3)

    for i in matrix:
        print(i)
    print('##4')

    for column_3 in range(len(matrix)):
        for row_3 in range(len(matrix[0])):
            if matrix[column_3][row_3] == 3:
                matrix[column_3][row_3] = 0
    for i in matrix:
        print(i)
    print('##5')


    hour += 1
    total_count = sum(matrix, [])
    result_count = total_count.count(1) + total_count.count(4)
    result.append(result_count)
print(hour)
print(result[-2])
