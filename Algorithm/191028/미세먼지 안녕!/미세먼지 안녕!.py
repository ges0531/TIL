import sys

sys.stdin = open('input.txt', 'r')


def air_function_1(start_node):
    a = start_node[0][0]
    b = start_node[0][1]
    while 0 <= a-1:
        matrix[a][b] = matrix[a-1][b]
        a -= 1
    matrix[start_node[0][0]][start_node[0][1]] = 0
    while b < matrix_column-1:
        matrix[a][b] = matrix[a][b+1]
        b += 1
    while a <= start_node[0][0]-1:
        matrix[a][b] = matrix[a+1][b]
        a += 1
    while 0 <= b-1:
        matrix[a][b] = matrix[a][b-1]
        b -= 1
    matrix[start_node[0][0]][start_node[0][1]] = -1


def air_function_2(start_node):
    a = start_node[0][0]
    b = start_node[0][1]
    while a < matrix_row-1:
        matrix[a][b] = matrix[a+1][b]
        a += 1
    matrix[start_node[0][0]][start_node[0][1]] = 0
    while b < matrix_column-1:
        matrix[a][b] = matrix[a][b+1]
        b += 1
    while start_node[0][0] <= a-1:
        matrix[a][b] = matrix[a-1][b]
        a -= 1
    while 0 <= b-1:
        matrix[a][b] = matrix[a][b-1]
        b -= 1
    matrix[start_node[0][0]][start_node[0][1]] = -1


matrix_row, matrix_column, time_count = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(matrix_row)]
dust_matrix = [[0]*matrix_column for _ in range(matrix_row)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
air_location = []
air_location_2 = []
for time in range(time_count):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] != -1 and matrix[row][column]:
                for i in range(4):
                    if 0 <= row+dy[i] < matrix_row and 0 <= column+dx[i] < matrix_column:
                        if matrix[row+dy[i]][column+dx[i]] != -1:
                            dust_matrix[row + dy[i]][column + dx[i]] += (matrix[row][column]//5)
                            dust_matrix[row][column] -= (matrix[row][column] // 5)
            elif matrix[row][column] == -1 and not air_location:
                air_location.append([row, column])
                air_location_2.append([row+1, column])
    for row_2 in range(len(matrix)):
        for column_2 in range(len(matrix[row_2])):
            matrix[row_2][column_2] += dust_matrix[row_2][column_2]
            dust_matrix[row_2][column_2] = 0
    air_function_1(air_location)
    air_function_2(air_location_2)

print(sum(map(sum, matrix))+2)


