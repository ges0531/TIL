import sys

sys.stdin = open('input.txt', 'r')


def DFS(x):
    stack = [[0, 0]]
    Y, X = 0, 0
    check = 0
    while stack:
        if check == 0:
            Y, X = stack.pop()
        check = 0
        for i in range(4):
            if 0 <= Y+dy[i] < matrix_column and 0 <= X+dx[i] < matrix_row:
                if matrix[Y+dy[i]][X+dx[i]] == x:
                    matrix[Y][X] = 2
                    matrix[Y + dy[i]][X + dx[i]] = 2
                    Y = Y+dy[i]
                    X = X+dx[i]
                    stack.append([Y, X])
                    check = 1
                    break


matrix_column, matrix_row = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_column)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
hour = 0
result = []
result_count = 1
while result_count != 0:
    DFS(0)
    for column in range(len(matrix)):
        for row in range(len(matrix[0])):
            if matrix[column][row] == 2:
                matrix[column][row] = 0
                for j in range(4):
                    if column+dy[j] >= 0 and column+dy[j] < matrix_column:
                        if row+dx[j] >= 0 and row+dx[j] < matrix_row:
                            if matrix[column+dy[j]][row+dx[j]] == 1:
                                matrix[column + dy[j]][row + dx[j]] = 0
    hour += 1
    total_count = sum(matrix, [])
    result_count = total_count.count(1)
    result.append(result_count)

print(hour)
print(result[-2])